from .components import ComponentStyles


class Theme:
    def __init__(self, data: dict):
        self.background = data.get("background", {})
        self.text = data.get("text", {})
        self.accent = data.get("accent", {})
        self.card = data.get("card", {})
        self.line = data.get("line", "#000000")

        self.components = ComponentStyles(data)