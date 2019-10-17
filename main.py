"""
Mini Project 2 for Comparative Languages @ Wright State University
Author: Alexander Voultos
Date: 10/14/2019

Tokenizes a string input and displays the value of the tokens
"""

import ply.lex as lex


def lexing(inp):
    """
    Function for tokenizing input and displaying token value
    :param inp: (String) - Input value for tokenizing
    :return: N/A
    """

    # Initialize Token names
    tokens = ["NUM", "SYM", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN", "ERROR"]

    # Used to ignore space values in token
    t_ignore = ' \t'

    # If error is thrown, display the illegal character
    def t_error(t):
        print(f'Illegal Character {t}')

    # Token logic and regex for ADD
    def t_ADD(t):
        r'\+'
        print('ADD', end=' ')

    # Token logic and regex for SUBTRACT
    def t_SUBTRACT(t):
        r'\-'
        print('SUBTRACT', end=' ')

    # Token logic and regex for MULTIPLY
    def t_MULTIPLY(t):
        r'\*'
        print("MULTIPLY", end=' ')

    # Token logic and regex for DIVIDE
    def t_DIVIDE(t):
        r'/'
        print("DIVIDE", end=' ')

    # Token logic and regex for LPAREN
    def t_LPAREN(t):
        r'\('
        print("LPAREN", end=' ')

    # Token logic and regex for RPAREN
    def t_RPAREN(t):
        r'\)'
        print("RPAREN", end=' ')

    # Token logic and regex for NUM
    def t_NUM(t):
        r'[0-9]+[.]*[0-9]*'
        print("NUM", end=' ')

    # Token logic and regex for SYM
    def t_SYM(t):
        r'[_a-zA-Z][_a-zA-Z]*'
        print("SYM", end=' ')

    # Build the Lexer
    lexer = lex.lex()

    # Input data into lexer
    lexer.input(inp)

    # Tokenize input
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    lexing(input("Enter String: "))
#lexing("3 99 5 + 4 * 3 + 44")

