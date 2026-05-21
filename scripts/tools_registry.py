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
    # Use voice-stack venv if it exists, otherwise fallback to system python
    venv_python = BASE_DIR / ".venvs" / "voice-stack" / "Scripts" / "python.exe"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable or "python"

def markdown_to_pdf(input_md: str, output_pdf: str) -> str:
    """
    Chuyển đổi file Markdown sang PDF sử dụng weasyprint/reportlab.
    
    Args:
        input_md: Đường dẫn đến file markdown đầu vào.
        output_pdf: Đường dẫn lưu file PDF đầu ra.
        
    Returns:
        Thông điệp trạng thái hoàn thành hoặc lỗi.
    """
    script_path = BASE_DIR / "systems" / "pm-agent" / "skills" / "infrastructure" / "markdown-to-pdf" / "scripts" / "md_to_pdf.py"
    if not script_path.exists():
        return f"Error: Cannot find md_to_pdf script at {script_path}"
        
    cmd = [get_python_exe(), str(script_path), input_md, output_pdf]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Success: PDF generated successfully at {output_pdf}. Details: {res.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"Error running PDF generation: {e.stderr.strip()}"

def voice_to_text(audio_path: str, language: str = "vi") -> str:
    """
    Chuyển đổi giọng nói từ file âm thanh sang văn bản (STT).
    
    Args:
        audio_path: Đường dẫn đến file âm thanh (wav, mp3, v.v.).
        language: Ngôn ngữ nhận diện, ví dụ "vi" hoặc "en".
        
    Returns:
        Văn bản đã nhận diện hoặc thông báo lỗi.
    """
    script_path = BASE_DIR / "ops" / "scripts" / "voice" / "voice_to_text.py"
    if not script_path.exists():
        return f"Error: Cannot find voice_to_text script at {script_path}"
        
    cmd = [get_python_exe(), str(script_path), audio_path, "--language", language]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running STT: {e.stderr.strip()}"

def text_to_voice(text: str, output_name: str = "voice-output") -> str:
    """
    Chuyển đổi văn bản thành giọng nói (TTS) sử dụng edge-tts.
    
    Args:
        text: Văn bản cần chuyển thành giọng nói.
        output_name: Tên file âm thanh đầu ra (không cần đuôi .mp3).
        
    Returns:
        Đường dẫn file âm thanh đã tạo hoặc thông báo lỗi.
    """
    script_path = BASE_DIR / "ops" / "scripts" / "voice" / "text_to_voice.py"
    if not script_path.exists():
        return f"Error: Cannot find text_to_voice script at {script_path}"
        
    cmd = [get_python_exe(), str(script_path), "--text", text, "--name", output_name]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running TTS: {e.stderr.strip()}"

def generate_daily_report(target_path: str, date: str = "", mode: str = "project") -> str:
    """
    Tạo báo cáo dự án hàng ngày (Daily Project Report) dựa trên trạng thái của dự án hoặc framework.
    
    Args:
        target_path: Đường dẫn thư mục gốc dự án hoặc workspace.
        date: Ngày báo cáo định dạng YYYY-MM-DD. Nếu rỗng sẽ lấy ngày hiện tại.
        mode: Chế độ báo cáo ("project" hoặc "framework").
        
    Returns:
        Đường dẫn file báo cáo đã được sinh hoặc thông báo lỗi.
    """
    script_path = BASE_DIR / "systems" / "pm-agent" / "skills" / "project-operations" / "daily-project-report-generator" / "scripts" / "generate_daily_report.py"
    if not script_path.exists():
        return f"Error: Cannot find generate_daily_report script at {script_path}"
        
    cmd = [get_python_exe(), str(script_path), target_path, "--mode", mode]
    if date:
        cmd.extend(["--date", date])
        
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Success: Daily report generated at {res.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"Error generating daily report: {e.stderr.strip()}"

# Print list of registered tools if run directly
if __name__ == "__main__":
    print("=== Đăng ký Tools thành công cho Antigravity 2.0 ===")
    print(f"1. markdown_to_pdf: [Path: {BASE_DIR}/systems/pm-agent/skills/infrastructure/markdown-to-pdf/scripts/md_to_pdf.py]")
    print(f"2. voice_to_text: [Path: {BASE_DIR}/ops/scripts/voice/voice_to_text.py]")
    print(f"3. text_to_voice: [Path: {BASE_DIR}/ops/scripts/voice/text_to_voice.py]")
    print(f"4. generate_daily_report: [Path: {BASE_DIR}/systems/pm-agent/skills/project-operations/daily-project-report-generator/scripts/generate_daily_report.py]")
