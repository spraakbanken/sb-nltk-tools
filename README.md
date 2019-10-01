
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

Import the module:
```
from sb_corpus_reader import SBCorpusReader
```

Use the corpus reader:
```
corpus = SBCorpusReader('talbanken.xml')
corpus.sents()
corpus.tagged_words()
...
```


