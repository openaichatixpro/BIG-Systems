import os
import time
import argparse
import threading
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/api/models')
def list_models():
    try:
        ollama_host = os.environ.get('OLLAMA_HOST', 'http://ollama:11434')
        response = requests.get(f"{ollama_host}/api/tags")
        if response.status_code == 200:
            models = [model['name'] for model in response.json().get('models', [])]
            return jsonify({"models": models})
        return jsonify({"models": [], "error": f"Ollama returned {response.status_code}"})
    except Exception as e:
        return jsonify({"models": [], "error": str(e)})


def watch_folder_loop(watch_folder, output_folder, batch_size):
    # Minimal placeholder loop: scans folder every 5s and writes a heartbeat file
    os.makedirs(output_folder, exist_ok=True)
    while True:
        # This is a placeholder for your real processing logic
        heartbeat = os.path.join(output_folder, 'last_scan.txt')
        with open(heartbeat, 'w', encoding='utf-8') as f:
            f.write(f'last_scan:{time.time()}\n')
        time.sleep(5)


def run_server(host='0.0.0.0', port=3001):
    app.run(host=host, port=port)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--watch-folder', default=os.environ.get('WATCH_FOLDER', '/data'))
    parser.add_argument('--output', default=os.environ.get('OUTPUT_FOLDER', '/output'))
    parser.add_argument('--batch-size', type=int, default=int(os.environ.get('BATCH_SIZE', '50000')))
    args = parser.parse_args()

    watch_thread = threading.Thread(target=watch_folder_loop, args=(args.watch_folder, args.output, args.batch_size), daemon=True)
    watch_thread.start()

    # Start Flask server (will block)
    run_server()


if __name__ == '__main__':
    main()
