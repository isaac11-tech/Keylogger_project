from flask import Flask, render_template ,request, jsonify


app = Flask(__name__)

data = []

@app.route('/', methods=['POST'])
def receive_log():
    temp_data = request.get_json(silent=True)
    if not temp_data or 'message' not in temp_data:
        return jsonify({"error": "Invalid data"}), 400
    data.append(temp_data)
    print(f"Received log: {temp_data['message']}")
    return jsonify({"status": "success", "received": temp_data['message']}), 200

@app.route('/getData', methods=['GET'])
def get_data():
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)
