from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟一个内存中的数据存储
data_store = []

@app.route('/api/data', methods=['POST'])
def add_data():
    # 获取 POST 请求中的 JSON 数据
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"status": "error", "message": "Missing 'content' in request"}), 400
    
    # 添加数据到存储
    new_entry = {"id": len(data_store) + 1, "content": data['content']}
    data_store.append(new_entry)
    return jsonify({"status": "success", "data": new_entry}), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    # 返回所有数据
    return jsonify({"status": "success", "data": data_store})

if __name__ == '__main__':
    app.run(debug=True)