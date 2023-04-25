from pug_lexer import Lexer
from pug_parser import PugParser
from sys import argv

DATA = '''
.button(type="checkbox" nafme="agreement" checked) askdfjsdklfj
'''

def lex_input(lexer: PugLexer):
    global DATA

    lexer.input(DATA)

    while tok := lexer.token():
        print(tok)

def parse(parser: PugParser):
    global DATA
    results = parser.parse(data=DATA)

    for result in results:
        print(result)

def main():
    lexer = Lexer() 
    parser = PugParser()

    if len(argv) == 1:
        print("Missing arguments")
        return

    command = argv[1]

    if command == "parse":
        parse(parser)
    else:
        lex_input(lexer)




if __name__ == "__main__":
    main()