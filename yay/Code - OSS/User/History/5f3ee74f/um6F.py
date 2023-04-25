import ply.lex as lex

class PugLexer():

    states = (
        ('tag', 'exclusive'),
        ('attributes', 'exclusive'),
        ('multilinecontent', 'exclusive'),
    )

    tokens = (
            'TAG',
            'CLASS',
            'ID',
            'LPAREN',
            'RPAREN',
            'ATTR',
            'ATTRVAL',
            'TEXT',
            'IDENT',
            'DOT',
            'EQUAL',
            'COMMA',
            'NEWLINE',
            )

    t_ignore = '\n'
    
    t_tag_ignore = '\n\t'
    t_attributes_ignore = ''
    t_multilinecontent_ignore = ''

    def __init__(self) -> None:
        self.lexer = lex.lex(module=self)
        self.current_identation = 0

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def check_zero_identation(self, token):
        if self.current_identation != 0:
            return
        next_char = token.lexer.peak()

        if next_char not in [' ', '\t']:
            token.lexer.begin('INITIAL')

    def t_multilinecontent_IDENT(self, t):
        r'[\s\t]+'
        new_identation = len(t.value)
        print("new_identation=", new_identation)
        print("current_identation=", self.current_identation)

        if new_identation <= self.current_identation:
            t.lexer.begin('INITIAL')
            self.current_identation = new_identation
        pass

    def t_multilinecontent_TEXT(self, t):
        r'[^\n]+\n'
        self.check_zero_identation(t)
        return t

    def t_tag_ID(self, t):
        r'\#(\w(?!(\.|\#)))+\w'
        return t

    def t_tag_CLASS(self, t):
        r'\.(\w(?!(\.|\#)))+\w'
        return t

    def t_tag_DOT(self, t):
        r'\.\n'
        t.lexer.begin('multilinecontent')
        self.check_zero_identation(t)
        return t

    def t_ID(self, t):
        r'\#(\w(?!(\.|\#)))+\w'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('tag')
        return t

    def t_CLASS(self, t):
        r'\.(\w(?!(\.|\#)))+\w'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('tag')
        return t
    
    def t_TAG(self, t):
        r'(\w(?!(\.|\#)))+\w'
        t.lexer.begin('tag')
        return t

    def t_tag_LPAREN(self, t):
        r'\('
        t.lexer.begin('attributes')
        return t

    def t_attributes_RPAREN(self, t):
        r'\)'
        t.lexer.begin('tag')
        return t

    def t_attributes_ATTRVAL(self, t):
        r'(\'[^\']+\'|\"[^\"]+\")'
        return t

    def t_attributes_EQUAL(self, t):
        r'\='
        return t

    def t_attributes_ATTR(self, t):
        r'\w+'
        return t

    def t_attributes_IDENT(self, t):
        r'[\s\n\t]+'
        return t

    def t_attributes_COMMA(self, t):
        r'\,'
        return t

    def t_tag_TEXT(self, t):
        r'\s+[^\n]+'
        t.lexer.begin('INITIAL')
        t.value = t.value.lstrip()
        return t

    def t_IDENT(self, t):
        r'^[\s\t]+'
        self.current_identation = len(t.value)
        return t

    def t_error(self, t):
        print("error on ", t.value, "type = ", t.type)
        t.lexer.skip(1)

    def t_tag_error(self, t):
        print("Tag state error on ", t.value, "type = ", t.type)
        t.lexer.skip(1)

    def t_attributes_error(self, t):
        print("Attributes state error on ", t.value, "type = ", t.type)
        t.lexer.skip(1)

    def t_multilinecontent_error(self, t):
        print("Multiline Content state error on ", t.value, "type = ", t.type)
        t.lexer.skip(1)
