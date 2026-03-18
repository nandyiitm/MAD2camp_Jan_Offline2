from flask import Flask

app = Flask(__name__)

from routes import api
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)