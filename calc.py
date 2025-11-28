import logging                                # Importa a biblioteca padrão para registrar logs (informações, avisos e erros).
from sympy import symbols, sympify, diff, integrate, limit, oo, SympifyError
                                              # Importa funções matemáticas simbólicas do SymPy para manipular expressões.


# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,                       # Define o nível mínimo de log a ser exibido (INFO mostra INFO, WARNING e ERROR).
    format="%(asctime)s [%(levelname)s] %(message)s"  
                                              # Define o formato da mensagem de log: data/hora, nível e mensagem.
)

class Calculadora():                          # Declaração da classe Calculadora.
    def __init__(self):                       # Método construtor da classe.
        self.f = None                         # Armazena a função simbólica inserida pelo usuário.
        self.x = symbols('x')                 # Cria a variável simbólica 'x' do SymPy.
        self.func_str = None                  # Armazena a string original da função digitada pelo usuário.

    def obter_funcao(self, func_str):         # Método para receber e converter a função do usuário.
        self.func_str = func_str              # Guarda a string da expressão na instância da classe.
        
        while True:                           # Loop até que a expressão seja válida.
            try:
                f = sympify(self.func_str)    # Converte a string em expressão simbólica do SymPy.
                self.f = f                    # Armazena a expressão simbólica internamente.
                x = self.x                    # Recupera a variável simbólica 'x'.

                if not f.has(x) and f.is_number:
                                              # Se a expressão não depende de x e é apenas um número:
                    logging.warning(f"A expressão '{f}' é apenas um número. Usando mesmo assim.")
                elif not f.has(x):            # Se não há dependência de x, mas não é número:
                    logging.warning(f"A variável 'x' não está na sua expressão: {f}")

                logging.info(f"Função inserida: f(x) = {f}")
                                              # Loga que a função foi interpretada com sucesso.

                return f, x                   # Retorna a função simbólica e o símbolo x.
                
            except SympifyError:              # Captura erro se a função tiver sintaxe inválida.
                logging.error("Função inválida. Tente novamente.")
                logging.info("Use sintaxe Python: ** para potência, * para multiplicação.")
                logging.info("Funções comuns: sin(x), cos(x), exp(x), log(x)")
            except Exception as e:            # Captura qualquer outro erro inesperado.
                logging.error(f"Ocorreu um erro inesperado: {e}")


    def calcular_derivada(self, f, x):        # Método para calcular derivadas.
        try:
            ordem_str = input("Qual a ordem da derivada? (padrão=1): ")
                                              # Pergunta a ordem da derivada ao usuário.
            ordem = int(ordem_str) if ordem_str.isdigit() else 1
                                              # Converte para inteiro ou usa 1 como padrão.
            
            derivada = diff(f, x, ordem)      # Calcula a derivada usando SymPy.

            logging.info("-" * 30)            # Linha separadora.
            logging.info(f"A derivada de ordem {ordem} de f(x) é:")
            logging.info(f"f'({x}) = {derivada}")
                                              # Mostra o resultado via log.
            
        except Exception as e:                # Captura erros no cálculo.
            logging.error(f"Erro ao calcular a derivada: {e}")


    def calcular_integral(self, f, x, tipo):  # Método para calcular integrais.
        if tipo == 'd':                       # Caso a integral seja definida:
            try:
                a_str = input("Limite inferior (a) (use 'oo' para infinito): ")
                                              # Lê limite inferior.
                b_str = input("Limite superior (b) (use 'oo' para infinito): ")
                                              # Lê limite superior.
                
                a = sympify(a_str)            # Converte o limite inferior.
                b = sympify(b_str)            # Converte o limite superior.
                
                integral_def = integrate(f, (x, a, b))
                                              # Calcula a integral definida.

                logging.info("-" * 30)        # Linha separadora.
                logging.info(f"A integral definida de {a} até {b} é:")
                logging.info(f"Resultado: {integral_def}")
                
            except Exception as e:            # Captura qualquer erro.
                logging.error(f"Erro ao calcular integral definida: {e}")

        else:                                 # Caso seja integral indefinida:
            try:
                integral_indef = integrate(f, x)
                                              # Calcula a integral indefinida.

                logging.info("-" * 30)
                logging.info("A integral indefinida de f(x) é:")
                logging.info(f"Resultado: {integral_indef} + C")
                                              # Adiciona constante de integração.
                
            except Exception as e:            # Captura erros no processo.
                logging.error(f"Erro ao calcular integral indefinida: {e}")


    def calcular_limite(self, f, x):          # Método para calcular limites.
        try:
            ponto_str = input("Calcular limite quando x tende a (ex: 0, 2, oo): ")
                                              # Usuário define ponto de aproximação.
            ponto = sympify(ponto_str)        # Converte o ponto para formato simbólico.
            
            direcao = input("Lado? '+' (direita), '-' (esquerda) ou 'ambos' [padrão=ambos]: ")
                                              # Usuário escolhe direção do limite unilateral.

            if direcao == '+':                # Limite pela direita.
                lim = limit(f, x, ponto, dir='+')
            elif direcao == '-':              # Limite pela esquerda.
                lim = limit(f, x, ponto, dir='-')
            else:                             
                lim = limit(f, x, ponto)      # Limite bilateral (ambos os lados).
                
            logging.info("-" * 30)
            logging.info(f"O limite de f(x) quando x -> {ponto} é:")
            logging.info(f"Resultado: {lim}")  # Mostra o resultado.
            
        except Exception as e:                # Captura erros no cálculo.
            logging.error(f"Erro ao calcular o limite: {e}")
