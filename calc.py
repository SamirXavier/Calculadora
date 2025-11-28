from sympy import symbols, sympify, diff, integrate, limit, oo, SympifyError


class Calculadora():
    def __init__(self):
        pass

    def obter_funcao(self, func_str):
        x = symbols('x')
        self.func_str = func_str
        while True:
            
            
            try:
                f = sympify(self.func_str)

                if not f.has(x) and f.is_number:
                    print(f"A expressão '{f}' é apenas um número. Vamos usá-la mesmo assim.")
                elif not f.has(x):
                    print(f"Aviso: A variável 'x' não está na sua expressão: {f}")

                print(f"Função inserida: f(x) = {f}")
                return f, x
                
            except SympifyError:
                print("Erro: Função inválida. Tente novamente.")
                print("Use sintaxe Python: ** para potência, * para multiplicação.")
                print("Funções comuns: sin(x), cos(x), exp(x), log(x)")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")


    def calcular_derivada(self,f, x):
        try:
            ordem_str = input("Qual a ordem da derivada? (padrão=1): ")
            ordem = int(ordem_str) if ordem_str.isdigit() else 1
            
            derivada = diff(f, x, ordem)
            print("-" * 30)
            print(f"A derivada de ordem {ordem} de f(x) é:")
            print(f"f'({x}) = {derivada}")
            
        except Exception as e:
            print(f"Erro ao calcular a derivada: {e}")

    def calcular_integral(self,f, x):
        tipo = input("Integral 'Definida' (d) ou 'Indefinida' (i)? [padrão=i]: ").lower()
        
        if tipo == 'd':
            try:
                a_str = input("Limite inferior (a) (use 'oo' para infinito): ")
                b_str = input("Limite superior (b) (use 'oo' para infinito): ")
                
                a = sympify(a_str)
                b = sympify(b_str)
                
                integral_def = integrate(f, (x, a, b))
                print("-" * 30)
                print(f"A integral definida de {a} até {b} é:")
                print(f"Resultado: {integral_def}")
                
            except Exception as e:
                print(f"Erro ao calcular integral definida: {e}")
        else:
            try:
                integral_indef = integrate(f, x)
                print("-" * 30)
                print("A integral indefinida de f(x) é:")
                print(f"Resultado: {integral_indef} + C")
                
            except Exception as e:
                print(f"Erro ao calcular integral indefinida: {e}")

    def calcular_limite(f, x):
        try:
            ponto_str = input("Calcular limite quando x tende a (ex: 0, 2, oo): ")
            ponto = sympify(ponto_str)
            
            direcao = input("Lado? '+' (direita), '-' (esquerda) ou 'ambos' [padrão=ambos]: ")
            
            if direcao == '+':
                lim = limit(f, x, ponto, dir='+')
            elif direcao == '-':
                lim = limit(f, x, ponto, dir='-')
            else:
                lim = limit(f, x, ponto)
                
            print("-" * 30)
            print(f"O limite de f(x) quando x -> {ponto} é:")
            print(f"Resultado: {lim}")

        except Exception as e:
            print(f"Erro ao calcular o limite: {e}")
