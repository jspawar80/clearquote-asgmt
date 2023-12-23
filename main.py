from flask import Flask, request, jsonify

app = Flask(__name__)

#  /healthcheck: returns "Healthy" with code 200.
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return "Healthy", 200


# /gcd: accepts a JSON with 2 keys x and y. Returns the GCD of the two numbers.
@app.route('/gcd', methods=['POST'])
def gcd():
    gcdData = request.get_json()
    x = gcdData['x']
    y = gcdData['y']
    return jsonify({"gcd": get_gcd(x, y)})

def get_gcd(x, y):
    while(y):
      x, y = y, x % y
    return x

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
