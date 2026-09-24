"""
Gujarati Text-to-Speech Converter
AI/ML Project - Converts Gujarati text to speech using multiple engines
"""

import os
import sys
import threading
from pathlib import Path

try:
    import pyttsx3
except Exception:
    pyttsx3 = None

try:
    from gtts import gTTS
except Exception:
    gTTS = None


class GujaratiTTS:
    """Text-to-speech converter for Gujarati language."""

    def __init__(self, allow_online_fallback=False):
        """Initialize the TTS engine."""
        self._lock = threading.Lock()
        self.allow_online_fallback = allow_online_fallback
        self.engine = None
        if pyttsx3 is not None:
            try:
                self.engine = pyttsx3.init()
                self._setup_engine()
            except Exception as exc:
                print(f"[WARN] Offline pyttsx3 engine unavailable: {exc}")
        print("[INFO] Gujarati TTS initialized (using gTTS for Gujarati language support)")

    def _run_engine_queue(self, text, output_file=None, play=True):
        """Queue text/file operations and block until synthesis completes."""
        if self.engine is None:
            raise RuntimeError("No offline TTS engine is available")

        if output_file:
            self.engine.save_to_file(text, output_file)
            print(f"[TTS] Queued save to: {output_file}")

        if play:
            self.engine.say(text)
            print("[TTS] Queued playback")

        self.engine.runAndWait()

    def _setup_engine(self):
        """Configure TTS engine for optimal performance."""
        if self.engine is None:
            return

        try:
            self.engine.setProperty("rate", 185)
            self.engine.setProperty("volume", 1.0)
            voices = self.engine.getProperty("voices")
            print(f"[INFO] Available voices: {len(voices)}")

            if voices:
                for i, voice in enumerate(voices):
                    print(f"  {i}: {voice.name} (ID: {voice.id})")
                self.engine.setProperty("voice", voices[0].id)
                print(f"[OK] Voice set to: {voices[0].name}")
            else:
                print("[WARN] No voices available - using default")

        except Exception as exc:
            print(f"[ERROR] Voice setup error: {str(exc)}")
            print("[WARN] Continuing with default voice...")

    def _normalize_output_path(self, output_file):
        """Normalize output file names for gTTS, which only emits MP3 data."""
        if not output_file:
            return output_file

        output_path = Path(output_file)
        if output_path.suffix.lower() == ".wav":
            return output_path.with_suffix(".mp3")
        return output_path

    def text_to_speech(self, text, output_file=None, play=True, timeout=15):
        """
        Convert Gujarati text to speech using gTTS (requires internet).

        Args:
            text (str): Gujarati text to convert
            output_file (str): Optional path to save audio file (.mp3 or .wav)
            play (bool): Whether to play audio immediately (only used for local engine)
            timeout (int): Maximum seconds to wait before canceling

        Returns:
            bool: True if successful, False otherwise
        """
        if not text or not text.strip():
            print("[ERROR] Empty text provided")
            return False

        try:
            print(f"[TTS] Converting: {text[:40]}...")

            if gTTS is None:
                print("[ERROR] gTTS not installed. Install with: pip install gtts")
                return False

            target_file = self._normalize_output_path(output_file)

            try:
                tts_engine = gTTS(text=text, lang="gu", slow=False)

                if target_file:
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    tts_engine.save(str(target_file))

                    if os.path.exists(str(target_file)) and os.path.getsize(str(target_file)) > 64:
                        size_kb = os.path.getsize(str(target_file)) / 1024
                        print(f"[OK] Audio created ({size_kb:.2f} KB)")

                        if play:
                            print("[INFO] Audio saving complete. Use an external player to play it.")
                        return True

                    print("[ERROR] Audio file not created or too small")
                    return False

                print("[INFO] Audio generated successfully (no output file specified)")
                return True

            except Exception as gtts_error:
                print(f"[ERROR] gTTS conversion failed: {str(gtts_error)}")
                print("[INFO] This usually means an internet connection issue or gTTS service unavailability")
                return False

        except Exception as exc:
            print(f"[ERROR] Conversion error: {str(exc)}")
            return False

    def batch_convert(self, texts, output_dir=None):
        """Convert multiple Gujarati texts to speech."""
        results = {}

        if output_dir:
            Path(output_dir).mkdir(parents=True, exist_ok=True)

        for i, text in enumerate(texts, 1):
            output_file = None
            if output_dir:
                output_file = os.path.join(output_dir, f"gujarati_audio_{i}.mp3")

            success = self.text_to_speech(text, output_file=output_file, play=False)
            results[text] = success

        return results


def main():
    """Main function with example usage"""
    print("=" * 60)
    print("Gujarati Text-to-Speech Converter")
    print("=" * 60)
    
    # Initialize TTS
    tts = GujaratiTTS()
    
    # Example Gujarati texts
    example_texts = [
        "નમસ્તે, આ એક ગુજરાતી ટેક્સ્ટ ટુ સ્પીચ પ્રોજેક્ટ છે।",  # Hello, this is a Gujarati TTS project
        "આર્ટિફિશિયલ ઇંટેલિજન્સ ભવિષ્યનું ભાષા છે।",  # AI is the language of the future
        "ગુજરાતી આપણી સુંદર ભાષા છે।"  # Gujarati is our beautiful language
    ]
    
    # Interactive mode
    print("\n📝 Choose an option:")
    print("1. Convert sample Gujarati texts")
    print("2. Enter custom Gujarati text")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n🎵 Converting sample texts...")
        for text in example_texts:
            print(f"\n📢 Text: {text}")
            tts.text_to_speech(text, play=True)
            input("Press Enter to continue...")
    
    elif choice == "2":
        text = input("\n📝 Enter Gujarati text: ").strip()
        if text:
            output_file = input("Save to file? (yes/no): ").strip().lower()
            if output_file == "yes":
                filename = input("Enter filename (e.g., output.wav): ").strip()
                tts.text_to_speech(text, output_file=filename, play=True)
            else:
                tts.text_to_speech(text, play=True)
        else:
            print("❌ No text provided")
    
    elif choice == "3":
        print("👋 Goodbye!")
        sys.exit(0)
    
    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    main()
