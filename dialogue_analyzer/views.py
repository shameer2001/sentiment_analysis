import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import process_dialogue_file, transcribe_audio
from django.http import HttpResponse

def upload_dialogue(request):
    if request.method == 'POST' and request.FILES['dialogue']:
        dialogue_file = request.FILES['dialogue']
        fs = FileSystemStorage()
        filename = fs.save(dialogue_file.name, dialogue_file)
        uploaded_file_path = fs.path(filename)


        if str(dialogue_file.name).endswith('.txt'):
            insights = process_dialogue_file(uploaded_file_path)
        
        else:  # Assuming it's an audio file for simplicity
            deepgram_api_key = 'd838f9987d5137232037594bb3a08172a6938c95'
            transcript = transcribe_audio(uploaded_file_path, deepgram_api_key)
            insights = process_dialogue_file(transcript, is_text=True)

        return render(request, 'dialogue_analyzer/upload_dialogue.html', {
            'insights': insights
        })

    return render(request, 'dialogue_analyzer/upload_dialogue.html')
