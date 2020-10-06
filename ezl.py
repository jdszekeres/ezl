# Author: Jackson szekeres
#purpose: main file of ezl
from lex import *
from emit import *
from parse import *
import sys
import os
def status(text):
    #print status in color
    print( u"\u001b[32m"+text+"\u001b[0m")
#main function
def main():
    print("EZL Compiler")
    # if not enough arguments sys.exit
    if len(sys.argv) < 2:
        sys.exit("Error: Compiler needs source file as argument.")
    #open file that is last cli argument
    with open(sys.argv[-1], 'r') as inputFile:
        input = inputFile.read()
        inf = inputFile

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter(sys.argv[-1].split(".")[0]+".c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    status("written to file")
    #if no gcc argument then ignore this step
    if not "--no-gcc" in sys.argv:
        os.system("gcc "+sys.argv[-1].split(".")[0]+".c -o "+ sys.argv[-1].split(".")[0])
        status("compiled")
    #chmod +x makes the file executable
    os.system("chmod +x "+sys.argv[-1].split(".")[0])
    status("made execuatable")
    #this tells you how to run this file
    print("run this as ", end="")
    print("./"+sys.argv[-1].split(".")[0])
   

main()
 