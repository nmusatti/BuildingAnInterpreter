'''
Created on May 23, 2015

@author: nick
'''

import readline

import snap.parser


def repl():
    while True:
        line = raw_input("> ")
        if len(line) == 0:
            return
        print(snap.parser.parse(line))

if __name__ == '__main__':
    repl()
