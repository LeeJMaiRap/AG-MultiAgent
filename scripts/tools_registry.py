#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.parent.resolve()

def get_python_exe():
    # Sử dụng venv voice-stack nếu có, nếu không thì dùng python mặc định
    venv_python = BASE_DIR / ".venvs" / "voice-stack" / "Scripts" / "python.exe"
    if venv_python.exists():
        return str(venv_python)
    return "python"

def markdown_to_pdf(input_md: str, output_pdf: str) -> bool:
    """Chuyển đổi file Markdown sang PDF sử dụng weasyprint/reportlab."""
    script_path = BASE_DIR / "systems" / "pm-agent" / "skills" / "infrastructure" / "markdown-to-pdf" / "scripts" / "md_to_pdf.py"
    if not script_path.exists():
        print(f"Lỗi: Không tìm thấy script md_to_pdf tại {script_path}")
        return False
        
    cmd = [get_python_exe(), str(script_path), input_md, output_pdf]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"PDF Output: {res.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Lỗi chạy script xuất PDF: {e.stderr}")
        return False

def voice_to_text(audio_path: str, language: str = "vi") -> str:
    """Chuyển đổi giọng nói từ file âm thanh sang văn bản (STT)."""
    script_path = BASE_DIR / "ops" / "scripts" / "voice" / "voice_to_text.py"
    if not script_path.exists():
        return f"Lỗi: Không tìm thấy script voice_to_text tại {script_path}"
        
    cmd = [get_python_exe(), str(script_path), audio_path, "--language", language]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Lỗi chạy STT: {e.stderr}"

def text_to_voice(text: str, output_name: str = "voice-output") -> str:
    """Chuyển đổi văn bản thành giọng nói (TTS) sử dụng edge-tts."""
    script_path = BASE_DIR / "ops" / "scripts" / "voice" / "text_to_voice.py"
    if not script_path.exists():
        return f"Lỗi: Không tìm thấy script text_to_voice tại {script_path}"
        
    cmd = [get_python_exe(), str(script_path), "--text", text, "--name", output_name]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Lỗi chạy TTS: {e.stderr}"

# In ra danh sách các công cụ đã đăng ký để kiểm tra
if __name__ == "__main__":
    print("=== Đăng ký Tools thành công cho Antigravity 2.0 ===")
    print(f"1. markdown_to_pdf: [Path: {BASE_DIR}/systems/pm-agent/skills/infrastructure/markdown-to-pdf/scripts/md_to_pdf.py]")
    print(f"2. voice_to_text: [Path: {BASE_DIR}/ops/scripts/voice/voice_to_text.py]")
    print(f"3. text_to_voice: [Path: {BASE_DIR}/ops/scripts/voice/text_to_voice.py]")
