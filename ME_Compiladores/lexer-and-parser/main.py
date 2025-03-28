from lexer import lexer  # Importa o lexer do arquivo lexer.py
from parser import parser  # Importa o parser do arquivo parser.py

def main():
    code = """
    // Este é um comentário
    move_up
    move_down
    hero + treasure
    if (hero -> treasure) { attack } else { defend }
    // Comentário após comandos
    """

    print("=== Início do Analisador Léxico ===")
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    print("=== Fim do Analisador Léxico ===\n")

    print("=== Início do Analisador Sintático ===")
    try:
        result = parser.parse(code, lexer=lexer)
        print("Análise Sintática bem-sucedida!")
    except Exception as e:
        print(f"Erro durante a análise sintática: {e}")
    print("=== Fim do Analisador Sintático ===")

if __name__ == "__main__":
    main()
