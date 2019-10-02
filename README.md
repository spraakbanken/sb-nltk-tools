
# Språkbanken NLTK Corpus Reader

The main module, `sb_corpus_reader.py`, 
contains the class SBCorpusReader,
which is an implementation of the NLTK CorpusReader api.
The SBCorpusReader is intended to be used with 
[Språkbanken's downloadable corpora](https://spraakbanken.gu.se/eng/resources/).

For more information about NLTK and the CorpusReader api,
please see the [NLTK website](http://www.nltk.org/).

--------
### Installation

Make sure NLTK is installed.
Put the file `sb_corpus_reader.py` in your working directory. 
You can test if it works by running the test file:

1. Download and extract the [Talbanken corpus](https://spraakbanken.gu.se/eng/resource/talbanken).
Put the decompressed file `talbanken.xml` in your working directory.

2. From the command line, run: `python3 sb_postagger_test.py`

--------
### Usage

Import NLTK and the SBCorpusReader, and use like this:
```
>>> import nltk
>>> from sb_corpus_reader import SBCorpusReader
>>> talbanken = SBCorpusReader('talbanken.xml')
>>> talbanken.sents()
[['Individuell', 'beskattning', 'av', 'arbetsinkomster'], ['Genom', 'skattereformen', 'införs', 'individuell', 'beskattning', '(', 'särbeskattning', ')', 'av', 'arbetsinkomster', '.'], ...]
>>> talbanken.tagged_words()
[('Individuell', 'JJ'), ('beskattning', 'NN'), …]
>>> fd = nltk.FreqDist(talbanken.words())
>>> fd
FreqDist({'.': 5178, ',': 2859, 'och': 2486, 'i': 2240, 'att': 2052, 'som': 1587, 'är': 1456, 'en': 1383, 'av': 1335, 'på': 1153, ...})
>>> fd.freq('och')
0.02580283561331036
>>> fd.freq('universitetet')
3.113777427189504e-05
>>> text = nltk.Text(talbanken.words())
>>> text.concordance("universitetet")
Displaying 3 of 3 matches:
  enligt doc. Göran Bergman , vid universitetet i Helsingfors , saknar hunden fö
 g bl.a. . Prof. Stig Larsson vid universitetet i Odense påpekar att man ofta ge
 itetsstaden ; i några fall utgör universitetet och studenterna fortfarande stad
```

--------
### Assorted notes

#### Python version

The module is designed for Python version ≥3.4, and NLTK version ≥3. It's currently only tested in Python 3.7.4, and NLTK 3.4.5.

#### Språkbanken corpus format

The SBCorpusReader is very tailor-made for Språkbanken’s export format, which is an xml format but where two xml tags are never on the same line. There might be some corpora that are exported in another format, and therefore cannot be read by SBCorpusReader.

#### Large corpora

Språkbanken has lots of large corpora, and this wrapper should work regardless of corpus size... if your computer can handle it. NLTK's corpus reader is lazy and only reads parts of the corpus into memory at the time, which makes it possible to work with really large texts. But things can take very long time... to build a nltk.FreqDist() over the words in the [Åtta sidor corpus](https://spraakbanken.gu.se/eng/resource/attasidor) (2.8 M words) takes more than a minute on a modern laptop.

#### Future work

So far, the SBCorpusReader has only implemented the following methods of the nltk.CorpusReader interface:

- `.words()` and `.tagged_words()`
- `.sents()` and `.tagged_sents()`

More methods will come in the future, such as `.tagged_texts()` or `.parsed_sents()`.
