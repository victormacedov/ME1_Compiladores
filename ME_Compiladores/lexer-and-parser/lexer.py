import ply.lex as lex

# Lista de tokens
tokens = [
    'MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT',
    'JUMP', 'ATTACK', 'DEFEND',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ARROW',
    'NUMBER', 'IDENTIFIER',
    'IF', 'ELSE', 'WHILE', 'FOR',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMENT'
]

# Palavras reservadas
reserved = {
    'move_up': 'MOVE_UP',
    'move_down': 'MOVE_DOWN',
    'move_left': 'MOVE_LEFT',
    'move_right': 'MOVE_RIGHT',
    'jump': 'JUMP',
    'attack': 'ATTACK',
    'defend': 'DEFEND',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'hero': 'IDENTIFIER',
    'enemy': 'IDENTIFIER',
    'treasure': 'IDENTIFIER',
    'trap': 'IDENTIFIER'
}

# Token para comentários
def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar comentários

# Token ARROW
t_ARROW = r'->'

# Operadores lógicos
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Definir identificadores
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Checa se é palavra reservada
    return t

# Definir números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Outros tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Ignorar espaços, tabulações e novas linhas
t_ignore = ' \t\n'

# Tratamento de caracteres inválidos
def t_error(t):
    print(f"Caractere inválido ou inesperado: '{t.value[0]}'")
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()