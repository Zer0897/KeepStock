from src.widget.form import Form
from src.widget.notify import Notification
from src.widget.navigate import NavigationBar
from src.widget.camera import Scanner

from typing import List
from pathlib import Path


KV_DIR: Path = Path(__file__).with_name('kv')
KV_FILES: List[Path] = list(KV_DIR.glob('*.kv'))
