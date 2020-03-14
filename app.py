from flask import Flask, jsonify, request
app = Flask(__name__)
from db import retrieve, insertPublicKey
from flask_swagger_ui import get_swaggerui_blueprint

@app.route("/api/publicKey", methods=['GET', 'POST'])
def example():
    if request.method == "GET":
        uid = request.args.get("uid")
        key = retrieve(uid)
        if not key:
            pass
        return jsonify({"uid": uid, "key" : key}) 
    if request.method == "POST":
        data = request.get_json()
        try : 
            uid = data.get("uid")
            key = data.get("key")
            return jsonify({"done" : insertPublicKey(uid, key)})
        except:
            return jsonify({"done" : -1})

SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Secure Chat Application"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


app.run(host='0.0.0.0', debug=True)