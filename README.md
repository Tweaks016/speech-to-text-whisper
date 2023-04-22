# Flask Speech Recognition with Whisper AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Flask: 2.2.3](https://img.shields.io/badge/flask-2.2.3-green.svg)](https://flask.palletsprojects.com/en/2.0.x/)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-%23d15b20)](https://github.com/openai/whisper)

This is a simple Flask app that uses Whisper AI to transcribe speech from audio files and youtube videos. This project demonstrates how to build a simple speech recognition application using Flask and the Whisper AI library. It uses the base Whisper AI model by default, but you can specify a different model if you prefer. The application can transcribe youtube videos  and save the resulting transcript to a text file.

## Installation

1. Clone this repository: `git clone https://github.com/your-username/your-repo.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the app: `python mainApp.py`
4. Navigate to `http://localhost:5000` in your web browser.

## Usage

1. Upload an audio file to the app or specify the youtube video link.
2. Wait for the transcription to complete.
3. View the transcription result in the browser.
4. Optionally, translate the transcription to a different language using the dropdown menu.

## File Structure

```bash
├── SPEECH-TO-TEXT-WHISPER
│   ├── requirements.txt
│   ├── mainApp.py
│   └── LICENSE
├── app
│   ├── SpeechText.py
│   └───__pycache__
├── audio_file
├── file_store
├── static
├── templates
└── ├── index.html
```

## Configuration

By default, the app runs on port 5000. You can change this by modifying the `PORT` variable in `mainApp.py`.

You can also specify the model used by Whisper AI by modifying the `WHISPER_MODEL_USED` variable in `mainApp.py`. By default, the base model is used.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

