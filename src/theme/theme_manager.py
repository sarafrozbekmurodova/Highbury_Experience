from .theme_loader import ThemeLoader
from .theme import Theme


class ThemeManager:
    _instance = None

    def __init__(self, theme_name="dark"):
        data = ThemeLoader.load(theme_name)
        self._theme = Theme(data)
        self._theme_name = theme_name

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ThemeManager()
        return cls._instance

    def get_theme(self):
        return self._theme

    def set_theme(self, theme_name: str):
        data = ThemeLoader.load(theme_name)
        self._theme = Theme(data)
        self._theme_name = theme_name

    def get_theme_name(self):
        return self._theme_name