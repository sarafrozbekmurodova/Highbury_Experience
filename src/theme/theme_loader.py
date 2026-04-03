import json
from pathlib import Path


class ThemeLoader:
    @staticmethod
    def load(theme_name: str) -> dict:
        base_path = Path(__file__).parent / "themes"
        file_path = base_path / f"{theme_name}.json"

        if not file_path.exists():
            raise FileNotFoundError(f"Theme '{theme_name}' not found.")

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)