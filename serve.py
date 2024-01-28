from flask import Flask, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # When a POST request is received, a new process to run stress_cpu.py is started
    subprocess.Popen(["python3", "submit_process.py"])
    return jsonify(message="CPU stress test initiated"), 202

@app.route('/', methods=['GET'])
def get_private_ip():
    # Returns the private IP address of the EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return jsonify(ip_address=private_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
