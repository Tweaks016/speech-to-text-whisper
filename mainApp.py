from flask import Flask, render_template, request, url_for, redirect, render_template_string
from flask_cors import CORS
from app import SpeechText
from pydub import AudioSegment
from whisper import load_model, transcribe
import torch, io, os

app = Flask(__name__)
app.secret_key = 'John The Ripper'
YOUTUBE_LINK = ''
VALID_INVALID_CHECK = False
AUDIO_FILE_PATH = ''
AUDIO_FILE_NAME_ = 'audioFileFromUser.mp3'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def currentTemp():
    if request.method == 'POST':
        # Check for valid input from user in link field or file input field 
        if not (request.form.get('linkToVideo') or request.files.get('file')):
            return redirect(url_for('home'))            
        else:
            if request.form.get('linkToVideo'):     # if user entered link 
                # checking whether the url given by the user is youtube video link or not
                YOUTUBE_LINK = request.form.get('linkToVideo')
                VALID_INVALID_CHECK = SpeechText.is_valid_youtube_url(YOUTUBE_LINK)
                # linkUrl = request.form['linkToVideo']
                if not VALID_INVALID_CHECK:
                    return redirect(url_for('home'))
                
                # Now let's download the youtube video from the link specified by the user
                AUDIO_FILE_PATH = SpeechText.youtubeVideoToAudioDownload(YOUTUBE_LINK)
                
            # speech conversion
            elif request.files.get('file'):         # if user uploaded an audio file
                
                wavFile = request.files['file']
                AUDIO_FILE_PATH = os.path.join(".\\audio_files", AUDIO_FILE_NAME_)
                filename = wavFile.filename        
                wavFile.save(AUDIO_FILE_PATH)
                
            try:
                lang = request.form.get('val')
                convertedText = SpeechText._TextFromSpeech(AUDIO_FILE_PATH, lang)
                if convertedText[0] != False:            
                    return redirect(url_for('home'))
                return render_template('index.html', convertedText=convertedText[1])        # Print the output 
            except Exception as e:
                pass
    return "Error"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
