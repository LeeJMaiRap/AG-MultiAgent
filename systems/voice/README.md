# Voice IO

## STT
Use Whisper in local venv:

```bash
/root/.openclaw/workspace/.venv-stt/bin/python \
  /root/.openclaw/workspace/systems/voice/scripts/transcribe.py \
  <audio_file> base
```

Notes:
- Default language forced to Vietnamese in current script.
- Model `base` gives much better results than `tiny`.
- For short/unclear clips, result may still be imperfect.

## TTS
Use edge-tts:

```bash
/root/.openclaw/workspace/.venv-stt/bin/python \
  /root/.openclaw/workspace/systems/voice/scripts/synthesize.py \
  "Xin chào anh Doanh" \
  /root/.openclaw/workspace/systems/voice/output/reply.mp3
```

Default voice:
- `vi-VN-HoaiMyNeural`

## Current status
- STT: working on local test file
- TTS: working, outputs mp3
- Next improvement: auto language detect, preprocessing, confidence/fallback flow
