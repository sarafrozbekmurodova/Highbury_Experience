import tkinter as tk
from view.components.order_panel import OrderPanel
from view.components.menu_panel import Sidebar
from view.components.top_panel import TopPanel

class MainWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.translations = controller.translations
        self.current_language = "EN"

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
        self.top_panel = TopPanel(self.root, self)
        self.top_frame = self.top_panel.frame

        self.body_frame = tk.Frame(self.root, bg=self.bg_main)
        self.body_frame.pack(side="top", fill="both", expand=True)

        # Left panel is now its own component
        self.sidebar = Sidebar(self.body_frame, self, controller)
        self.left_frame = self.sidebar.frame

        self.center_frame = tk.Frame(self.body_frame, bg=self.bg_center)
        self.center_frame.pack(side="left", fill="both", expand=True)

        # Right panel is already its own component
        self.order_panel = OrderPanel(self.body_frame, self, controller)
        self.right_frame = self.order_panel.frame

        # ---------- Center content containers ----------
        self.hero_frame = tk.Frame(self.center_frame, bg=self.bg_center)
        self.page_container = tk.Frame(self.center_frame, bg=self.bg_center)
        self.special_frame = tk.Frame(self.center_frame, bg=self.bg_center)

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        self.confirmation_page = None
        self.special_page = None        

        self.build_top()
        self.build_hero()

        self.update_order_list([], 0, 0, 0.0)
        self.show_home()

    # ====================== LANGUAGE SWITCH ======================
    def switch_language(self, lang):
        if lang == self.current_language:
            return

        self.current_language = lang
        self.build_top()
        self.sidebar.build()
        self.build_hero()
        self.order_panel.build()
        self.build_special_page()

        if self.current_page in self.controller.pages:
            page = self.controller.pages[self.current_page]
            if hasattr(page, "refresh_language"):
                page.refresh_language(lang)
            elif hasattr(page, "build_page"):
                page.build_page()

        if self.current_page == "home":
            self.build_hero()

        if self.current_page == "special":
            self.build_special_page()

        self.controller.refresh_order_panel()

    def refresh_ui(self):
        self.build_top()
        self.sidebar.build()
        self.build_hero()
        self.order_panel.build()
        self.build_special_page()

    # =========================================================
    # Top Bar
    # =========================================================
    def build_top(self):
        self.top_panel.build()



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
            command=lambda: self.navigate_to_page("starters", t["starters"]),
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

        tag_list = (
            ["England", "Kockens Val", "Söndagsklassiker"]
            if self.current_language == "SV"
            else ["England", "Chef's Choice", "Sunday Classic"]
        )

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
            command=lambda: self.controller.add_to_order({
                "item_id": "sunday_roast",
                "name": t["sunday_roast"],
                "price": 16
            })
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
        self.sidebar.update_highlight(self.current_sidebar_selection)

    def update_top_nav_highlight(self, active_name):
        self.top_panel.update_highlight(active_name)    

    def call_service(self):
        popup = tk.Toplevel(self.root)
        popup.title("Call Service")
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
    # Order panel delegation
    # =========================================================
    def update_order_list(self, order_items, subtotal, total, tip_percentage):
        self.order_panel.update_order_list(order_items, subtotal, total, tip_percentage)

    def update_place_order_button(self):
        self.order_panel.update_place_order_button()

    def show_order_confirmation(self):
        self.order_panel.show_order_confirmation()

    def set_tip_mode(self, tip_percentage):
        self.order_panel.set_tip_mode(tip_percentage)

    def update_tip_buttons(self, active_tip_percentage):
        self.order_panel.update_tip_buttons(active_tip_percentage)

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
            display_name = self.controller.t(item["name_key"]) if item.get("name_key") else item["name"]
            summary += f"• {item['quantity']} x {display_name}   ({item['price'] * item['quantity']} kr)\n"

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
        t = self.translations[self.current_language]
        self.navigate_to_page("starters", t["starters"])