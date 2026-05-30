from flask import Flask, render_template_string, request, make_response

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Calculator version1</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; margin: 0; }
        .calculator { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 300px; }
        h2 { text-align: center; color: #333; margin-top: 0; }
        input, select, button { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; font-size: 16px; }
        button { background-color: #007bff; color: white; border: none; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #0056b3; }
        .result { font-size: 18px; font-weight: bold; text-align: center; margin-top: 15px; color: #28a745; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Docker Calculator Version1</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" value="{{ num1 }}" placeholder="First Number" required>
            <select name="operation">
                <option value="add" {% if operation == 'add' %}selected{% endif %}>+</option>
                <option value="subtract" {% if operation == 'subtract' %}selected{% endif %}>-</option>
                <option value="multiply" {% if operation == 'multiply' %}selected{% endif %}>&times;</option>
                <option value="divide" {% if operation == 'divide' %}selected{% endif %}>&divide;</option>
            </select>
            <input type="number" step="any" name="num2" value="{{ num2 }}" placeholder="Second Number" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    num1 = ''
    num2 = ''
    operation = 'add'
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error (Div by 0)"
        except ValueError:
            result = "Invalid Input"
            
    # Explicitly forcing HTML response headers
    response = make_response(render_template_string(HTML_TEMPLATE, result=result, num1=num1, num2=num2, operation=operation))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5050))
app.run(host='0.0.0.0', port=port)