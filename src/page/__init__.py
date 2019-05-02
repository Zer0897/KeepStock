from src.page.page import BaseView, InventoryViewPage, InPage, OutPage, EditPage
from src.page.splash import SplashPage
from src.page.menu import MenuPage
from typing import List
from pathlib import Path


KV_DIR: Path = Path(__file__).with_name('kv')
KV_FILES: List[Path] = list(KV_DIR.glob('*.kv'))
