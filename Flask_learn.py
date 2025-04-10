from flask import Flask, jsonify, request

app = Flask(__name__)

# 示例数据
data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

@app.route('/get_age', methods=['GET'])
def get_age():
    name = request.args.get('name')

    if name in data_store:
        age = data_store[name]
        response_data = {
            "status": "success",
            "name": name,
            "age": age
        }
    else:
        response_data = {
            "status": "error",
            "message": "Name not found"
        }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
