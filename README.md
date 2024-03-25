# Sentiment Analysis

This is a web application that analyses the sentiments and psychological insights about people conversing with each other. 

API Key: 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

## Folder structure

- `dialogue_analyzer/` contains the code to do with the openai API, input of txt files and mp3 files, the transcribing of audio and the uploading of the GPT output to the site.
- `media/` contains all the txt files and mp3 files used for my own tests. 
- `sentiment_analysis/` contains all the code to do with django.
- `manage.py` is the file that will be run in the terminal.


## Installing dependencies

I used 3 python packages in this assignment: `openai` (version 0.28), `django` and `requests`. These packages can be installed as follows from the CLI in your environment:

```
pip install openai==0.28
pip install django
pip install requests
```

## Usage Instructions

1) In the terminal type:

   `python3 manage.py runserver` or `python manage.py runserver`

2) The terminal should output something like this:
  
   `System check identified no issues (0 silenced).` \
   `March 24, 2024 - 23:16:48`\
   `Django version 5.0.3, using settings 'sentiment_analysis.settings`\
   `Starting development server at http://127.0.0.1:8000/`\
   `Quit the server with CONTROL-C.`

   Copy the server URL `http://127.0.0.1:8000/` into your browser.

3) Upload your relevant text or audio file and click 'Upload and Analyze'



## Difficulties:

The Explorer and Hero mode were not difficult. They took a couple of hours. However, I got stuck at Master mode due to an problem in my Google Cloud Server; when I tried to deploy the folder, I would always get this error:

                                                                                                                
`ERROR: (gcloud.app.deploy) Error Response: [13] Failed to create cloud build: invalid bucket "519972873954.cloudbuild-logs.googleusercontent.com";default Cloud Build service account or user-specified service account does not have access to the bucket`

I tried many things to solve it but was not able to due to time constraints. My part-time jobs and other job application assignment deadlines took up a lot of my time. My next steps would have have been to try AWS since it is more familiar to me.

