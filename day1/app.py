from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> This is ajay john </h1><br><p>Thank you for joining.. I hope you enjoyed it 2024, follow for more content around Devops.</p> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
