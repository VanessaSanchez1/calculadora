from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operacion']
        
        if operation == 'sumar':
            result = num1 + num2
        elif operation == 'restar':
            result = num1 - num2
        elif operation == 'multiplicar':
            result = num1 * num2
        elif operation == 'dividir':
            result = num1 / num2 if num2 != 0 else "Error: Division x 0"
        else:
            result = "Invalid operation"
        
        return render_template('index.html', result=result)
    except ValueError:
        return "Error: Invalid input!"

if __name__ == '__main__':
    app.run(debug=True)