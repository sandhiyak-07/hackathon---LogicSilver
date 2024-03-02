import openai
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

your_openai_key = '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'
your_text = 'please help me to write python code!'
client = openai.OpenAI(api_key=your_openai_key)

@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/convert_text_to_speech', methods=['POST'])
def convert_text_to_speech():
    try:
        data = request.json
        text = data['text']

    
        response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
)
        try:
            os.remove('speech.mp3')
        except FileNotFoundError:
            print("File not found")

        # Write the response content to a file
        with open('speech.mp3', 'wb') as f:
            f.write(response.content)

        return jsonify({'success': True}), 200
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': 'An error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
