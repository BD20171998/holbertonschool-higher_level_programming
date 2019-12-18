#!/usr/bin/python3


def multiple_returns(sentence):

    if not sentence or sentence == "":
        return None

    l = len(sentence)

    return l, sentence[0:1]
