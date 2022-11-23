# File: WordleAssistant.py
# Student: Jawad Kazi
# UT EID: JAK4774
# Course Name: CS303E
#
# Date: 11/3/22
# Description of Program: The program provides a suite of functions that can aide in finding proper words for a wordle puzzle. This suite includes determining which words have certain letters, don't have certain lettes, and have certain letters in certain indexes of the word. Finally, all three of these paramters can be set at the convenience of the user utilizing one single function.

def createWordlist(filename):
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """
    with open(filename, 'r') as f:
        new_wordlist = set()
        wordlist = f.readlines()
        for word in wordlist:
            # remove newline at end
            word = word[:-1]
            if len(word) < 6 and word[-1] != 's' and len(set(word)) == len(word):
                new_wordlist.add(word)
        return new_wordlist, len(new_wordlist)


def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.
    """
    new_wordlist = set()
    for word in wordlist:
        notin = False
        for letter in include:
            if letter not in word:
                notin = True
        if notin:
            continue
        new_wordlist.add(word)
    return new_wordlist

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.
    """
    new_wordlist = set()
    for word in wordlist:
        notin = False
        for letter in exclude:
            if letter in word:
                notin = True
        if notin:
            continue
        new_wordlist.add(word)
    return new_wordlist


def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    new_wordlist = set()
    for word in wordlist:
        notin = False
        for key, value in posInfo.items():
            try:
                if word[value] != key:
                    notin = True
            except IndexError:
                notin = True
        if notin:
            continue
        new_wordlist.add(word)
    return new_wordlist


def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from
    the wordlist that contains the words that satisfy all of
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    new_wordlist = containsAll(wordlist, include)
    new_wordlist = containsNone(new_wordlist, exclude)
    print(new_wordlist)
    new_wordlist = containsAtPositions(new_wordlist, posInfo)
    return new_wordlist

