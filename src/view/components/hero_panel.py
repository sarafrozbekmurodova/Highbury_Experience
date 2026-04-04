"""
Hero panel component.

The name "HeroPanel" comes from UI/UX terminology, where a "hero section"
refers to the prominent introductory area on a screen, typically used to
welcome users and highlight primary actions.

Responsibilities:
- Display the home screen introduction
- Show welcome text and tagline
- Provide primary navigation actions (start order, today's special)
"""

import tkinter as tk


class HeroPanel:
    """
    Component representing the home screen's main content area.

    This panel is shown when the user is on the home page and acts as the
    primary entry point into the ordering flow.
    """

    def __init__(self, parent, main_window):
        """
        Initialize the hero panel.

        :param parent: Parent container
        :param main_window: Reference to the main window for styling and navigation
        """
        self.parent = parent
        self.main_window = main_window
        self.frame = tk.Frame(self.parent, bg=self.main_window.bg_center)

    def build(self):
        """
        Build or rebuild the hero panel UI.

        This method:
        - clears existing content
        - renders welcome text and branding
        - creates action buttons for navigation
        """
        for widget in self.frame.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]

        outer = tk.Frame(self.frame, bg=self.main_window.bg_center)
        outer.pack(fill="both", expand=True, padx=28, pady=28)

        start_card = tk.Frame(
            outer,
            bg=self.main_window.card_bg,
            highlightbackground=self.main_window.card_border,
            highlightthickness=1
        )
        start_card.pack(expand=True)

        inner = tk.Frame(start_card, bg=self.main_window.card_bg)
        inner.pack(padx=80, pady=70)

        tk.Label(
            inner,
            text="♛",
            bg=self.main_window.card_bg,
            fg=self.main_window.gold,
            font=("Georgia", 30, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            inner,
            text=t["welcome"],
            bg=self.main_window.card_bg,
            fg=self.main_window.text_main,
            font=("Georgia", 30, "bold")
        ).pack()

        tk.Label(
            inner,
            text=t["tagline"],
            bg=self.main_window.card_bg,
            fg=self.main_window.text_soft,
            font=("Arial", 13)
        ).pack(pady=(12, 26))

        tk.Button(
            inner,
            text=t["start_order"],
            bg=self.main_window.green,
            fg="white",
            activebackground=self.main_window.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=36,
            pady=14,
            font=("Arial", 12, "bold"),
            cursor="hand2",
            command=lambda: self.main_window.navigate_to_page("starters", "starters"),
            width=18
        ).pack(pady=(0, 14))

        tk.Button(
            inner,
            text=t["todays_special"],
            bg=self.main_window.red,
            fg="white",
            activebackground=self.main_window.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=36,
            pady=14,
            font=("Arial", 12, "bold"),
            cursor="hand2",
            command=self.main_window.show_special_page,
            width=18
        ).pack()