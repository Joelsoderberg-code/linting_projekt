from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Enkel HTML-template för hemsidan
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .info {
            background-color: #e8f4fd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .api-link {
            display: inline-block;
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
        }
        .api-link:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Välkommen till min Flask-applikation!</h1>
        
        <div class="info">
            <h3>Om denna app:</h3>
            <p>Detta är en enkel Flask-applikation som visar hur man kan skapa en webbapplikation med Python.</p>
        </div>
        
        <h3>Testa API:et:</h3>
        <a href="/api/hello" class="api-link">Hälsning API</a>
        <a href="/api/data" class="api-link">Data API</a>
        
        <div class="info">
            <h3>Funktioner:</h3>
            <ul>
                <li>Hemsida med snygg design</li>
                <li>REST API endpoints</li>
                <li>JSON-svar</li>
                <li>Responsiv design</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Huvudsidan för applikationen"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/hello')
def hello_api():
    """API endpoint som returnerar en hälsning"""
    return jsonify({
        'message': 'Hej från Flask API!',
        'status': 'success',
        'language': 'svenska'
    })

@app.route('/api/data')
def data_api():
    """API endpoint som returnerar exempeldata"""
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Produkt A', 'price': 100},
            {'id': 2, 'name': 'Produkt B', 'price': 200},
            {'id': 3, 'name': 'Produkt C', 'price': 150}
        ],
        'total': 3,
        'status': 'success'
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Flask App',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("Startar Flask-applikationen...")
    print("Besök http://localhost:5000 för att se hemsidan")
    print("API endpoints:")
    print("  - http://localhost:5000/api/hello")
    print("  - http://localhost:5000/api/data")
    print("  - http://localhost:5000/health")
    app.run(debug=True, host='0.0.0.0', port=5000)
