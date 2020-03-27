from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '你好，世界！'
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
