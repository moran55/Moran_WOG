import flask


def score_server():
    f_res = open('Scores.txt', 'r')
    lines = f_res.read()
