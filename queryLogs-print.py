from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    # Print the data received in the POST request
    print("Received POST request with the following data:")
    print(request.data.decode())  # Assuming the body is byte-encoded
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

