from pytube import YouTube
from googletrans import Translator
from whisper import load_model, transcribe
import re, torch, io, os

BASE_FILE_DIR = '.\\file_store'

# Check for valid youtube url
def is_valid_youtube_url(url):    
    pattern = re.compile(r'^https?://(?:www\.)?(?:youtube\.com|youtu\.be)/(?:watch\?v=)?([a-zA-Z0-9_-]{11})$')
    return bool(pattern.match(url))

# function to download youtube video in mp3 format for link provided
def youtubeVideoToAudioDownload(link):
    audio_file_path = ''
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_audio_only()
        audio_file_path = youtubeObject.download(filename='.\\audio_files\\ConvertSpeechFromYoutubeLink.mp3')
        return audio_file_path
    except (Exception, KeyError, AttributeError):
        youtubeObject = YouTube(link)
        audio_file_path = youtubeObject.download(filename='.\\audio_files\\ConvertSpeechFromYoutubeLink.mp3')
        youtubeObject = youtubeObject.streams.get_audio_only()
        print("An error has occurred")
    print("Download is completed successfully")

'''
Text Conversion from english speech to text.....
'''
def transcribeAudio(audio_file):
    
    CURRENT_LANG = ''
    STORE_FILE = os.path.join(BASE_FILE_DIR, 'TranscriptContent.txt')
    TRANSCRIPT_TEXT = ''
    WHISPER_MODEL_USED = 'base'     # Specify model to be used
    
    # Device 
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Transcription process
    model = load_model(WHISPER_MODEL_USED, device=device)
    transciption = transcribe(model, audio_file)
    CURRENT_LANG = transciption['language']
    
    # Saving the transciption to a text file
    with io.open(STORE_FILE, 'w', encoding='utf-8') as file1:
        file1.write(transciption['text'])
    
    return STORE_FILE, CURRENT_LANG

# Translation 
def translateAudio(current_lang, to_lang, file_location):
    
    TRANSCRIPT_TEXT = ''
    CURRENT_LANG = current_lang
    TO_LANG = to_lang
    STORE_TRANSLATED_FILE = os.path.join(BASE_FILE_DIR, 'TranslatedContent.txt')
    
    # Reading the file
    with io.open(file_location, 'r', encoding='utf-8') as file2:
        TRANSCRIPT_TEXT = file2.read()
    
    # Translating the text
    translator = Translator()
    text_translate = translator.translate(TRANSCRIPT_TEXT, src=CURRENT_LANG, dest=TO_LANG)
    
    # Storing translated text
    with io.open(STORE_TRANSLATED_FILE, 'w', encoding='utf-8') as file3:
        file3.write(text_translate.text)
    
    return STORE_TRANSLATED_FILE

def _TextFromSpeech(audio_file,lang=None):
    # variables required
    FILE_LOCATION_ = ''
    TRANSLATED_TEXT_FILE = ''
    text_generated = ''
    
    try:
        # Transcribe 
        file_loc, c_lang = transcribeAudio(audio_file)
        FILE_LOCATION_ = file_loc
        
        if lang != 'defaultIfNoValSelected':        # Translate         
            # for any language if selected
            C_LANG = c_lang         # Current language
            T_LANGUAGE = lang       # To language
            TRANSLATED_TEXT_FILE = translateAudio(C_LANG, T_LANGUAGE, FILE_LOCATION_)
            
            # location to file stored
            with io.open(TRANSLATED_TEXT_FILE, 'r', encoding='utf-8') as file5:
                text_generated = file5.read()
        else:       # Output the transcribed text
            # storing text to a variable
            with io.open(FILE_LOCATION_, 'r', encoding='utf-8') as file4:
                text_generated = file4.read()
        # return the output
        return False, text_generated
                
    except Exception as er:
        # print(f"[-] Error Occured: {er}")
        pass
