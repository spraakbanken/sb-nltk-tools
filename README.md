
# Språkbanken NLTK Corpus Reader

The main module, `sb_corpus_reader.py`, 
contains the class SBCorpusReader,
which is an implementation of the NLTK CorpusReader api

This corpus reader is intended to be used with 
Språkbanken's downloadable corpora, which can be obtained
from here: https://spraakbanken.gu.se/eng/resources/

For more information about NLTK and the CorpusReader api,
please see the NLTK site: http://www.nltk.org/

### Installation

Just put the file `sb_corpus_reader.py` in your working directory.

Make sure that NLTK is installed.

You can test if it works by running the test file:

1. Download and decompress the Talbanken corpus: https://spraakbanken.gu.se/eng/resource/talbanken

2. From the command line, run: `python3 sb_postagger_test.py`

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
