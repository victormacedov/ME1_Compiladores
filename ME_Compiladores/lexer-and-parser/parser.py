import ply.yacc as yacc

# Importar tokens do lexer
from lexer import tokens

# Regras de gramática
def p_S(p):
    '''S : cmd
         | cmd S
         | if_stmt
         | if_stmt S
         | while_stmt
         | while_stmt S
         | for_stmt
         | for_stmt S
         | expr
         | expr S
         | COMMENT
         | COMMENT S
         | empty'''  # Suporte para entradas vazias
    pass

def p_empty(p):
    '''empty :'''
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
            | expr TIMES expr
            | expr DIVIDE expr
            | expr ARROW expr'''
    pass

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe! Token inesperado: {p.type} ('{p.value}') na linha {getattr(p, 'lineno', 'desconhecida')}")
    else:
        print("Erro de sintaxe! EOF inesperado. Verifique se você fechou todos os blocos, parênteses ou expressões iniciadas antes do fim do arquivo.")

# Criação do parser
parser = yacc.yacc()
