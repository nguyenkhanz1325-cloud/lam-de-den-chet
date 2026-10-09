from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='.')
DATA_FILE = 'data.json'

# Khởi tạo data rỗng nếu file chưa tồn tại
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"photo": "", "exams": []}, f)

@app.route('/')
def index():
    # Trả về giao diện web
    return send_from_directory('.', 'index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Gửi dữ liệu đề thi xuống frontend
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/api/save', methods=['POST'])
def save_data():
    # Nhận dữ liệu từ frontend và lưu vào file
    data = request.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)