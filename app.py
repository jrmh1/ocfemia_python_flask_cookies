from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/getcookies')
def get_cookies():

    username = request.cookies.get('username')
    if username:
        return f"Cookie Value: {username}"
    else:
        return "No cookie found"


@app.route('/setcookies', methods=['POST'])
def set_cookies():

    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "No 'username' provided in the request"}), 400

    username = data['username']


    resp = make_response(f"Cookie has been set for username: {username}")


    resp.set_cookie('username', username)


    return resp


if __name__ == '__main__':
    app.run(debug=True)
