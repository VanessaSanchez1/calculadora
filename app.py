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
<<<<<<< HEAD
        operation = request.form.get('operacion', '')
=======
        operation = request.form['operation']
>>>>>>> main

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
<<<<<<< HEAD
            result = num1 / num2 if num2 != 0 else "Error: División por cero"
=======
            if num2 == 0:
                result = "Error: División por cero"
            else:
                result = num1 / num2
>>>>>>> main
        else:
            result = "Operación inválida"

        return render_template('index.html', result=result)
<<<<<<< HEAD

    except ValueError:
        return "Error: entrada inválida"

if __name__ == '__main__':
    app.run(debug=True)
=======
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
>>>>>>> main
