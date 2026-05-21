#!/usr/bin/env python3
"""
Transcribe audio file using Whisper.
Usage: python transcribe.py <audio_file> [model_size]
"""
import sys
import os

def transcribe(audio_path, model_size="base"):
    """Transcribe audio file using Whisper."""
    import whisper
    
    if not os.path.exists(audio_path):
        return {"error": f"File not found: {audio_path}"}
    
    try:
        model = whisper.load_model(model_size)
        result = model.transcribe(audio_path, language="vi")
        return {
            "text": result["text"].strip(),
            "language": result.get("language", "vi"),
            "model": model_size
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file> [model_size]")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "base"
    
    result = transcribe(audio_file, model_size)
    
    if "error" in result:
        print(f"ERROR: {result['error']}", file=sys.stderr)
        sys.exit(1)
    else:
        print(result["text"])
