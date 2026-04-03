import tkinter as tk


class Sidebar:
    def __init__(self, parent, main_window, controller):
        self.parent = parent
        self.main_window = main_window
        self.controller = controller

        self.frame = tk.Frame(
            self.parent,
            width=210,
            bg=self.main_window.bg_sidebar
        )
        self.frame.pack(side="left", fill="y")
        self.frame.pack_propagate(False)

        self.buttons = {}

        self.build()

    def build(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]

        tk.Label(
            self.frame,
            text=t["menu"],
            fg=self.main_window.text_main,
            bg=self.main_window.bg_sidebar,
            font=("Georgia", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(22, 18))

        categories = [
            (t["starters"], "starters"),
            (t["light_courses"], "light_courses"),
            (t["main_courses"], "main"),
            (t["set_meals"], "set_meals"),
            (t["desserts"], "desserts"),
            (t["beverages"], "drinks"),
        ]

        self.buttons = {}

        for label, key in categories:
            btn = tk.Button(
                self.frame,
                text=label,
                bg=self.main_window.bg_sidebar,
                fg=self.main_window.text_soft,
                activebackground=self.main_window.green,
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=18,
                pady=12,
                font=("Arial", 11),
                cursor="hand2",
                command=lambda p=key, s=label: self.main_window.navigate_to_page(p, s)
            )
            btn.pack(fill="x", padx=14, pady=4)
            self.buttons[label] = btn

    def update_highlight(self, selected_label):
        for label, btn in self.buttons.items():
            if label == selected_label:
                btn.config(
                    bg=self.main_window.green,
                    fg="white",
                    activebackground=self.main_window.green_hover,
                    activeforeground="white",
                    font=("Arial", 11, "bold")
                )
            else:
                btn.config(
                    bg=self.main_window.bg_sidebar,
                    fg=self.main_window.text_soft,
                    activebackground=self.main_window.green,
                    activeforeground="white",
                    font=("Arial", 11)
                )