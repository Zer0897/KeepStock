from src.page.view import BaseView
from src.page.splash import SplashPage
from src.page.menu import MenuPage
from src.page.inventory import ViewPage, InPage, OutPage, EditPage
from typing import List
from pathlib import Path


KV_DIR: Path = Path(__file__).with_name('kv')
KV_FILES: List[Path] = list(KV_DIR.glob('*.kv'))
