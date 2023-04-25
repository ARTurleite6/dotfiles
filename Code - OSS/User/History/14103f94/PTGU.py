import ply.yacc as yacc
from pug_lexer import PugLexer
from pug_ast.pug_ast import Block, AST

class PugParser():
    def __init__(self):
        self.tokens = PugLexer.tokens
        self.parser = yacc.yacc(module=self, debug=True)

    def parse(self, data):
        return self.parser.parse(data)

    def get_parent(self, possible_parents: list[AST], child: AST) -> AST | None:
        print("possible_parents =", possible_parents)
        reversed_list = possible_parents[::-1]

        parent = None
        for pp in reversed_list:
            print("pai =", pp, "identation =", pp.identation)
            if pp.identation < child.identation:
                return pp
        return None

    def p_html(self, p):
        '''
        html : statements
        '''
        p[0] = p[1]
    
    def p_statements_list_with_identation(self, p):
        'statements : statements IDENT statement'
        ast_statement = p[3]
        ast_statement.identation = len(p[2])
        parent = self.get_parent(p[1], p[3])
        print("parent =", parent)
        if parent:
            parent.add_child(p[3])
            p[0] = p[1]
        else:
            p[0] = p[1] + [p[3]]

    def p_statements_list_without_identation(self, p):
        'statements : statements statement'
        ast_statement = p[2]
        ast_statement.identation = 0
        p[0] = p[1] + [p[2]]
    
    def p_statements_empty(self, p):
        'statements : '
        p[0] = []

    def p_statement_block_ident(self, p):
        'statement : block'
        p[0] = p[1]
    
    def p_block_without_content(self, p):
        'block : tag_block'
        p[0] = p[1]
    
    def p_block_with_multiline_content(self, p):
        'block : tag_block DOT multiline_content'
        block = p[1]
        block.content = p[3].rstrip()
        p[0] = block
    
    def p_block_with_content(self, p):
        'block : tag_block content'
        block = p[1]
        block.content = p[2]
        p[0] = block
    
    def p_non_tag_block(self, p):
        '''
        tag_block : identifiers attributes
        '''
        p[0] = Block(attributes=p[2], identifiers=p[1])

    def p_tag_block(self, p):
        '''
        tag_block : TAG identifiers attributes
        '''
        p[0] = Block(tag=p[1], attributes=p[3], identifiers=p[2])

    def p_identifiers_list(self, p):
        '''
        identifiers : identifiers identifier
        '''
        p[0] = p[1] + [p[2]]

    def p_identifiers_empty(self, p):
        'identifiers : '
        p[0] = []

    def p_identifier(self, p):
        '''
        identifier : ID
                   | CLASS
        '''
        p[0] = p[1]

    def p_attributes_existent(self, p):
        "attributes : LPAREN attributes_list RPAREN"
        p[0] = p[2]

    def p_attributes_non_existent(self, p):
        "attributes : "
        p[0] = []

    def p_attributes_list(self, p):
        'attributes_list : attributes_list attributes_separator attribute' 
        p[0] = p[1] + [p[3]]

    def p_attributes_single(self, p):
        'attributes_list : attribute'
        p[0] = [p[1]]

    def p_attribute_with_value(self, p):
        'attribute : ATTR EQUAL ATTRVAL'
        p[0] = f"{p[1]}={p[3]}"

    def p_attribute_without_value(self, p):
        'attribute : ATTR'
        p[0] = f"{p[1]}=\"{p[1]}\""

    def p_attributes_separator(self, p):
        '''
        attributes_separator : IDENT
                             | COMMA
                             | COMMA IDENT
                             | IDENT COMMA
                             | IDENT COMMA IDENT
        '''
        p[0] = p[1]

        if len(p) >= 2:
            p[0] += p[1]
        if len(p) >= 3:
            p[0] += p[2]
        if len(p) == 4: 
            p[0] += p[3]

    def p_multiline_content_list(self, p):
        'multiline_content : multiline_content TEXT'
        p[0] = p[1] + p[2] 

    def p_multiline_content_single(self, p):
        'multiline_content : TEXT'
        p[0] = p[1] 

    def p_multiline_content_empty(self, p):
        'multiline_content : '
        p[0] = ""

    def p_content(self, p):
        '''
        content : TEXT
        '''
        print("content =", p[1])
        p[0] = p[1]

    def p_error(self, p):
        if p:
            print("Syntax error at token", p.type)
        else:
            print("Syntax error at EOF")
