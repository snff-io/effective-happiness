from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/<string:username>/', methods=['GET'])
def (username):
    """
    This is a simple API
    Call this api passing a username and get back its full name
    ---
    parameters:
      - name: username
        in: path
        type: string
        required: true
    responses:
      200:
        description: The full name of the user
    """
    return jsonify({'username': username, 'fullname': 'User Name'})

if __name__ == "__main__":
    app.run(debug=True)