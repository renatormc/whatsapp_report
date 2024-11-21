import subprocess
from renderer import render_folder
import config
from InquirerPy import prompt
from parser import timestamp_options


def render(folder: str) -> None:
    map = {t.example:t for t in timestamp_options}
    questions = [
        {
            "name": "tf",
            "type": "list",
            "message": "Formato de data e hora:",
            "choices": list(map.keys())
        }
    ]
    result = prompt(questions)
    render_folder(folder, map[result['tf']]) #type: ignore


def update() -> None:
    subprocess.run(['git', 'reset', '--hard'], cwd=str(config.APPDIR))
    subprocess.run(['git', 'checkout', 'master'], cwd=str(config.APPDIR))
    subprocess.run(['git', 'pull', 'origin', 'master'], cwd=str(config.APPDIR))


def code() -> None:
    subprocess.run(['code', str(config.APPDIR)])
