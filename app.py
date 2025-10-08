import time
import sympy
from flask import Flask, request, jsonify, render_template

# --- LÓGICA DO SERVIDOR WEB ---
app = Flask(__name__)

# Rota principal que exibe o front-end (o arquivo index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota que recebe os dados do front-end, calcula e devolve os resultados
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()

    # Extrai os dados recebidos do front-end
    func_str = data['funcao']
    var_str = data['variavel']
    tol = float(data['tol'])
    max_iter = int(data['max_iter'])
    a = float(data['a'])
    b = float(data['b'])
    x0_newton = float(data['x0_newton'])
    x0_secante = float(data['x0_secante'])
    x1_secante = float(data['x1_secante'])

    try:
        # Usa SymPy para criar as funções a partir da string
        variavel = sympy.symbols(var_str)
        expr = sympy.sympify(func_str)
        deriv_expr = sympy.diff(expr, variavel)
        
        f = sympy.lambdify(variavel, expr, 'math')
        df = sympy.lambdify(variavel, deriv_expr, 'math')

        # Executa todos os métodos
        res_b = bisseccao(f, a, b, tol, max_iter)
        res_fp = falsa_posicao(f, a, b, tol, max_iter)
        res_nr = newton_raphson(f, df, x0_newton, tol, max_iter)
        res_s = secante(f, x0_secante, x1_secante, tol, max_iter)
        
        resultados = {
            "Bissecção": res_b,
            "Falsa Posição": res_fp,
            "Newton-Raphson": res_nr,
            "Secante": res_s
        }
        
        return jsonify(resultados)

    except Exception as e:
        return jsonify({"erro": f"Erro no cálculo: {str(e)}"}), 400


# --- MÉTODOS NUMÉRICOS ---
def bisseccao(f, a, b, tol, max_iter):
    iteracoes = 0
    start_time = time.time()
    if f(a) * f(b) >= 0:
        return {"erro": "f(a) * f(b) >= 0"}
    
    raiz = (a + b) / 2
    while (b - a) / 2 > tol and iteracoes < max_iter:
        if f(raiz) == 0: break
        elif f(a) * f(raiz) < 0: b = raiz
        else: a = raiz
        raiz = (a + b) / 2
        iteracoes += 1
    
    tempo_execucao = (time.time() - start_time) * 1000
    precisao = abs(f(raiz))
    return {"raiz": raiz, "iteracoes": iteracoes, "tempo": tempo_execucao, "precisao": precisao}

def falsa_posicao(f, a, b, tol, max_iter):
    iteracoes = 0
    start_time = time.time()
    if f(a) * f(b) >= 0:
        return {"erro": "f(a) * f(b) >= 0"}
    
    x_anterior = float('inf')
    x_novo = (a * f(b) - b * f(a)) / (f(b) - f(a))
    while abs(x_novo - x_anterior) > tol and iteracoes < max_iter:
        if f(a) * f(x_novo) < 0: b = x_novo
        else: a = x_novo
        x_anterior = x_novo
        x_novo = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iteracoes += 1
        
    tempo_execucao = (time.time() - start_time) * 1000
    precisao = abs(f(x_novo))
    return {"raiz": x_novo, "iteracoes": iteracoes, "tempo": tempo_execucao, "precisao": precisao}


def newton_raphson(f, df, x0, tol, max_iter):
    iteracoes = 0
    start_time = time.time()
    x = x0
    for i in range(max_iter):
        dfx = df(x)
        if abs(dfx) < 1e-12:
            return {"erro": "Derivada próxima de zero"}
        x_novo = x - f(x) / dfx
        if abs(x_novo - x) < tol: break
        x = x_novo
        iteracoes += 1

    tempo_execucao = (time.time() - start_time) * 1000
    precisao = abs(f(x))
    return {"raiz": x, "iteracoes": iteracoes, "tempo": tempo_execucao, "precisao": precisao}

def secante(f, x0, x1, tol, max_iter):
    iteracoes = 0
    start_time = time.time()
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-12:
            return {"erro": "Diferença f(x1)-f(x0) próxima de zero"}
        x_novo = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x_novo - x1) < tol: break
        x0, x1 = x1, x_novo
        iteracoes += 1
    
    tempo_execucao = (time.time() - start_time) * 1000
    precisao = abs(f(x_novo))
    return {"raiz": x_novo, "iteracoes": iteracoes, "tempo": tempo_execucao, "precisao": precisao}


# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)

    