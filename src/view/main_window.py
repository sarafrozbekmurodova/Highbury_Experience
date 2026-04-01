import tkinter as tk


class MainWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

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

        self.build_top()
        self.build_left()
        self.build_hero()
        self.build_right()

        self.update_order_list([], 0)
        self.show_home()

    # =========================================================
    # Top Bar
    # =========================================================
    def build_top(self):
        brand_frame = tk.Frame(self.top_frame, bg=self.bg_top)
        brand_frame.pack(side="left", padx=18)

        tk.Label(
            brand_frame,
            text="♛ The Crown & Barrel",
            bg=self.bg_top,
            fg=self.text_main,
            font=("Georgia", 18, "bold")
        ).pack(side="left", pady=14)

        nav_frame = tk.Frame(self.top_frame, bg=self.bg_top)
        nav_frame.pack(side="left", padx=40)

        nav_items = [
            ("Home", self.show_home, True),
            ("Menu", lambda: self.navigate_to_page("starters", "Starters"), True),
            ("Today's Special", self.show_special_page, True),
            ("My Order", None, False),
        ]

        for label, command, enabled in nav_items:
            if enabled:
                btn = tk.Button(
                    nav_frame,
                    text=label,
                    command=command,
                    bg=self.bg_top,
                    fg=self.text_soft,
                    activebackground=self.bg_top,
                    activeforeground=self.text_main,
                    relief="flat",
                    bd=0,
                    padx=16,
                    pady=10,
                    font=("Arial", 11),
                    cursor="hand2"
                )
            else:
                btn = tk.Button(
                    nav_frame,
                    text=label,
                    state="disabled",
                    disabledforeground=self.text_muted,
                    bg=self.bg_top,
                    relief="flat",
                    bd=0,
                    padx=16,
                    pady=10,
                    font=("Arial", 11)
                )

            btn.pack(side="left", padx=8, pady=10)
            self.top_nav_buttons[label] = btn

        right_top = tk.Frame(self.top_frame, bg=self.bg_top)
        right_top.pack(side="right", padx=18)

        call_btn = tk.Button(
            right_top,
            text="Call Service",
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

        lang_frame = tk.Frame(right_top, bg=self.bg_top)
        lang_frame.pack(side="left")

        en_btn = tk.Button(
            lang_frame,
            text="EN",
            bg=self.gold,
            fg="#1b140f",
            activebackground=self.gold,
            activeforeground="#1b140f",
            relief="flat",
            bd=0,
            padx=8,
            pady=6,
            font=("Arial", 9, "bold"),
            cursor="hand2"
        )
        en_btn.pack(side="left", padx=3)

        for code in ["SV", "DE"]:
            btn = tk.Button(
                lang_frame,
                text=code,
                state="disabled",
                disabledforeground=self.text_muted,
                bg=self.bg_top,
                relief="flat",
                bd=0,
                padx=8,
                pady=6,
                font=("Arial", 9, "bold")
            )
            btn.pack(side="left", padx=3)

    # =========================================================
    # Left Sidebar
    # =========================================================
    def build_left(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.left_frame,
            text="Menu",
            fg=self.text_main,
            bg=self.bg_sidebar,
            font=("Georgia", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(22, 18))

        categories = [
            ("Starters", "starters"),
            ("Light Courses", "light_courses"),
            ("Main Courses", "main"),
            ("Set Meals", "set_meals"),
            ("Desserts", "desserts"),
            ("Beverages", "drinks"),
        ]

        self.sidebar_buttons = {}

        for label, page_key in categories:
            btn = tk.Button(
                self.left_frame,
                text=label,
                bg=self.bg_sidebar,
                fg=self.text_soft,
                activebackground=self.green,
                activeforeground="white",
                relief="flat",
                bd=0,
                anchor="w",
                padx=18,
                pady=12,
                font=("Arial", 11),
                cursor="hand2",
                command=lambda p=page_key, s=label: self.navigate_to_page(p, s)
            )
            btn.pack(fill="x", padx=14, pady=4)
            self.sidebar_buttons[label] = btn

        self.update_sidebar_highlight()

    # =========================================================
    # Home / Hero
    # =========================================================
    def build_hero(self):
        for widget in self.hero_frame.winfo_children():
            widget.destroy()

        welcome_card = tk.Frame(
            self.hero_frame,
            bg=self.card_bg,
            highlightbackground=self.card_border,
            highlightthickness=1,
            height=420
        )
        welcome_card.pack(fill="both", expand=True, pady=(0, 18))
        welcome_card.pack_propagate(False)

        inner = tk.Frame(welcome_card, bg=self.card_bg)
        inner.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            inner,
            text="♛",
            bg=self.card_bg,
            fg=self.gold,
            font=("Georgia", 28, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            inner,
            text="Welcome to The Crown & Barrel",
            bg=self.card_bg,
            fg=self.text_main,
            font=("Georgia", 32, "bold")
        ).pack()

        tk.Label(
            inner,
            text="Traditional British Pub Fare · Est. 1887",
            bg=self.card_bg,
            fg=self.text_soft,
            font=("Georgia", 14)
        ).pack(pady=(10, 22))

        cta_frame = tk.Frame(inner, bg=self.card_bg)
        cta_frame.pack()

        tk.Button(
            cta_frame,
            text="Menu",
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=22,
            pady=12,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=lambda: self.navigate_to_page("starters", "Starters")
        ).pack(side="left", padx=8)

        tk.Button(
            cta_frame,
            text="Today's Special",
            bg=self.red,
            fg="white",
            activebackground=self.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=22,
            pady=12,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=self.show_special_page
        ).pack(side="left", padx=8)

        special_title = tk.Label(
            self.hero_frame,
            text="✧ Today's Special",
            bg=self.bg_center,
            fg=self.text_main,
            font=("Georgia", 20, "bold")
        )
        special_title.pack(anchor="w", pady=(0, 12))

        special_card = tk.Frame(
            self.hero_frame,
            bg=self.card_bg,
            highlightbackground=self.card_border,
            highlightthickness=1
        )
        special_card.pack(fill="x")

        left = tk.Frame(special_card, bg=self.card_bg)
        left.pack(side="left", fill="both", expand=True, padx=18, pady=16)

        tk.Label(
            left,
            text="Sunday Roast Beef ✩",
            bg=self.card_bg,
            fg=self.text_main,
            font=("Georgia", 16, "bold"),
            anchor="w"
        ).pack(anchor="w")

        tk.Label(
            left,
            text="Slow-roasted sirloin with Yorkshire pudding, roast potatoes, seasonal vegetables and rich gravy",
            bg=self.card_bg,
            fg=self.text_soft,
            font=("Arial", 10),
            anchor="w",
            justify="left",
            wraplength=650
        ).pack(anchor="w", pady=(8, 0))

        right = tk.Frame(special_card, bg=self.card_bg)
        right.pack(side="right", padx=18, pady=16)

        tk.Label(
            right,
            text="£16.50",
            bg=self.card_bg,
            fg=self.gold,
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 10))

        tk.Button(
            right,
            text="+ Add",
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            font=("Arial", 10, "bold"),
            cursor="hand2",
            command=lambda: self.controller.add_to_order("Sunday Roast Beef", "16 kr")
        ).pack()

    # =========================================================
    # Dedicated Today's Special page
    # =========================================================
    def build_special_page(self):
        for widget in self.special_frame.winfo_children():
            widget.destroy()

        wrapper = tk.Frame(self.special_frame, bg=self.bg_center)
        wrapper.pack(fill="both", expand=True, padx=18, pady=18)

        tk.Label(
            wrapper,
            text="Today's Special",
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
            text="Sunday Roast Beef ✩",
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
            text="Slow-roasted sirloin with Yorkshire pudding, roast potatoes, seasonal vegetables and rich gravy.",
            bg=self.card_bg,
            fg=self.text_soft,
            font=("Arial", 12),
            justify="left",
            wraplength=850
        ).pack(anchor="w", padx=20, pady=(0, 12))

        tags = tk.Frame(special_card, bg=self.card_bg)
        tags.pack(anchor="w", padx=20, pady=(0, 18))

        for text in ["England", "Chef's Choice", "Sunday Classic"]:
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
            text="+ Add to Order",
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            command=lambda: self.controller.add_to_order("Sunday Roast Beef", "16 kr")
        ).pack(side="left")

        tk.Button(
            actions,
            text="Back to Home",
            bg=self.red,
            fg="white",
            activebackground=self.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
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

        header = tk.Frame(self.right_frame, bg=self.bg_right)
        header.pack(fill="x", pady=(14, 0))

        tk.Label(
            header,
            text="Order Summary",
            fg=self.text_main,
            bg=self.bg_right,
            font=("Georgia", 18, "bold")
        ).pack(side="left", padx=16)

        mode_frame = tk.Frame(self.right_frame, bg=self.bg_right)
        mode_frame.pack(fill="x", padx=16, pady=(10, 10))

        tk.Button(
            mode_frame,
            text="Single Order",
            bg=self.green,
            fg="white",
            activebackground=self.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            mode_frame,
            text="Group Order",
            state="disabled",
            disabledforeground=self.text_muted,
            bg=self.bg_right,
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10)
        ).pack(side="left")

        divider = tk.Frame(self.right_frame, bg=self.line, height=1)
        divider.pack(fill="x", padx=0, pady=(4, 8))

        self.order_list = tk.Frame(self.right_frame, bg=self.bg_right)
        self.order_list.pack(fill="both", expand=True, padx=10, pady=8)

        self.total_label = tk.Label(
            self.right_frame,
            text="Total: 0 kr",
            fg=self.gold,
            bg=self.bg_right,
            font=("Arial", 14, "bold")
        )
        self.total_label.pack(anchor="w", padx=16, pady=(6, 10))

        self.place_order_btn = tk.Button(
            self.right_frame,
            text="Place Order",
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
            self.hero_frame.pack(side="top", fill="both", expand=True, padx=18, pady=18)

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

    def call_service(self):
        popup = tk.Toplevel(self.root)
        popup.title("Call Service")
        popup.configure(bg=self.bg_center)
        popup.geometry("320x180")
        popup.resizable(False, False)

        tk.Label(
            popup,
            text="Service has been called.",
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
            padx=20,
            pady=8,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack()

    # =========================================================
    # Order panel updates
    # =========================================================
    def update_order_list(self, order_items, total):
        for widget in self.order_list.winfo_children():
            widget.destroy()

        if not order_items:
            tk.Label(
                self.order_list,
                text="Your order is empty.\nBrowse our menu and add items.",
                fg=self.text_muted,
                bg=self.bg_right,
                font=("Arial", 11),
                justify="center"
            ).pack(expand=True, pady=80)

            self.total_label.config(text="Total: 0 kr")
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

        self.total_label.config(text=f"Total: {total} kr")

    # =========================================================
    # Confirmation page
    # =========================================================
    def show_confirmation_page(self, order_items, total):
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

        summary = "Order Summary:\n\n"
        for item in order_items:
            summary += f"• {item['quantity']} x {item['name']}   ({item['price'] * item['quantity']} kr)\n"
        summary += f"\nTotal: {total} kr"

        self.order_summary_label.config(text=summary)
        self.show_page_container()
        self.hide_hero()
        self.hide_special_container()
        self.hide_sidebar()
        self.confirmation_page.tkraise()

    def go_back_to_menu(self):
        self.navigate_to_page("starters", "Starters")