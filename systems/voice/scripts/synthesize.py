#!/usr/bin/env python3
"""
Synthesize speech from text using edge-tts.
Usage: python synthesize.py <text> <output_file> [voice]
"""
import sys
import asyncio

async def synthesize(text, output_file, voice="vi-VN-HoaiMyNeural"):
    """Synthesize speech using edge-tts."""
    try:
        import edge_tts
        
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        return {"success": True, "output": output_file, "voice": voice}
    except ImportError:
        return {"error": "edge-tts not installed. Run: pip install edge-tts"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python synthesize.py <text> <output_file> [voice]")
        sys.exit(1)
    
    text = sys.argv[1]
    output_file = sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "vi-VN-HoaiMyNeural"
    
    result = asyncio.run(synthesize(text, output_file, voice))
    
    if "error" in result:
        print(f"ERROR: {result['error']}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Synthesized to: {result['output']}")
