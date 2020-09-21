from lex import *
from emit import *
from parse import *
import sys
import os
def status(text):
    print( u"\u001b[32m"+text+"\u001b[0m")
def main():
    print("EZL Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
        inf = inputFile

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter(sys.argv[1].split(".")[0]+".c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    status("written to file")
    os.system("gcc "+sys.argv[1].split(".")[0]+".c -o "+ sys.argv[1].split(".")[0])
    status("compiled")
    os.system("chmod +x "+sys.argv[1].split(".")[0])
    status("made execuatable")
    print("run this as ", end="")
    print("./"+sys.argv[1].split(".")[0])
   

main()
