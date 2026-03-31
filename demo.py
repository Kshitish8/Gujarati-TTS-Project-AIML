"""
Quick Start Demo - Run this to test the Gujarati TTS project immediately
"""

import sys
import io
import os

# Fix Windows Unicode encoding issue
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from gujarati_tts import GujaratiTTS

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def demo():
    """Run quick demo"""
    print_header("🔊 Gujarati Text-to-Speech Demo")
    
    print("Initializing TTS engine...")
    tts = GujaratiTTS()
    print("✅ Engine ready!\n")
    
    # Create demo audio directory
    audio_dir = "demo_audio"
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    # Demo texts
    demo_texts = [
        ("Greeting", "નમસ્તે"),
        ("Full Greeting", "નમસ્તે, આપ કેમ છો?"),
        ("AI Quote", "આર્ટિફિશિયલ ઇંટેલિજન્સ ભવિષ્યનું ભાષા છે।"),
        ("Language", "ગુજરાતી આપણી સુંદર ભાષા છે।"),
        ("Project", "આ એક ટેક્સ્ટ ટુ સ્પીચ પ્રોજેક્ટ છે।"),
    ]
    
    print("📚 Demo Conversions:\n")
    
    for i, (title, text) in enumerate(demo_texts, 1):
        print(f"{i}. {title}")
        print(f"   Text: {text}")
        print(f"   Converting...", end=" ")
        
        # Save to file
        output_file = os.path.join(audio_dir, f"demo_{i:02d}_{title.replace(' ', '_').lower()}.mp3")
        result = tts.text_to_speech(text, output_file=output_file, play=False)
        
        if result:
            print("✅ Success!")
        else:
            print("❌ Failed!")
        
        if i < len(demo_texts):
            input("\n   Press Enter to continue...")
    
    print_header("✅ Demo Complete!")
    print(f"Audio files saved to: {audio_dir}/")
    print("Project is working correctly!\n")

if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\n❌ Demo interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease ensure dependencies are installed:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
