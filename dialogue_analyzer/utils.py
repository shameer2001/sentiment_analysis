import openai

def process_dialogue_file(content, is_text=False):
    openai.api_key = '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'
    
    # Check if the input is text or a file path
    dialogue = content if is_text else open(content, 'r').read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Analyze the following dialogue and provide insights about the speakers' characteristics and sentiments: For example: ‘[Speaker_2] likes a sport. It seems he cares about his health, [Speaker_1] pretends to be smart’.\n"},
            {"role": "user", "content": dialogue}
        ]
    )

    return response['choices'][0]['message']['content'].strip().split('\n')


import requests

def transcribe_audio(file_path, deepgram_api_key):
    with open(file_path, 'rb') as audio_file:
        response = requests.post(
            'https://api.deepgram.com/v1/listen',
            headers={'Authorization': f'Token {deepgram_api_key}'},
            files={'file': audio_file},
        )
        response_data = response.json()

        transcript = response_data.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')
        return transcript
