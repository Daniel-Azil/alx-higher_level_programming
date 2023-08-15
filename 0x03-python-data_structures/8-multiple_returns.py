#!/usr/bin/python3
def multiple_returns(sentence):
    var = len(sentence)
    if (var == 0):
        strc_rtn = (var, None)
    else:
        strc_rtn = (var, sentence[0])
    return (strc_rtn)
