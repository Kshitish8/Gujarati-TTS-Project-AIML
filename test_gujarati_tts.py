"""
Gujarati Text-to-Speech Converter
AI/ML Project - Converts Gujarati text to speech using Neural TTS (gTTS)
"""

import os
from gtts import gTTS

class GujaratiTTS:
    """Text-to-Speech converter specifically optimized for Gujarati language"""
    
    def __init__(self):
        self.language = 'gu' # 'gu' is the ISO code for Gujarati

    def text_to_speech(self, text, output_file="output.mp3"):
        """
        Convert Gujarati text to speech and save as an audio file.
        
        Args:
            text (str): Gujarati text to convert
            output_file (str): Path to save audio file (.mp3)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not text or not text.strip():
            print("[ERROR] Empty text provided")
            return False
            
        try:
            print(f"[TTS] Converting: {text[:40]}...")
            
            # Initialize gTTS with Gujarati language
            tts = gTTS(text=text, lang=self.language, slow=False)
            
            # Save the audio file
            tts.save(output_file)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                size_kb = os.path.getsize(output_file) / 1024
                print(f"[OK] Audio created successfully ({size_kb:.2f} KB)")
                return True
            else:
                return False

        except Exception as e:
            print(f"[ERROR] Conversion error: {str(e)}")
            return False

    def batch_convert(self, texts, output_dir="audio_files"):
        """Convert multiple Gujarati texts to speech"""
        results = {}
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        for i, text in enumerate(texts, 1):
            output_file = os.path.join(output_dir, f"gujarati_audio_{i}.mp3")
            success = self.text_to_speech(text, output_file=output_file)
            results[text] = success
            
        return results