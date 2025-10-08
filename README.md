# Projeto_Calculo_Numerico - Simulador Comparativo de Métodos Numéricos

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.2%2B-black?logo=flask)
![SymPy](https://img.shields.io/badge/SymPy-1.12-green)

## 📖 Sobre o Projeto

Este projeto é um **Simulador Comparativo de Métodos Numéricos** desenvolvido como parte da avaliação da Unidade 1 da disciplina de Cálculo Numérico, da **Fundação Universidade Federal do Vale do São Francisco (UNIVASF)**.

O objetivo principal é aplicar e analisar a eficiência de quatro métodos iterativos para encontrar zeros de funções algébricas e transcendentes. A aplicação foi desenvolvida com uma interface web interativa para facilitar a entrada de dados e a visualização clara dos resultados.

## ✨ Funcionalidades

* **Implementação de 4 Métodos Numéricos:**
    * Bissecção 
    * Falsa Posição 
    * Newton-Raphson 
    * Secante 
* **Interface Web Interativa:** Front-end desenvolvido com HTML/CSS/JS e conectado a um back-end Python com Flask.
* **Entrada de Funções Dinâmicas:** O usuário pode inserir qualquer função matemática como uma string (ex: `10*exp(-0.5*t)*cos(2*t) - 5`). 
* **Cálculo Automático de Derivadas:** Utilizando a biblioteca SymPy, a derivada da função inserida é calculada automaticamente para uso no método de Newton-Raphson.
* **Tabela Comparativa de Resultados:** Ao final do cálculo, é exibida uma tabela clara comparando cada método em termos de:
    * Raiz encontrada 
    * Número de iterações realizadas 
    * Tempo de execução em milissegundos 
    * Precisão final alcançada (`|f(raiz)|`) 

## 🚀 Tecnologias Utilizadas

* **Back-end:** Python
* **Servidor Web:** Flask
* **Cálculo Simbólico:** SymPy
* **Front-end:** HTML, CSS, JavaScript

## 🔧 Instalação e Configuração

Siga os passos abaixo para executar o projeto em sua máquina local.

1.  **Clone o repositório:**
    ```bash
    git clone [[https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)](https://github.com/joao-vitor01/Projeto_Calculo_Numerico.git)
    cd nome-do-repositorio
    ```

3.  **Instale as dependências:**
    O projeto utiliza as bibliotecas Flask e SymPy. Para facilitar a instalação, crie um arquivo `requirements.txt` com o seguinte conteúdo:
    ```
    Flask
    sympy
    ```
    Em seguida, instale a partir deste arquivo:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Como Executar

1.  Com o ambiente virtual ativado e as dependências instaladas, execute o servidor Flask:
    ```bash
    python app.py
    ```

2.  Abra seu navegador de internet e acesse o seguinte endereço:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
