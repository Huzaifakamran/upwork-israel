from openai import OpenAI
from flask import Flask, request, jsonify
import hashlib
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/transcription', methods=['POST'])
def get_transcription():
    try:
        user_speech = request.data.decode('utf-8')
        print(user_speech)
        
        is_condition_met = chatgpt_response(user_speech)
        return jsonify({'result': is_condition_met}),200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'result': False, 'error': str(e)}),400

def chatgpt_response(user_speech):
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. You need to understand the user message and response in just Trur or False. So if user residing in Blunestconnect community then return True and if they want to learn about the community then return False."},
        {"role": "user", "content": user_speech}
    ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)


