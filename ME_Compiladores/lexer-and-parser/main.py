from lexer import lexer  # Importa o lexer do arquivo lexer.py
from parser import parser  # Importa o parser do arquivo parser.py

def main():
    code = """
    for (hero; enemy - 3; treasure + 5) {
        attack
    }
    """

    print("=== Início do Analisador Léxico ===")
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token: {tok.type}, Valor: {tok.value}, Linha: {tok.lineno}, Posição: {tok.lexpos}")
    print("=== Fim do Analisador Léxico ===\n")

    print("=== Início do Analisador Sintático ===")
    try:
        result = parser.parse(code, lexer=lexer)
        print("Análise Sintática Finalizada!")
    except Exception as e:
        print(f"Erro durante a análise sintática: {e}")
    print("=== Fim do Analisador Sintático ===")

if __name__ == "__main__":
    main()
