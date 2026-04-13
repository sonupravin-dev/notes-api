from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return "Notes API Running"

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    notes.append(data)
    return jsonify({"message": "Note added"})

@app.route('/notes/<int:index>', methods=['DELETE'])
def delete_note(index):
    notes.pop(index)
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run()
