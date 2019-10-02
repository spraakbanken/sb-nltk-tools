"""
Run some POS tagging tests from the NLTK book 
(primarily chapter 5, section 4)

You need to download a corpus from Språkbanken first,
e.g., Talbanken which is manually POS-annotated
(https://spraakbanken.gu.se/eng/resource/talbanken)
"""

import sys
import nltk
from sb_corpus_reader import SBCorpusReader

if len(sys.argv) != 2:
    sys.exit("Usage: %s corpus-file.xml" % (sys.argv[0],))
corpuspath = sys.argv[1]

corpus = SBCorpusReader(corpuspath)
tagged_sents = corpus.tagged_sents()
print(corpus.readme())
print("No. sentences:", len(tagged_sents))
print()

print("* Separating training and testing data (NLTK book, sec 5.2)")
breakpoint = int(len(tagged_sents) * 0.9)
train_sents = tagged_sents[:breakpoint]
test_sents = tagged_sents[breakpoint:]
print("No. train sentences:", len(train_sents))
print("No. test  sentences:", len(test_sents))
print()

seen_example = nltk.untag(tagged_sents[10])
unseen_example = nltk.untag(tagged_sents[-10])
def show_example(tagged_sent):
    return " ".join(map(nltk.tuple2str, tagged_sent))

print("* Default tagger (NLTK book, sec 4.1)")
tags = [tag for sent in train_sents for (word, tag) in sent]
most_common_tag = nltk.FreqDist(tags).max()
print("Most common tag:", most_common_tag)
default_tagger = nltk.DefaultTagger(most_common_tag)
print("Seen  :", show_example(default_tagger.tag(seen_example)))
print("Unseen:", show_example(default_tagger.tag(unseen_example)))
print("Evaluation:", default_tagger.evaluate(test_sents))
print()

print("* Unigram tagger (NLTK book, sec 5.1)")
unigram_tagger = nltk.UnigramTagger(train_sents)
print("Seen  :", show_example(unigram_tagger.tag(seen_example)))
print("Unseen:", show_example(unigram_tagger.tag(unseen_example)))
print("Evaluation:", unigram_tagger.evaluate(test_sents))
print()

print("* Bigram tagger (NLTK book, sec 5.3)")
bigram_tagger = nltk.BigramTagger(train_sents)
print("Seen  :", show_example(bigram_tagger.tag(seen_example)))
print("Unseen:", show_example(bigram_tagger.tag(unseen_example)))
print("Evaluation:", bigram_tagger.evaluate(test_sents))
print()

print("* Affix tagger (NLTK book, sec 10, exercise 11)")
affix_tagger = nltk.AffixTagger(train_sents, affix_length=-3, min_stem_length=1)
print("Seen  :", show_example(affix_tagger.tag(seen_example)))
print("Unseen:", show_example(affix_tagger.tag(unseen_example)))
print("Evaluation:", affix_tagger.evaluate(test_sents))
print()

print("* Combining taggers (NLTK book, sec 5.4)")
t0 = nltk.AffixTagger(train_sents, affix_length=-3, min_stem_length=1, backoff=default_tagger)
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print("Evaluation, affix   backoff tagger:", t0.evaluate(test_sents))
print("Evaluation, unigram backoff tagger:", t1.evaluate(test_sents))
print("Evaluation, bigram  backoff tagger:", t2.evaluate(test_sents))
print("Evaluation, trigram backoff tagger:", t3.evaluate(test_sents))
print()

print("* Performance limitations (NLTK book, sec 5.7)")
cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in tagged_sents
    for x, y, z in nltk.trigrams(sent))
ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print("Trigram ambiguity:", sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N())

print("Confusion matrix for bigram backoff tagger:")
test_tags = [tag for sent in test_sents for (word, tag) in t2.tag(nltk.untag(sent))]
gold_tags = [tag for sent in test_sents for (word, tag) in sent]
print(nltk.ConfusionMatrix(gold_tags, test_tags))
print()

print("* TnT tagger (not in NLTK book)")
tnt_tagger = nltk.TnT()
tnt_tagger.train(train_sents)
print("Seen  :", show_example(tnt_tagger.tag(seen_example)))
print("Unseen:", show_example(tnt_tagger.tag(unseen_example)))
print("Evaluation, TnT tagger:", tnt_tagger.evaluate(test_sents))
print()

print("* HMM tagger (not in NLTK book)")
hmm_tagger = nltk.HiddenMarkovModelTagger.train(train_sents)
print("Seen  :", show_example(hmm_tagger.tag(seen_example)))
print("Unseen:", show_example(hmm_tagger.tag(unseen_example)))
print("Evaluation, HMM tagger:", hmm_tagger.evaluate(test_sents))
print()

print("* Perceptron tagger (not in NLTK book)")
perp_tagger = nltk.PerceptronTagger(load=False)
perp_tagger.train(train_sents)
print("Seen  :", show_example(perp_tagger.tag(seen_example)))
print("Unseen:", show_example(perp_tagger.tag(unseen_example)))
print("Evaluation, perceptron tagger:", perp_tagger.evaluate(test_sents))
print()


