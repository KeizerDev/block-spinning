import random
import re

BLOCKS_REGEX = r"#block#((?:(?=([^#]+))\2|#(?!/?block#))*)#/block#"
PARAGRAPH_REGEX = r"#p#((?:(?=([^#]+))\2|#(?!/?p#))*)#/p#"
SENTENCE_TAG = "#s#"
EMPTY_STRING = ""


def _parse_blocks(string):
    """
    Function to get blocks out of the given string
    :param string:
    :return array:
    """
    matches = re.findall(BLOCKS_REGEX, string)
    return [match[0].strip() for match in matches]


def _parse_sentences(string):
    """
    Function to get all the paragraphs out of a giving block
    :param string:
    :return array:
    """
    sentences = string.split(SENTENCE_TAG)

    # Remove last element because of the last ending #s#
    sentences.pop()

    return [sentence.strip() for sentence in sentences]


def _parse_paragraphs(string):
    """
    Function to get all the paragraphs out of a giving block
    :param string:
    :return array:
    """
    matches = re.findall(PARAGRAPH_REGEX, string)
    return [match[0] for match in matches]


def _random_sentences(sentences):
    return random.choice(sentences)


def spin(string, lock_first=False, limit_of_blocks=None):
    """
    Function used to block spin a string
    :param string:
    :param lock_first:
    :param limit_of_blocks:
    :return string:
    """

    blocks = [[[sentences for sentences in _parse_sentences(paragraph)] for paragraph in _parse_paragraphs(block)] for
              block in _parse_blocks(string)]

    if lock_first:
        blocks_with_lock_first = blocks[1:]
        random.shuffle(blocks_with_lock_first)
        blocks = [blocks[0]] + blocks_with_lock_first
    else:
        random.shuffle(blocks)

    if limit_of_blocks is not None:
        blocks = blocks[:limit_of_blocks]

    result = ""

    for block in blocks:
        if result != "":
            result += "\n" * 2

        for paragraph in block:
            result += _random_sentences(paragraph)

    return result
