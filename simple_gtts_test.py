"""
Simple gTTS test to isolate the problem
"""

import sys
import io

# Fix Windows Unicode encoding issue
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from gtts import gTTS
import os

print("Testing gTTS with Gujarati text...")
print()

# Simple test text
test_text = "नमस्ते"

try:
    print(f"Creating audio for: {test_text}")
    
    # Create gTTS object for Gujarati
    tts = gTTS(text=test_text, lang='gu', slow=False)
    
    # Save to file
    output_file = "test_output.mp3"
    tts.save(output_file)
    
    # Check if file was created
    if os.path.exists(output_file):
        file_size = os.path.getsize(output_file)
        print(f"✓ Success! File created: {output_file}")
        print(f"  File size: {file_size} bytes")
    else:
        print("✗ Error: File was not created")
        
except Exception as e:
    print(f"✗ Error: {type(e).__name__}")
    print(f"  Message: {str(e)}")
    import traceback
    traceback.print_exc()

print()
print("Test complete!")
