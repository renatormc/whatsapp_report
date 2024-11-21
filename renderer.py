from pathlib import Path
from typing import Iterable
from jinja2 import Environment, FileSystemLoader, select_autoescape
import config
from parser import Message, TimestampFormat, extract_messages, get_list_participants


env = Environment(
    loader=FileSystemLoader(config.APPDIR / "templates"),
    autoescape=select_autoescape()
)

env.filters['timestamp'] = lambda x: x.strftime("%d/%m/%Y %H:%M:%S")


def render_template(tpl_name: str, **kwargs) -> str:
    template = env.get_template(tpl_name)
    return template.render(**kwargs)


def render_chat(messages: Iterable[Message], dest: Path, me: str) -> None:
    html = render_template("chat.jinja", messages=messages, me=me)
    dest.write_text(html, encoding="utf-8")


def render_folder(folder: str, tf: TimestampFormat) -> None:
    path = Path(folder)
    for entry in path.iterdir():
        if entry.name.startswith("Conversa do WhatsApp com") and entry.suffix == ".txt":
            txt_path = entry
            break
    else:
        print("not found .txt file")
        return
    text = txt_path.read_text(encoding="utf-8")

    messages = extract_messages(text, tf)
    participants = get_list_participants(messages)
    dest_file = txt_path.with_suffix(".html")
    render_chat(messages, dest_file, me=participants[0])
    print(f"Gerado arquivo \"{dest_file.absolute()}\"")
