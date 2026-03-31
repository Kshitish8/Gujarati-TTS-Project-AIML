# Gujarati Text-to-Speech (TTS) Converter

## Project Overview

This is an AI/ML project that converts Gujarati text into natural-sounding speech. It uses the `pyttsx3` library, which is a cross-platform text-to-speech library that works offline without requiring API keys.

## Features

✅ **Gujarati Language Support** - Converts Gujarati text to speech  
✅ **Offline Processing** - No internet required  
✅ **Batch Processing** - Convert multiple texts  
✅ **Audio Export** - Save speech as audio files (.wav, .mp3)  
✅ **Adjustable Speed & Volume** - Configurable speech parameters  
✅ **Interactive CLI** - User-friendly command-line interface

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Verify Installation

If you encounter issues with `pyaudio`, try:

```bash
# On Windows
pip install pipwin
pipwin install pyaudio

# On macOS
brew install portaudio
pip install pyaudio

# On Linux
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## Usage

### Basic Usage - Interactive Mode

```bash
python gujarati_tts.py
```

### Programmatic Usage

```python
from gujarati_tts import GujaratiTTS

# Initialize
tts = GujaratiTTS()

# Convert single text
gujarati_text = "નમસ્તે, આ એક ટેક્સ્ટ ટુ સ્પીચ પ્રોજેક્ટ છે।"
tts.text_to_speech(gujarati_text, output_file="output.wav")

# Batch process
texts = ["ટેક્સ્ટ એક", "ટેક્સ્ટ બે", "ટેક્સ્ટ ત્રણ"]
results = tts.batch_convert(texts, output_dir="./audio_files")
```

## Project Structure

```
aiml project/
├── gujarati_tts.py          # Main TTS converter class
├── test_gujarati_tts.py     # Unit tests
├── web_interface.py         # Streamlit web app
├── requirements.txt         # Python dependencies
└── README.md               # Documentation
```

## Example Gujarati Texts

- "નમસ્તે" - Hello
- "આર્ટિફિશિયલ ઇંટેલિજન્સ" - Artificial Intelligence
- "ગુજરાતી" - Gujarati
- "કૃત્રિમ બુદ્ધિમત્તા" - Artificial Intelligence

## How It Works

1. **Text Input**: Accepts Gujarati Unicode text
2. **TTS Engine**: pyttsx3 engine converts text to phonetic representation
3. **Speech Synthesis**: Engine generates audio from phonetics
4. **Output**: Audio played directly or saved to file

## Technologies Used

- **pyttsx3**: Offline text-to-speech library
- **Python 3.8+**: Programming language
- **Streamlit** (optional): For web interface

## Limitations & Notes

- Speech quality depends on system TTS voices available
- Some complex Gujarati diacritics may need special handling
- Requires portaudio libraries for audio input/output on some systems

## Future Enhancements

- [ ] Add neural network-based TTS (Google/Azure API)
- [ ] Support for phonetic adjustments
- [ ] Real-time speech recognition integration
- [ ] Web-based interface with more features
- [ ] Audio quality improvements

## Author

AI/ML Subject - Text-to-Speech Project

## License

Educational Use Only
