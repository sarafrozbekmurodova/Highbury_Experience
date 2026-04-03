from theme.theme_manager import ThemeManager


class StyledButton:
    def __init__(self, widget, variant="primary", size="md", icon=None, compound="left", command=None):
        """
        widget: tk.Label (IMPORTANT for macOS)
        command: function to call on click
        """
        self.widget = widget
        self.variant = variant
        self.size = size
        self.icon = icon
        self.compound = compound
        self.command = command

        self.theme = ThemeManager.get_instance().get_theme()

        self.style = self.theme.components.get_button(variant)
        self.size_style = self.theme.components.get_button_size(size)

        if self.style is None:
            raise ValueError(f"Button variant '{variant}' not found")

        self._apply_style()
        self._bind_events()

    # ------------------------
    # STYLE
    # ------------------------
    def _apply_style(self):
        self.widget.configure(
            bg=self.style.bg,
            fg=self.style.fg,
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )

        # Size
        if self.size_style:
            self.widget.configure(
                padx=self.size_style.get("padx", 10),
                pady=self.size_style.get("pady", 5)
            )

            font_size = self.size_style.get("font_size")
            if font_size:
                self.widget.configure(font=("Arial", font_size))

        # Icon
        if self.icon:
            self.widget.configure(image=self.icon, compound=self.compound)
            self.widget.image = self.icon  # prevent GC

    # ------------------------
    # EVENTS
    # ------------------------
    def _bind_events(self):
        self.widget.bind("<Enter>", self._on_enter)
        self.widget.bind("<Leave>", self._on_leave)
        self.widget.bind("<Button-1>", self._on_click)

    def _on_enter(self, event):
        self.widget.configure(bg=self.style.hover_bg)

    def _on_leave(self, event):
        self.widget.configure(bg=self.style.bg)

    def _on_click(self, event):
        if self.command:
            self.command()

    # ------------------------
    # PUBLIC
    # ------------------------
    def update_variant(self, variant):
        self.variant = variant
        self.style = self.theme.components.get_button(variant)
        self._apply_style()

    def update_size(self, size):
        self.size = size
        self.size_style = self.theme.components.get_button_size(size)
        self._apply_style()