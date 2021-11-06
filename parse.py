
# Author: Jackson szekeres
#purpose: parse incoming data in ezl programming lanugage

import sys
from lex import *
import time
import json
# Parser object keeps track of current token, checks if the code matches the grammar, and emits code along the way.
class Parser:
    def __init__(self, lexer, debug=False):
        self.lexer = lexer
        self.debug = debug
        self.line = 1
        self.symbols = set()    # All variables we have declared so far.
        self.labelsDeclared = set() # Keep track of all labels declared
        self.labelsGotoed = set() # All labels goto'ed, so we know if they exist or not.
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.
        self.hidden = dict({})
        self.main = dict({
        })
    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
 
    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name+" in line "+str(self.line))
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.

    # Return true if the current token is a comparison operator.
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)
    #abort is exit with message
    def is_var(self, ident):
        try:
            self.hidden[ident]
            return True
        except:
            return False
        return False
    def abort(self, message):
        sys.exit("Error! " + message)


#this is the main file
    def program(self):
        
        # Since some newlines are required in our grammar, need to skip the excess.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            # print('\033[91m'+self.curToken.text+'\033[0m')
            self.statement()
    def statement(self):
        # Check the first token to see what kind of statement this is.

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            self.nextToken()
            
           
            
            try:
                print(str(self.hidden[self.curToken.text]))
                self.main["PRINT line "+str(self.line)] = self.hidden[self.curToken.text]
                self.nextToken()
            except:
                self.main["PRINT line "+str(self.line)] = str(self.curToken.text)
                print(str(self.curToken.text))
                self.nextToken()

        #RAISE (STRING)
        #raise error
        elif self.checkToken(TokenType.RAISE):
            self.nextToken()
            self.main["RAISE error line "+str(self.line)] = self.curToken.text
            raise SystemError(self.curToken.text) 
            self.nextToken()
        elif self.checkToken(TokenType.IF):
            def string(str_var):
               return str("\""+str_var+"\"")
            def is_integer(n):
                try:
                    float(n)
                except ValueError:
                    return False
                else:
                    return True
            self.nextToken()
             
            #print(self.curToken.text)
            query  = str("")
            while not self.checkToken(TokenType.THEN):
                if self.is_var(self.curToken.text):
                    if is_integer(self.hidden[self.curToken.text]):
                        query = query+str(self.hidden[self.curToken.text])
                    else:
                        query = query + string(self.hidden[self.curToken.text])
                elif self.isComparisonOperator():
                    query = query + self.curToken.text
                elif is_integer(self.curToken.text):
                    query = query + str(self.curToken.text)
                else:
                    query = query + string(self.curToken.text)
                if self.debug:
                    print(self.curToken.text)
                self.nextToken()
            self.nl()
            
            self.main["IF line "+str(self.line)] = str(eval(query))
 
            if eval(query):

                self.nextToken()
                self.nl()
                while not self.checkToken(TokenType.ENDIF):
                    self.statement()
                self.nextToken()
            else:
                self.nextToken()
                self.nl()
                while not self.checkToken(TokenType.ENDIF):
                    self.nextToken()
                self.nextToken()
        #WAIT float
        #wait before contining
        elif self.checkToken(TokenType.WAIT): 
            self.nextToken()
            try:
                self.main["WAIT line "+str(self.line)] = str(self.curToken.text)
                time.sleep(float(self.curToken.text))
                self.nextToken()
            except:
                self.abort('Input passed is not a float')
 # "LET" ident = expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()

            #  Check if ident exists in symbol table. If not, declare it.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
                var = self.curToken.text
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            
            if self.checkToken(TokenType.STRING):
                self.hidden[var] = self.curToken.text
                self.main["varible "+var] = self.hidden[var]         
                self.nextToken()
            else:
                self.hidden[var] = self.curToken.text
                self.main["varible "+var] = self.hidden[var]
                self.nextToken()
            #print(self.curToken.text)   
            #self.nextToken()


        # "INPUT" ident
        elif self.checkToken(TokenType.INPUT):
            self.nextToken()

            # If variable doesn't already exist, declare it.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
                self.hidden[self.curToken.text] = input("")
                self.main["varible "+self.curToken.text] = self.hidden[self.curToken.text]
            self.match(TokenType.IDENT)

            
        elif self.checkToken(TokenType.EXPORT):
            self.nextToken()
            if self.checkToken(TokenType.STRING):
                with open(self.curToken.text, "w+") as f:
                    json.dump(self.main, indent = 4, fp = f)
            self.nextToken()
        # This is not a valid statement. Error!
        else:
            self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ") in line "+str(self.line))
        #line count so you know the line # for errors
        self.line += 1
        # Newline.
        self.nl()


    # comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
    def comparison(self):
        self.expression()
        # Must be at least one comparison operator and another expression.
        if self.isComparisonOperator():
            
            self.nextToken()
            self.expression()
        # Can have 0 or more comparison operator and expressions.
        while self.isComparisonOperator():
            yield self.curToken.text
            self.nextToken()
            self.expression()


    # expression ::= term {( "-" | "+" ) term}
    def expression(self):
        self.term()
        # Can have 0 or more +/- and expressions.
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            yield self.curToken.text
            self.nextToken()
            self.term()


    # term ::= unary {( "/" | "*" ) unary}
    def term(self):
        self.unary()
        # Can have 0 or more *// and expressions.
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH) or self.checkToken(TokenType.MOD):
            yield self.curToken.text
            self.nextToken()
            self.unary()


    # unary ::= ["+" | "-"] primary
    def unary(self):
        # Optional unary +/-
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            yield self.curToken.text
            self.nextToken()        
        self.primary()


    # primary ::= number | ident
    def primary(self):
        if self.checkToken(TokenType.FLOAT): 
            yield self.curToken.text
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            # Ensure the variable already exists.
            if self.curToken.text not in self.symbols:
                self.abort("Referencing variable before assignment: " + self.curToken.text)

            return self.curToken.text
            self.nextToken()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)

    # nl ::= '\n'+
    def nl(self):
        # Require at least one newline.
        self.match(TokenType.NEWLINE)
        # But we will allow extra newlines too, of course.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()