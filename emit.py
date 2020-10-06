# Author: Jackson szekeres
#purpose: store the code to be writen to C file

class Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.header = ""
        self.code = ""
        #code and header put together then saved to file
    def emit(self, code):
        self.code += code
        #add directly
    def emitLine(self, code):
        self.code += code + '\n'
        #add new line
    def headerLine(self, code):
        self.header += code + '\n'
        #add header
    def writeFile(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.header + self.code)
            #write to output