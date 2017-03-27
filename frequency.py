""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    raw_text = open(file_name, 'r')
    lines = raw_text.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    all_text = lines[curr_line+1:]
    stripped_words = ["".join(c for c in word if c not in string.punctuation) for word in
                      [val for sublist in [line.split() for line in all_text] for val in sublist]]
    return stripped_words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_dict = {i: word_list.count(i) for i in set(word_list)}
    sorted_words = list(sorted(word_dict, key=word_dict.get, reverse=True))
    [print("Word: {}\t Frequency: {}".format(sorted_words[idx], word_dict[sorted_words[idx]])) for idx in range(n)]


if __name__ == "__main__":
    words = get_word_list("pg84.txt")
    get_top_n_words(words, 100)
