from flask import Flask, request, jsonify
from model import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    result = translator.translate(text)
    return jsonify({"translation": result})

if __name__ == "__main__":
    app.run(debug=True)
