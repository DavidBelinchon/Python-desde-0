from flask import Flask
from flask import jsonify

app = Flask(__name__, static_url_path='',static_folder='web')


@app.route('/')
def root():
    return app.send_static_file('index.html')



@app.route('/test/<path:path>', methods=['GET'])
def send_js(path):
    return "test al path "+path



@app.route('/getUser', methods=['GET'])
def getUser():
  jsonObject = [{

        "FirstName": "Code",
        "Lastname": "Handbook"
    }, {
        "FirstName": "Ravi",
        "Lastname": "Shanker"
    }, {
        "FirstName": "Salman",
        "Lastname": "Khan"
    }, {
        "FirstName": "Ali",
        "Lastname": "Zafar"
    }

];
  return jsonify(jsonObject)



if __name__ == "__main__":
    app.run()