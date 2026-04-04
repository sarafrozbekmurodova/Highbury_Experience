import tkinter as tk


class TopPanel:
    def __init__(self, parent, main_window):
        self.parent = parent
        self.main_window = main_window
        self.top_nav_buttons = {}

        self.frame = tk.Frame(self.parent, bg=self.main_window.bg_top, height=68)
        self.frame.pack(side="top", fill="x")
        self.frame.pack_propagate(False)

    def build(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]
        self.top_nav_buttons = {}

        brand_frame = tk.Frame(self.frame, bg=self.main_window.bg_top)
        brand_frame.pack(side="left", padx=18)

        tk.Label(
            brand_frame,
            text=t["brand"],
            bg=self.main_window.bg_top,
            fg=self.main_window.text_main,
            font=("Georgia", 18, "bold")
        ).pack(side="left", pady=14)

        nav_frame = tk.Frame(self.frame, bg=self.main_window.bg_top)
        nav_frame.pack(side="left", padx=40)

        nav_items = [
            ("Home", t["home"], self.main_window.show_home),            
            ("Menu", t["menu"], lambda: self.main_window.navigate_to_page("starters", "starters")),
            ("Today's Special", t["todays_special"], self.main_window.show_special_page),
            ("My Order", t["my_order"], None),
        ]

        for internal_name, text, cmd in nav_items:
            if cmd:
                btn = tk.Button(
                    nav_frame,
                    text=text,
                    command=cmd,
                    bg=self.main_window.bg_top,
                    fg=self.main_window.text_soft,
                    activebackground=self.main_window.bg_top,
                    activeforeground=self.main_window.text_main,
                    relief="flat",
                    padx=16,
                    pady=10,
                    font=("Arial", 11),
                    cursor="hand2"
                )
            else:
                btn = tk.Button(
                    nav_frame,
                    text=text,
                    state="disabled",
                    disabledforeground=self.main_window.text_muted,
                    bg=self.main_window.bg_top,
                    relief="flat",
                    padx=16,
                    pady=10,
                    font=("Arial", 11)
                )

            btn.pack(side="left", padx=8, pady=10)
            self.top_nav_buttons[internal_name] = btn

        right_top = tk.Frame(self.frame, bg=self.main_window.bg_top)
        right_top.pack(side="right", padx=18)

        call_btn = tk.Button(
            right_top,
            text=t["call_service"],
            bg=self.main_window.red,
            fg="white",
            activebackground=self.main_window.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=self.main_window.call_service
        )
        call_btn.pack(side="left", padx=(0, 18), pady=10)

        lang_frame = tk.Frame(right_top, bg=self.main_window.bg_top)
        lang_frame.pack(side="left")

        for code in ["EN", "SV", "DE"]:
            active = code == self.main_window.current_language
            btn = tk.Button(
                lang_frame,
                text=code,
                bg=self.main_window.gold if active else self.main_window.bg_top,
                fg="#1b140f" if active else self.main_window.text_soft,
                activebackground=self.main_window.gold,
                activeforeground="#1b140f",
                relief="flat",
                bd=0,
                padx=10,
                pady=6,
                font=("Arial", 10, "bold"),
                cursor="hand2",
                command=lambda c=code: self.main_window.switch_language(c)
            )
            btn.pack(side="left", padx=3)

    def update_highlight(self, active_name):
        for label, btn in self.top_nav_buttons.items():
            if str(btn.cget("state")) == "disabled":
                continue

            if label == active_name:
                btn.config(
                    bg=self.main_window.green,
                    fg="white",
                    activebackground=self.main_window.green_hover,
                    activeforeground="white",
                    font=("Arial", 11, "bold")
                )
            else:
                btn.config(
                    bg=self.main_window.bg_top,
                    fg=self.main_window.text_soft,
                    activebackground=self.main_window.bg_top,
                    activeforeground=self.main_window.text_main,
                    font=("Arial", 11)
                )