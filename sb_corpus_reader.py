"""
This module contains the class SBCorpusReader,
which is an implementation of the NLTK CorpusReader api

This corpus reader is intended to be used with 
Språkbanken's downloadable corpora, which can be obtained
from here: https://spraakbanken.gu.se/eng/resources/

Currently, only the following CorpusReader instance methods 
are implemented:
- .words() and .tagged_words()
- .sents() and .tagged_sents()
"""

import nltk
import os.path

try:
    import xml.etree.cElementTree as ET
except ModuleNotFoundError:
    import xml.etree.ElementTree as ET


# number of sentences to read in a block
SENTS_PER_BLOCK = 1


class SBCorpusReader(nltk.corpus.CorpusReader):
    def __init__(self, path, encoding='utf-8'):
        self._fileid = path
        self._basename = os.path.basename(path).partition('.')[0]
        self._encoding = encoding

    def readme(self):
        return "Språkbanken reader for the corpus: %s" % (self._basename,)

    def words(self):
        return self._corpus_view(self._read_word_block)

    def tagged_words(self):
        return self._corpus_view(self._read_tagged_word_block)

    def sents(self):
        return self._corpus_view(self._read_sent_block)

    def tagged_sents(self):
        return self._corpus_view(self._read_tagged_sent_block)

    def paras(self):
        raise NotImplementedError

    def tagged_paras(self):
        raise NotImplementedError


    def _corpus_view(self, block_reader):
        return nltk.corpus.reader.StreamBackedCorpusView(self._fileid, block_reader, encoding=self._encoding)

    def _read_word_block(self, stream):
        words = self._read_tagged_word_block(stream)
        return [w[0] for w in words]

    def _read_tagged_word_block(self, stream):
        sents = self._read_tagged_sent_block(stream)
        return [w for ws in sents for w in ws]

    def _read_sent_block(self, stream):
        sents = self._read_tagged_sent_block(stream)
        return [[w[0] for w in ws] for ws in sents]

    def _read_tagged_sent_block(self, stream):
        sents = []
        for i in range(SENTS_PER_BLOCK):
            lines = None
            for line in stream:
                line = line.strip()
                if not line:
                    continue
                assert line.startswith('<')
                if lines is None:
                    if line.startswith('<sentence'):
                        lines = []
                    elif line.startswith('<w ') or line.startswith('<ne '):
                        lines = ['<sentence>']
                else:
                    assert not line.startswith('<sentence')
                if lines is not None:
                    lines.append(line)
                if '</sentence' in line:
                    break
            if lines is not None:
                xml = ET.fromstring("".join(lines))
                sents.append([self._get_tagged_word(elem) for elem in xml.iter('w')])
        return sents

    @staticmethod
    def _get_tagged_word(elem):
        return ("".join(elem.itertext()), elem.attrib.get('pos'))

