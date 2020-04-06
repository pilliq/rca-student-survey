#!/usr/local/bin/python3

import csv
import os
import json

res_dir = './results'
questions = {}
pages = {
    'school': {},
    'programme': {},
}

def path(fn):
    return f'{res_dir}/{fn}'

def load_questions(fn):
    with open(fn, newline='') as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            questions[row[0]] = row[1]

def page_type(fn):
    with open(fn, newline='') as f:
        r = csv.reader(f)
        header = next(r, None)
        return header[0]

def page_title(fn):
    with open(fn, newline='') as f:
        r = csv.reader(f)
        header = next(r, None)
        row = next(r, None)
        return row[0]

def get_chart(fn,q):
    chart = {
        'id': q,
        'title': questions[q],
        'data': [],
    }
    with open(fn, newline='') as f:
        r = csv.reader(f)
        header = next(r, None)
        r = csv.reader(f)
        for row in r:
            chart['data'].append([row[1], int(row[2])]) # [response, count]
    return chart

if __name__ == '__main__':
    load_questions('questions.csv')
    for root, dirs, files in os.walk(res_dir):
        for fn in files:
            page, q_ext = fn.split('-')
            q = q_ext.split('.')[0]
            pt = page_type(path(fn))
            if page not in pages[pt]:
                pages[pt][page] = {
                    'title': page_title(path(fn)),
                    'charts': [],
                }
            pages[pt][page]['charts'].append(get_chart(path(fn),q))
    print(json.dumps(pages))
