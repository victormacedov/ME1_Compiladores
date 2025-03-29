import ply.yacc as yacc

# Importar tokens do lexer
from lexer import tokens

# Definição da precedência dos operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras de gramática
def p_S(p):
    '''S : cmd
         | if_stmt
         | while_stmt
         | for_stmt
         '''
    pass

def p_cmd(p):
    '''cmd : move_cmd
           | action_cmd'''
    pass

def p_move_cmd(p):
    '''move_cmd : MOVE_UP
                | MOVE_DOWN
                | MOVE_LEFT
                | MOVE_RIGHT'''
    pass

def p_action_cmd(p):
    '''action_cmd : JUMP
                  | ATTACK
                  | DEFEND'''
    pass

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expr RPAREN LBRACE S RBRACE ELSE LBRACE S RBRACE'''
    pass

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN expr RPAREN LBRACE S RBRACE'''
    pass

def p_for_stmt(p):
    '''for_stmt : FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN LBRACE S RBRACE'''
    pass

def p_expr(p):
    '''expr : IDENTIFIER
            | NUMBER
            | expr PLUS expr
            | expr MINUS expr
            '''
    pass

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe! Token inesperado: {p.type} ('{p.value}') na linha {getattr(p, 'lineno', 'desconhecida')} na posição {getattr(p, 'lexpos', 'desconhecida')}")
    else:
        print("Erro de sintaxe! EOF inesperado. Verifique se você fechou todos os blocos, parênteses ou expressões iniciadas antes do fim do arquivo.")

# Criação do parser
parser = yacc.yacc()
