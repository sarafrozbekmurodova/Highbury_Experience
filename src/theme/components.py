class ButtonStyle:
    def __init__(self, data: dict):
        self.bg = data.get("bg")
        self.fg = data.get("fg")
        self.hover_bg = data.get("hover_bg")
        self.border = data.get("border")


class ComponentStyles:
    def __init__(self, data: dict):
        self.button = {
            name: ButtonStyle(style)
            for name, style in data.get("button", {}).items()
        }

        self.button_sizes = data.get("button_sizes", {})

    def get_button(self, variant: str):
        return self.button.get(variant)

    def get_button_size(self, size: str):
        return self.button_sizes.get(size)