#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""wcount.py: count words from an Internet file.

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def alnumify(word):
    """convert freshly split words to ones containing only
    alphanumeric characters
    """
    new_word = ''        # do not modify the original word
    if not word.isalnum():
        for letter in word:
            if letter.isalnum():
                new_word += letter
    else:
        new_word = word
    return new_word


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    # process the input lines
    words = lines.replace(".", " ").lower().split()

    # create a dictionary which functions just like a real-life dictionary
    dict_counts = {}
    for word in words:
        word = alnumify(word)
        dict_counts[word] = dict_counts.get(word, 0) + 1
    del dict_counts['']  # removes empty strings caused by alnumify()

    # sort and reverse the dictionary
    reverse_list = []
    for (k, v) in dict_counts.items():
        reverse_list += [(v, k)]
    reverse_list.sort(reverse=True)

    # fetch the information needed for display
    items_slice = reverse_list[:topn]
    for (k, v) in items_slice:
        print(v.ljust(12) + str(k))


if __name__ == '__main__':

    # user interface
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    # handle input error
    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    # handle file error and other exceptions
    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
