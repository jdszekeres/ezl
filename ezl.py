# Author: Jackson szekeres
#purpose: main file of ezl
from lex import *

from parse import *
import sys
import os
def status(text):
    #print status in color
    print( u"\u001b[32m"+text+"\u001b[0m")
#main function
def main():
    #status("EZL Compiler")
    # if not enough arguments sys.exit
    if len(sys.argv) < 2:
        sys.exit("Error: Compiler needs source file as argument.")
    #open file that is last cli argument
    with open(sys.argv[-1], 'r') as inputFile:
        input = inputFile.read()
        inf = inputFile

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    
    parser = Parser(lexer)

    parser.program() # Start the parser.

   

main()
 