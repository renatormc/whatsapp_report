import subprocess
from renderer import render_folder
import config

def render(folder: str) -> None:
    render_folder(folder)

def update() -> None:
    subprocess.run(['git', 'reset', '--hard'], cwd=str(config.APPDIR))
    subprocess.run(['git', 'checkout', 'master'], cwd=str(config.APPDIR))
    subprocess.run(['git', 'pull', 'origin', 'master'], cwd=str(config.APPDIR))

def code() -> None:
    subprocess.run(['code', str(config.APPDIR)])
