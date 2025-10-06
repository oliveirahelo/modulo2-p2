from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# definindo uma rota

@app.route('/')
def home():
    return f'seja bem vindo ao sistema'

# calculadora
@app.route('/soma/valor1=5/valor2=6')
def soma(n1,n2):
    return f'somando valores{n1} e {n2} ={n1 + n2}'


@app.route('/subtrair/valor1=5/valor2=6')
def subtração(n1,n2):
    return f'subtrindo valores{n1} e {n2} ={n1 - n2}'

@app.route('/multiplicar/valor1=5/valor2=6')
def multiplicação(n1,n2):
    return f'mutiplicando valores{n1} e {n2} ={n1 * n2}'

@app.route('/dividir/valor1=5/valor2=6')
def divisão(n1,n2):
    if n2 == 0:
     return f'invalido'
    else:
     return f'dividindo valores{n1} e {n2} ={n1 / n2}'
    

if __name__ == "__main__":
    app.run(depurar=True)

   