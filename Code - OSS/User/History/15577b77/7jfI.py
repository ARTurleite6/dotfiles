from pug_lexer import Lexer
from pug_parser import PugParser
from sys import argv

DATA = '''
.button(type="checkbox" nafme="agreement" checked) askdfjsdklfj
'''

def parse(parser: PugParser):

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