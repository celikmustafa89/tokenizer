# -*- coding: utf-8 -*-

import nltk
import codecs
import string

__author__ = 'Mustafa ÇELİK'


def write_list_to_file(filename, liste):
    """Writes list elements in to the given filename.

    :param filename: filename of the output.
    :param liste: list of the data that will be writen to the file.
    :return: None
    """
    with open(filename, 'w') as f:
        for s in liste:
            f.write(s + '\n')


def read_list_from_file(filename):
    """Reads list of elements from the given filename.

    :param filename: filename of the input.
    :return: list of the given file.
    """
    with open(filename, 'r') as f:
        liste = [line.rstrip('\n') for line in f]
    return liste


def punc_tokenizer(tokens, word_tokens):
    """Returns the list of all punctuation tokens.

    :param tokens: All tokens in the corpus.
    :param word_tokens: All word tokens in the corpus.
    :return: list of all punctuation tokens.
    """

    punc_tokens = list(set(tokens) - set(word_tokens))  # [x for x in tokens if x not in word_tokens]
    print('number of punctuations: {0}'.format(len(punc_tokens)))
    print('number of distinct punctuations: {0}'.format(len(set(punc_tokens))))
    print('number of distinct punctuations: {0}\n'.format(len(nltk.FreqDist(punc_tokens).keys())))

    return punc_tokens


def word_tokenizer_without_punc(raw_data):
    """Returns the list of all word tokens.

    :param raw_data: gets codecs.open("..../filename", 'r', 'utf-8').read()
    :return: list of all word tokens without punctuations
    """

    punctuations = list(string.punctuation)
    punctuations.append("''")
    tokens = nltk.word_tokenize(raw_data)
    words = [i.strip("".join(punctuations)) for i in tokens if i not in punctuations]
    print('number of words: {0}'.format(len(words)))
    print('number of distinct words: {0}'.format(len(set(words))))
    print('number of distinct words: {0}\n'.format(len(nltk.FreqDist(words).keys())))

    return words


def tokenizer(raw_data):
    """Returns the list of all tokens.

    :param raw_data: gets codecs.open("..../filename", 'r', 'utf-8').read()
    :return: list of all tokens
    """
    # fp = codecs.open("/home/joker/nltk_data/corpora/gutenberg/42binhaber.txt", 'r', 'utf-8')
    # tokens = nltk.word_tokenize(fp.read())
    tokens = nltk.word_tokenize(raw_data)
    fdist = nltk.FreqDist(tokens)

    print('number of tokens: {0}'.format(len(tokens)))
    print('number of distinct tokens: {0}'.format(len(set(tokens))))
    print('number of distinct tokens: {0}\n'.format(len(fdist.keys())))

    return tokens


def sentence_tokenizer(raw_data):
    """Returns the list of the sentences.

    :param raw_data: gets codecs.open("..../filename", 'r', 'utf-8').read()
    :return: list of sentences
    """
    sent_detector = nltk.data.load('tokenizers/punkt/turkish.pickle')
    sentences = sent_detector.tokenize(raw_data.strip())
    print('number of sentences: {0}'.format(len(sentences)))
    print('number of distinct sentences: {0}\n'.format(len(set(sentences))))
    return sentences


def main():
    """Finds all tokens, word tokens, punctuation tokens, and all distinct tokens.

    :return: counts tokens for each type. Prints tokens to files. And prints console outputs to file.
    """
    fp = codecs.open("/home/joker/nltk_data/corpora/gutenberg/42binhaber.txt", 'r', 'utf-8')
    raw_data = fp.read()

    # splits sentences
    sentences = sentence_tokenizer(raw_data)
    write_list_to_file("sentences.txt", sentences)

    # split tokens
    tokens = tokenizer(raw_data)
    write_list_to_file("all_tokens.txt", tokens)

    # split word tokens
    word_tokens = word_tokenizer_without_punc(raw_data)
    write_list_to_file("word_tokens.txt", word_tokens)

    # split punctuation tokens
    punc_tokens = punc_tokenizer(tokens, word_tokens)
    write_list_to_file("punc_tokens.txt", punc_tokens)


if __name__ == '__main__':
    main()
