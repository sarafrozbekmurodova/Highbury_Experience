import tkinter as tk


class MainWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        # ---------- Language Support ----------
        self.current_language = "EN"   # Default: English
        self.translations = {
            "EN": {
                "brand": "♛ The Crown & Barrel",
                "menu": "Menu",
                "starters": "Starters",
                "light_courses": "Light Courses",
                "main_courses": "Main Courses",
                "set_meals": "Set Meals",
                "desserts": "Desserts",
                "beverages": "Beverages",
                "home": "Home",
                "todays_special": "Today's Special",
                "my_order": "My Order",
                "call_service": "Call Service",
                "order_summary": "Order Summary",
                "single_order": "Single Order",
                "group_order": "Group Order",
                "total": "Total",
                "sub_total": "Subtotal",
                "tip": "Tip",
                "place_order": "Place Order",
                "empty_order": "Your order is empty.\nBrowse our menu and add items.",
                "welcome": "Welcome to The Crown & Barrel",
                "tagline": "Traditional British Pub Fare · Est. 1887",
                "sunday_roast": "Sunday Roast Beef ✩",
                "sunday_roast_desc": "Slow-roasted sirloin with Yorkshire pudding, roast potatoes, seasonal vegetables and rich gravy",
                "add": "+ Add",
                "add_to_order": "+ Add to Order",
                "back_to_home": "Back to Home",
                "start_order": "Start Order"
            },
            "SV": {
                "brand": "♛ Krona & Tunnan",
                "menu": "Meny",
                "starters": "Förrätter",
                "light_courses": "Lätta Rätter",
                "main_courses": "Huvudrätter",
                "set_meals": "Måltidspaket",
                "desserts": "Efterrätter",
                "beverages": "Drycker",
                "home": "Hem",
                "todays_special": "Dagens Special",
                "my_order": "Min Beställning",
                "call_service": "Kalla på Service",
                "order_summary": "Beställningsöversikt",
                "single_order": "Enskild beställning",
                "group_order": "Gruppbeställning",
                "total": "Totalt",
                "sub_total": "Delsumma",
                "tip": "Tip",
                "place_order": "Lägg Beställning",
                "empty_order": "Din beställning är tom.\nBläddra i menyn och lägg till varor.",
                "welcome": "Välkommen till Krona & Tunnan",
                "tagline": "Traditionell brittisk pubmat · Est. 1887",
                "sunday_roast": "Söndagsstekt Oxfilé ✩",
                "sunday_roast_desc": "Långtidsstekt oxfilé med yorkshirepudding, rostade potatisar, säsongens grönsaker och rik gravy",
                "add": "+ Lägg till",
                "add_to_order": "+ Lägg till i beställning",
                "back_to_home": "Tillbaka till Hem",
                "start_order": "Starta beställning"
            }
        }

        # ---------- State ----------
        self.current_page = "home"
        self.current_sidebar_selection = None

        # ---------- Color palette ----------
        self.bg_root = "#201814"
        self.bg_top = "#2a1f1a"
        self.bg_main = "#1f1713"
        self.bg_sidebar = "#1c1511"
        self.bg_center = "#221a16"
        self.bg_right = "#2a201b"
        self.card_bg = "#33261f"
        self.card_border = "#4a352b"

        self.text_main = "#f5efe8"
        self.text_soft = "#c8b8aa"
        self.text_muted = "#8d7f74"

        self.green = "#2d7d57"
        self.green_hover = "#379567"
        self.red = "#a13c4a"
        self.red_hover = "#b54856"
        self.gold = "#d6a34a"
        self.line = "#4a382f"

        self.root.configure(bg=self.bg_root)
        
        self.root.option_add("*Button.highlightThickness", 0)
        self.root.option_add("*Button.borderWidth", 0)
        self.root.option_add("*Button.relief", "flat")
        self.root.option_add("*Button.takeFocus", 0)

        # ---------- Root layout ----------
        self.top_frame = tk.Frame(self.root, bg=self.bg_top, height=68)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)

        self.body_frame = tk.Frame(self.root, bg=self.bg_main)
        self.body_frame.pack(side="top", fill="both", expand=True)

        self.left_frame = tk.Frame(self.body_frame, width=210, bg=self.bg_sidebar)
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.pack_propagate(False)

        self.center_frame = tk.Frame(self.body_frame, bg=self.bg_center)
        self.center_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = tk.Frame(self.body_frame, width=320, bg=self.bg_right)
        self.right_frame.pack(side="right", fill="y")
        self.right_frame.pack_propagate(False)

        # ---------- Center content containers ----------
        self.hero_frame = tk.Frame(self.center_frame, bg=self.bg_center)
        self.page_container = tk.Frame(self.center_frame, bg=self.bg_center)
        self.special_frame = tk.Frame(self.center_frame, bg=self.bg_center)

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        self.confirmation_page = None
        self.special_page = None

        self.top_nav_buttons = {}
        self.sidebar_buttons = {}
        self.tip_buttons = {}

        self.build_top()
        self.build_left()
        self.build_hero()
        self.build_right()

        self.update_order_list([], 0, 0, 0.0)
        self.show_home()
        
    # ====================== LANGUAGE SWITCH ======================
    def switch_language(self, lang):
        if lang == self.current_language:
            return
        self.current_language = lang
        self.build_top()
        self.build_left()
        self.build_hero()
        self.build_right()
        self.build_special_page()
        if self.current_page in self.controller.pages:
            page = self.controller.pages[self.current_page]
            if hasattr(page, 'refresh_language'):
                page.refresh_language(lang)
            else:
                if hasattr(page, 'build_page'):
                    page.build_page()
        if self.current_page == "home":
            self.build_hero()

        if self.current_page == "special":
            self.build_special_page()

    def refresh_ui(self):
        self.build_top()
        self.build_left()
        self.build_hero()
        self.build_right()
        self.build_special_page()
        self.order_list()
        self.order_summary_label()
        self.place_order()

    # =========================================================
    # Top Bar
    # =========================================================
    def build_top(self):
        for widget in self.top_frame.winfo_children():
            widget.destroy()

        t = self.translations[self.current_language]

        brand_frame = tk.Frame(self.top_frame, bg=self.bg_top)
        brand_frame.pack(side="left", padx=18)

        tk.Label(brand_frame, text=t["brand"], bg=self.bg_top, fg=self.text_main,
                 font=("Georgia", 18, "bold")).pack(side="left", pady=14)

        nav_frame = tk.Frame(self.top_frame, bg=self.bg_top)
        nav_frame.pack(side="left", padx=40)

        nav_items = [
            (t["home"], self.show_home),
            (t["menu"], lambda: self.navigate_to_page("starters", t["starters"])),
            (t["todays_special"], self.show_special_page),
            (t["my_order"], None),
        ]

        for text, cmd in nav_items:
            if cmd:
                btn = tk.Button(nav_frame, text=text, command=cmd,
                                bg=self.bg_top, fg=self.text_soft,
                                activebackground=self.bg_top, activeforeground=self.text_main,
                                relief="flat", padx=16, pady=10, font=("Arial", 11), cursor="hand2")
            else:
                btn = tk.Button(nav_frame, text=text, state="disabled",
                                disabledforeground=self.text_muted, bg=self.bg_top,
                                relief="flat", padx=16, pady=10, font=("Arial", 11))
            btn.pack(side="left", padx=8, pady=10)

        right_top = tk.Frame(self.top_frame, bg=self.bg_top)
        right_top.pack(side="right", padx=18)

        call_btn = tk.Button(
            right_top,
            text=t["call_service"],
            bg=self.red,
            fg="white",
            activebackground=self.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=self.call_service
        )
        call_btn.pack(side="left", padx=(0, 18), pady=10)

        # Language Buttons
        lang_frame = tk.Frame(right_top, bg=self.bg_top)
        lang_frame.pack(side="left")

        for code in ["EN", "SV"]:
            active = (code == self.current_language)
            btn = tk.Button(
                lang_frame, text=code,
                bg=self.gold if active else self.bg_top,
                fg="#1b140f" if active else self.text_soft,
                activebackground=self.gold,
                activeforeground="#1b140f",
                relief="flat", bd=0, padx=10, pady=6,
                font=("Arial", 10, "bold"), cursor="hand2",
                command=lambda c=code: self.switch_language(c)
            )
            btn.pack(side="left", padx=3)

    # =========================================================
    # Left Sidebar
    # =========================================================
    def build_left(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        t = self.translations[self.current_language]

        tk.Label(self.left_frame, text=t["menu"], fg=self.text_main, bg=self.bg_sidebar,
                 font=("Georgia", 18, "bold")).pack(anchor="w", padx=20, pady=(22, 18))

        categories = [
            (t["starters"], "starters"),
            (t["light_courses"], "light_courses"),
            (t["main_courses"], "main"),
            (t["set_meals"], "set_meals"),
            (t["desserts"], "desserts"),
            (t["beverages"], "drinks"),
        ]

        self.sidebar_buttons = {}

        for label, key in categories:
            btn = tk.Button(self.left_frame, text=label,
                            bg=self.bg_sidebar, fg=self.text_soft,
                            activebackground=self.green, activeforeground="white",
                            relief="flat", anchor="w", padx=18, pady=12,
                            font=("Arial", 11), cursor="hand2",
                            command=lambda p=key, s=label: self.navigate_to_page(p, s))
            btn.pack(fill="x", padx=14, pady=4)
            self.sidebar_buttons[label] = btn

    # =========================================================
    # Home / Start Screen
    # =========================================================
    def build_hero(self):
        for widget in self.hero_frame.winfo_children():
            widget.destroy()
        t = self.translations[self.current_language]
        outer = tk.Frame(self.hero_frame, bg=self.bg_center)
        outer.pack(fill="both", expand=True, padx=28, pady=28)

        start_card = tk.Frame(
            outer,
            bg=self.card_bg,
            highlightbackground=self.card_border,
            highlightthickness=1
        )
        start_card.pack(expand=True)

        inner = tk.Frame(start_card, bg=self.card_bg)
        inner.pack(padx=80, pady=70)

        tk.Label(
            inner,
            text="♛",
            bg=self.card_bg,
            fg=self.gold,
            font=("Georgia", 30, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            inner,
            text=t["welcome"],
            bg=self.card_bg,
            fg=self.text_main,
            font=("Georgia", 30, "bold")
        ).pack()

        tk.Label(
            inner,
            text=t["tagline"],
            bg=self.card_bg,
            fg=self.text_soft,
            font=("Arial", 13)
        ).pack(pady=(12, 26))

        tk.Button(
            inner,
            text=t["start_order"],
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=36,
            pady=14,
            font=("Arial", 12, "bold"),
            cursor="hand2",
            command=lambda: self.navigate_to_page("starters", "Starters"),
            width=18
        ).pack(pady=(0, 14))

        tk.Button(
            inner,
            text=t["todays_special"],
            bg=self.red,
            fg="white",
            activebackground=self.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=36,
            pady=14,
            font=("Arial", 12, "bold"),
            cursor="hand2",
            command=self.show_special_page,
            width=18
        ).pack()

    # =========================================================
    # Dedicated Today's Special page
    # =========================================================
    def build_special_page(self):
        for widget in self.special_frame.winfo_children():
            widget.destroy()
        t = self.translations[self.current_language]
        wrapper = tk.Frame(self.special_frame, bg=self.bg_center)
        wrapper.pack(fill="both", expand=True, padx=18, pady=18)

        tk.Label(
            wrapper,
            text=t["todays_special"],
            bg=self.bg_center,
            fg=self.text_main,
            font=("Georgia", 28, "bold")
        ).pack(anchor="w", pady=(0, 20))

        special_card = tk.Frame(
            wrapper,
            bg=self.card_bg,
            highlightbackground=self.card_border,
            highlightthickness=1
        )
        special_card.pack(fill="x")

        header = tk.Frame(special_card, bg=self.card_bg)
        header.pack(fill="x", padx=20, pady=(20, 10))

        tk.Label(
            header,
            text=t["sunday_roast"],
            bg=self.card_bg,
            fg=self.text_main,
            font=("Georgia", 22, "bold")
        ).pack(side="left")

        tk.Label(
            header,
            text="£16.50",
            bg=self.card_bg,
            fg=self.gold,
            font=("Arial", 18, "bold")
        ).pack(side="right")

        tk.Label(
            special_card,
            text=t["sunday_roast_desc"],
            bg=self.card_bg,
            fg=self.text_soft,
            font=("Arial", 12),
            justify="left",
            wraplength=850
        ).pack(anchor="w", padx=20, pady=(0, 12))

        tags = tk.Frame(special_card, bg=self.card_bg)
        tags.pack(anchor="w", padx=20, pady=(0, 18))
        
        tag_list = ["England", "Kockens Val", "Söndagsklassiker"] if self.current_language == "SV" else \
                   ["England", "Chef's Choice", "Sunday Classic"]

        for text in tag_list:
            tk.Label(
                tags,
                text=text,
                bg="#403128",
                fg=self.text_soft,
                padx=10,
                pady=6,
                font=("Arial", 9, "bold")
            ).pack(side="left", padx=(0, 8))

        actions = tk.Frame(special_card, bg=self.card_bg)
        actions.pack(fill="x", padx=20, pady=(0, 20))

        tk.Button(
            actions,
            text=t["add_to_order"],
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=20,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=lambda: self.controller.add_to_order(t["sunday_roast"], 16)
        ).pack(side="left")

        tk.Button(
            actions,
            text=t["back_to_home"],
            bg=self.red,
            fg="white",
            activebackground=self.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=20,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=self.show_home
        ).pack(side="left", padx=12)

    # =========================================================
    # Right Order Panel
    # =========================================================
    def build_right(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        t = self.translations[self.current_language]
        header = tk.Frame(self.right_frame, bg=self.bg_right)
        header.pack(fill="x", pady=(14, 0))

        tk.Label(
            header,
            text=t["order_summary"],
            fg=self.text_main,
            bg=self.bg_right,
            font=("Georgia", 18, "bold")
        ).pack(side="left", padx=16)

        mode_frame = tk.Frame(self.right_frame, bg=self.bg_right)
        mode_frame.pack(fill="x", padx=16, pady=(10, 10))

        tk.Button(
            mode_frame,
            text=t["single_order"],
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=12,
            pady=6,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            mode_frame,
            text=t["group_order"],
            state="disabled",
            disabledforeground=self.text_muted,
            bg=self.bg_right,
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=12,
            pady=6,
            font=("Arial", 10)
        ).pack(side="left")

        tip_frame = tk.Frame(self.right_frame, bg=self.bg_right)
        tip_frame.pack(fill="x", padx=16, pady=(0, 10))

        no_tip_btn = tk.Button(
            tip_frame,
            text="No Tip",
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10, "bold"),
            cursor="hand2",
            command=lambda: self.set_tip_mode(0.0)
        )
        no_tip_btn.pack(side="left", padx=(0, 8))

        ten_tip_btn = tk.Button(
            tip_frame,
            text="10% Tip",
            bg=self.bg_right,
            fg=self.text_soft,
            activebackground=self.green,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10),
            cursor="hand2",
            command=lambda: self.set_tip_mode(0.10)
        )
        ten_tip_btn.pack(side="left")

        self.tip_buttons = {
            0.0: no_tip_btn,
            0.10: ten_tip_btn
        }

        divider = tk.Frame(self.right_frame, bg=self.line, height=1)
        divider.pack(fill="x", padx=0, pady=(4, 8))

        self.order_list = tk.Frame(self.right_frame, bg=self.bg_right)
        self.order_list.pack(fill="both", expand=True, padx=10, pady=8)

        self.total_label = tk.Label(self.right_frame, text=f"{t['total']}: 0 kr",
                                    fg=self.gold, bg=self.bg_right, font=("Arial", 14, "bold"))
        self.total_label.pack(anchor="w", padx=16, pady=(6, 10))
        totals_divider = tk.Frame(self.right_frame, bg=self.line, height=1)
        totals_divider.pack(fill="x", padx=16, pady=(8, 10))

        self.subtotal_label = tk.Label(
            self.right_frame,
            text=t["sub_total"]+": 0 kr",
            fg=self.text_soft,
            bg=self.bg_right,
            font=("Arial", 11)
        )
        self.subtotal_label.pack(anchor="w", padx=16, pady=(0, 2))

        self.tip_amount_label = tk.Label(
            self.right_frame,
            text=t["tip"]+": 0 kr",
            fg=self.text_soft,
            bg=self.bg_right,
            font=("Arial", 11)
        )
        self.tip_amount_label.pack(anchor="w", padx=16, pady=(0, 2))

        self.total_label = tk.Label(
            self.right_frame,
            text=t["total"]+": 0 kr",
            fg=self.gold,
            bg=self.bg_right,
            font=("Arial", 14, "bold")
        )
        self.total_label.pack(anchor="w", padx=16, pady=(0, 10))

        self.place_order_btn = tk.Button(
            self.right_frame,
            text=t["place_order"],
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            font=("Arial", 12, "bold"),
            height=2,
            relief="flat",
            bd=0,
            command=self.controller.place_order,
            cursor="hand2"
        )
        self.place_order_btn.pack(fill="x", padx=16, pady=(0, 16))

    # =========================================================
    # Layout visibility helpers
    # =========================================================
    def show_sidebar(self):
        if not self.left_frame.winfo_manager():
            self.left_frame.pack(side="left", fill="y", before=self.center_frame)

    def hide_sidebar(self):
        if self.left_frame.winfo_manager():
            self.left_frame.pack_forget()

    def show_page_container(self):
        if not self.page_container.winfo_manager():
            self.page_container.pack(side="top", fill="both", expand=True, padx=18, pady=18)

    def hide_page_container(self):
        if self.page_container.winfo_manager():
            self.page_container.pack_forget()

    def show_hero(self):
        if not self.hero_frame.winfo_manager():
            self.hero_frame.pack(side="top", fill="both", expand=True)

    def hide_hero(self):
        if self.hero_frame.winfo_manager():
            self.hero_frame.pack_forget()

    def show_special_container(self):
        if not self.special_frame.winfo_manager():
            self.special_frame.pack(side="top", fill="both", expand=True)

    def hide_special_container(self):
        if self.special_frame.winfo_manager():
            self.special_frame.pack_forget()

    # =========================================================
    # Navigation helpers
    # =========================================================
    def navigate_to_page(self, page_name, sidebar_selection=None):
        self.current_page = page_name
        self.current_sidebar_selection = sidebar_selection

        self.hide_hero()
        self.hide_special_container()
        self.show_sidebar()
        self.show_page_container()

        if page_name in self.controller.pages:
            self.show_page(self.controller.pages[page_name])

        self.update_sidebar_highlight()
        self.update_top_nav_highlight("Menu")

    def show_home(self):
        self.current_page = "home"
        self.current_sidebar_selection = None

        self.hide_sidebar()
        self.hide_page_container()
        self.hide_special_container()
        self.build_hero()
        self.show_hero()

        self.update_sidebar_highlight()
        self.update_top_nav_highlight("Home")

    def show_special_page(self):
        self.current_page = "special"
        self.current_sidebar_selection = None

        self.hide_sidebar()
        self.hide_page_container()
        self.hide_hero()
        self.build_special_page()
        self.show_special_container()

        self.update_sidebar_highlight()
        self.update_top_nav_highlight("Today's Special")

    def show_page(self, page_frame):
        page_frame.tkraise()

    def update_sidebar_highlight(self):
        for label, btn in self.sidebar_buttons.items():
            if label == self.current_sidebar_selection:
                btn.config(
                    bg=self.green,
                    fg="white",
                    activebackground=self.green_hover,
                    activeforeground="white",
                    font=("Arial", 11, "bold")
                )
            else:
                btn.config(
                    bg=self.bg_sidebar,
                    fg=self.text_soft,
                    activebackground=self.green,
                    activeforeground="white",
                    font=("Arial", 11)
                )

    def update_top_nav_highlight(self, active_name):
        for label, btn in self.top_nav_buttons.items():
            if str(btn.cget("state")) == "disabled":
                continue

            if label == active_name:
                btn.config(
                    bg=self.green,
                    fg="white",
                    activebackground=self.green_hover,
                    activeforeground="white",
                    font=("Arial", 11, "bold")
                )
            else:
                btn.config(
                    bg=self.bg_top,
                    fg=self.text_soft,
                    activebackground=self.bg_top,
                    activeforeground=self.text_main,
                    font=("Arial", 11)
                )

    def set_tip_mode(self, tip_percentage):
        self.controller.set_tip_percentage(tip_percentage)
        self.update_tip_buttons(tip_percentage)

    def update_tip_buttons(self, active_tip_percentage):
        for tip_value, btn in self.tip_buttons.items():
            if tip_value == active_tip_percentage:
                btn.config(
                    bg=self.green,
                    fg="white",
                    activebackground=self.green_hover,
                    activeforeground="white",
                    font=("Arial", 10, "bold")
                )
            else:
                btn.config(
                    bg=self.bg_right,
                    fg=self.text_soft,
                    activebackground=self.green,
                    activeforeground="white",
                    font=("Arial", 10)
                )

    def call_service(self):
        popup = tk.Toplevel(self.root)
        popup.title(t["call_service"])
        popup.configure(bg=self.bg_center)
        popup.geometry("320x180")
        popup.resizable(False, False)

        tk.Label(
            popup,
            text="Staff has been called.",
            bg=self.bg_center,
            fg=self.text_main,
            font=("Arial", 14, "bold")
        ).pack(pady=(35, 10))

        tk.Label(
            popup,
            text="A member of staff will assist you shortly.",
            bg=self.bg_center,
            fg=self.text_soft,
            font=("Arial", 11)
        ).pack(pady=(0, 20))

        tk.Button(
            popup,
            text="OK",
            command=popup.destroy,
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=20,
            pady=8,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack()

    # =========================================================
    # Order panel updates
    # =========================================================
    def update_order_list(self, order_items, subtotal, total, tip_percentage):
        for widget in self.order_list.winfo_children():
            widget.destroy()
        t = self.translations[self.current_language]
        self.update_tip_buttons(tip_percentage)

        tip_amount = total - subtotal

        if not order_items:
            tk.Label(
                self.order_list,
                text=t["empty_order"],
                fg=self.text_muted,
                bg=self.bg_right,
                font=("Arial", 11),
                justify="center"
            ).pack(expand=True, pady=80)

            self.subtotal_label.config(text="Subtotal: 0 kr")
            self.tip_amount_label.config(text="Tip: 0 kr")
            self.total_label.config(text=t["total"]+": 0 kr")
            return

        for i, item in enumerate(order_items):
            item_frame = tk.Frame(
                self.order_list,
                bg=self.card_bg,
                highlightbackground=self.card_border,
                highlightthickness=1
            )
            item_frame.pack(fill="x", pady=6, padx=4)

            top_row = tk.Frame(item_frame, bg=self.card_bg)
            top_row.pack(fill="x", padx=10, pady=(8, 4))

            tk.Label(
                top_row,
                text=item["name"],
                fg=self.text_main,
                bg=self.card_bg,
                anchor="w",
                font=("Arial", 11, "bold")
            ).pack(side="left", fill="x", expand=True)

            delete_btn = tk.Button(
                top_row,
                text="×",
                fg="#ff7a7a",
                bg=self.card_bg,
                activebackground=self.card_bg,
                activeforeground="#ff9a9a",
                font=("Arial", 14, "bold"),
                width=2,
                relief="flat",
                bd=0,
                highlightthickness=0,
                takefocus=False,
                cursor="hand2",
                command=lambda idx=i: self.controller.remove_from_order(idx)
            )
            delete_btn.pack(side="right")

            bottom_row = tk.Frame(item_frame, bg=self.card_bg)
            bottom_row.pack(fill="x", padx=10, pady=(0, 10))

            qty_frame = tk.Frame(bottom_row, bg=self.card_bg)
            qty_frame.pack(side="left")

            minus_btn = tk.Button(
                qty_frame,
                text="−",
                width=3,
                bg="#1f1a17",
                fg=self.green,
                activebackground="#2b2521",
                activeforeground=self.green,
                relief="flat",
                bd=0,
                font=("Arial", 12, "bold"),
                cursor="hand2",
                command=lambda idx=i: self.controller.change_quantity(idx, -1)
            )
            minus_btn.pack(side="left", padx=2)

            tk.Label(
                qty_frame,
                text=str(item["quantity"]),
                bg=self.card_bg,
                fg=self.text_main,
                width=3,
                font=("Arial", 11, "bold")
            ).pack(side="left", padx=4)

            plus_btn = tk.Button(
                qty_frame,
                text="+",
                width=3,
                bg="#1f1a17",
                fg=self.green,
                activebackground="#2b2521",
                activeforeground=self.green,
                relief="flat",
                bd=0,
                font=("Arial", 12, "bold"),
                cursor="hand2",
                command=lambda idx=i: self.controller.change_quantity(idx, 1)
            )
            plus_btn.pack(side="left", padx=2)

            item_total = item["price"] * item["quantity"]

            tk.Label(
                bottom_row,
                text=f"{item_total} kr",
                fg=self.gold,
                bg=self.card_bg,
                font=("Arial", 11, "bold")
            ).pack(side="right")

        self.subtotal_label.config(text=f"Subtotal: {subtotal} kr")
        self.tip_amount_label.config(text=f"Tip: {tip_amount} kr")
        self.total_label.config(text=f"Total: {total} kr")

    # =========================================================
    # Confirmation page
    # =========================================================
    def show_confirmation_page(self, order_items, subtotal, total, tip_percentage):
        if self.confirmation_page is None:
            self.confirmation_page = tk.Frame(self.page_container, bg=self.bg_center)
            self.confirmation_page.grid(row=0, column=0, sticky="nsew")

            tk.Label(
                self.confirmation_page,
                text="Thank You!",
                font=("Georgia", 26, "bold"),
                fg=self.gold,
                bg=self.bg_center
            ).pack(pady=50)

            tk.Label(
                self.confirmation_page,
                text="Your order has been placed successfully.",
                font=("Arial", 14),
                fg=self.text_main,
                bg=self.bg_center
            ).pack(pady=10)

            self.order_summary_label = tk.Label(
                self.confirmation_page,
                text="",
                font=("Arial", 11),
                fg=self.text_soft,
                bg=self.bg_center,
                justify="left"
            )
            self.order_summary_label.pack(pady=20, padx=40)

            tk.Button(
                self.confirmation_page,
                text="Back to Menu",
                bg=self.green,
                fg="white",
                activebackground=self.green_hover,
                activeforeground="white",
                font=("Arial", 12, "bold"),
                width=20,
                height=2,
                relief="flat",
                bd=0,
                cursor="hand2",
                command=self.go_back_to_menu
            ).pack(pady=30)

        tip_amount = total - subtotal

        summary = "Order Summary:\n\n"
        for item in order_items:
            summary += f"• {item['quantity']} x {item['name']}   ({item['price'] * item['quantity']} kr)\n"

        summary += f"\nSubtotal: {subtotal} kr"
        summary += f"\nTip: {tip_amount} kr"
        if tip_percentage > 0:
            summary += f" ({int(tip_percentage * 100)}%)"
        summary += f"\nTotal: {total} kr"

        self.order_summary_label.config(text=summary)
        self.show_page_container()
        self.hide_hero()
        self.hide_special_container()
        self.hide_sidebar()
        self.confirmation_page.tkraise()

    def go_back_to_menu(self):
        self.navigate_to_page("starters", "Starters")
