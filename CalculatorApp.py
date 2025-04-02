from flask import Flask, request, jsonify

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return {"error": "Division by zero is not allowed"}, 400
    return x / y

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Validate if required fields exist
    if not data or 'operation' not in data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Missing required parameters"}), 400

    # Validate numeric input
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({"error": "num1 and num2 must be numbers"}), 400

    operation = data['operation'].lower()

    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        return jsonify({"error": "Invalid operation"}), 400

    result = operations[operation](num1, num2)
    
    # If the function returned an error response (tuple)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
