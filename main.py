from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado = None
        promedio = None
        error = None

        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        notas_validas = (10 <= nota1 <= 70) and (10 <= nota2 <= 70) and (10 <= nota3 <= 70)
        asistencia_valida = (0 <= asistencia <= 100)
        if not notas_validas or not asistencia_valida:
            error = "Número no válido: las notas deben estar entre 10 y 70, y la asistencia entre 0% y 100%"
            return render_template('ejercicio1.html', error=error)

        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            resultado = 'APROBADO'
        else:
            resultado = 'REPROBADO'
        return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        resultado = None
        nombre_mas_largo = None

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        largo_nombre1 = len(nombre1.replace(" ", ""))
        largo_nombre2 = len(nombre2.replace(" ", ""))
        largo_nombre3 = len(nombre3.replace(" ", ""))
        if largo_nombre1 > largo_nombre2 or largo_nombre1 > largo_nombre3:
            nombre_mas_largo = nombre1
            resultado = largo_nombre1
        elif largo_nombre2 > largo_nombre1 or largo_nombre2 > largo_nombre3:
            nombre_mas_largo = nombre2
            resultado = largo_nombre2
        else:
            nombre_mas_largo = nombre3
            resultado = largo_nombre3
        return render_template('ejercicio2.html', resultado=resultado, nombre_mas_largo=nombre_mas_largo)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)