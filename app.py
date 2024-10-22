from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Vulnerable endpoint demonstrating path traversal
@app.route('/view-file', methods=['GET'])
def view_file():
    # Get the filename from the query parameter
    filename = request.args.get('filename')  # Unsafe input retrieval

    # Base directory (simulated safe directory)
    base_directory = 'files/'

    # Vulnerable: constructing the file path using user input
    file_path = os.path.join(base_directory, filename)  # Unsafe concatenation

    try:
        # Open and read the file content (vulnerable part)
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
