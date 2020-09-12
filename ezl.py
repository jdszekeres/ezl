from lex import *
from emit import *
from parse import *
import sys
import os
def main():
    print("Teeny Tiny Compiler")

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
    os.system("gcc "+sys.argv[1].split(".")[0]+".c -o "+ sys.argv[1].split(".")[0])
    os.system("chmod +x "+sys.argv[1].split(".")[0])
    print("Compiling completed.")

main()
