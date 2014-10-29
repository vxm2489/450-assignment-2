  from sys import *

#Initialize Variables
size        = 100
lexeme      = [''] * size
input_file  = None
LETTER      = 0
DIGIT       = 1
UNKNOWN     = 99
EOF         = -1
nextToken   = 1
nextChar    = ""

INT_LIT     = 10
IDENT       = 11
ASSIGN_OP   = 20
ADD_OP      = 21
SUB_OP      = 22
MULT_OP     = 23
DIV_OP      = 24
LEFT_PAREN  = 25
RIGHT_PAREN = 26

#main driver
def main():
    global input_file,nextToken
    try:
        try:
            input_file = open("front.in", "r")   # Open Input file                  
        except Exception, e:
            print "ERROR: cannot open front.in"   # Print Exception if input file cannot be opened
        finally:
            getChar()                             # call getChar() to read the i/p file
            charFlag = 0  
        while nextToken != EOF:                   # Check for End of the File      
            lex()                                 # if EOF not reached, call lex() function 
            charFlag = charFlag + 1
        input_file.close()                        # close input file
    except Exception, e:
        print e                                   #prints exception



# getChar - a function to get the next character of  input and determine its character class
def getChar():
    global input_file,charClass,nextChar
    try:
        read_char = input_file.read(1) 
        if read_char != "-1"
            nextChar = read_char
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN            
        else:
            charClass = EOF
            nextChar = '\0'        
    except Exception, e:
        print e

# addChar - a function to add nextChar to lexeme        
def addChar():
    if lexLen <= 98:       
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error:lexeme is too long."
        
# getNonBlank - a function to call getChar until it returns a non-whitespace character
def getNonBlank():
    while nextChar.isspace():
        getChar()

#lookup - a function to lookup operators and parentheses and return the token
def lookup(ch):      
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    
# lex - a simple lexical analyzer for arithmetic expressions
def lex():
    global lexLen,lexeme,nextToken,charClass
    lexLen = 0
    lexeme = [''] * size
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()        
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'EOF'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
    
    if nextToken == -1:
      print "Next token is: " + str(nextToken) + " Next lexeme is EOF " 
    else:
      print "Next token is: " + str(nextToken) + " Next lexeme is " + str(lexeme[1])
    
main()            #Calling Main function
