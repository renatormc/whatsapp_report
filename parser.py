from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
from typing import Literal

FileType = Literal['audio', 'image', 'video', 'file']

@dataclass
class TimestampFormat:
    pattern: str
    format: str


@dataclass
class Body:
    text: str
    filename: str
    is_attachment: bool
    file_type: FileType = 'file'


@dataclass
class Message:
    timestamp: datetime
    sender: str
    body: Body


def get_list_participants(messages: list[Message]) -> list[str]:
    parts: list[str] = []
    for message in messages:
        if message.sender and message.sender not in parts:
            parts.append(message.sender)
    return parts

def analyze_file_type(filename: str) -> FileType:
    ext = Path(filename).suffix.lower()

    audio_extensions = ['.opus', '.mp3', '.aac', '.flac', '.wav', '.m4a', '.ogg', '.wma']
    if ext in audio_extensions:
        return 'audio'
    

    video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg']
    if ext in video_extensions:
        return 'video'
    

    image_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heif', '.svg']
    if ext in image_extensions:
        return 'image'
    return "file"

def parse_body(text: str) -> Body:
    text = text.strip()
    res = re.search(r'([\x20-\x7E]+)\s+\(arquivo anexado\)(.*)', text, re.MULTILINE | re.DOTALL)
    if res:
        return Body(filename=res.group(1), text=res.group(2), is_attachment=True, file_type=analyze_file_type(res.group(1)))
    return Body(filename="", text=text, is_attachment=False)

def extract_message(text: str, tf: TimestampFormat) -> Message:
    pattern1 = r'(rep)\s+-\s+(.{1,100}?):(.+)'.replace("rep", tf.pattern)
    pattern2 = r'(rep)\s+-(.+)'.replace("rep", tf.pattern)
    pattern = pattern1
    res = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if res:
        m = Message(
            timestamp=datetime.strptime(res.group(1), tf.format),
            sender=res.group(2),
            body=parse_body(res.group(3))
        )
        return m
    pattern = pattern2
    res = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if res:
        m = Message(
            timestamp=datetime.strptime(res.group(1), tf.format),
            sender="",
            body=parse_body(res.group(2))
        )
        return m
    raise Exception("not match")


def extract_messages(text: str, tf: TimestampFormat) -> list[Message]:
    pattern = r'(?=^rep - )'.replace("rep", tf.pattern)
    parts = re.split(r'(?=\n\d{2}/\d{2}/\d{4} \d{2}:\d{2} - )', text)
    parts = [part.strip() for part in parts if part and part.strip()]
    return [extract_message(part, tf) for part in parts]



