"""
Reusable menu category page.

This page renders a list of menu items for a specific category, such as
starters, desserts, drinks, or light courses. It supports translated text,
image display, add-to-order actions, and drag-and-drop interaction.
"""

import tkinter as tk
from PIL import Image, ImageTk
from components.draggable import Draggable


class MenuCategoryPage(tk.Frame):
    """
    Generic page used to display menu items for a single category.

    Responsibilities:
    - Render category title and optional subtitle
    - Display menu item cards with image, description, and price
    - Support add-to-order actions
    - Support drag-and-drop ordering
    - Rebuild itself when the language changes
    """

    def __init__(self, parent, controller, items, category_key):
        """
        Initialize the category page.

        :param parent: Parent Tkinter container
        :param controller: Main application controller
        :param items: Collection of menu items to display
        :param category_key: Translation key for the category title
        """
        super().__init__(parent, bg="#221a16")
        self.controller = controller
        self.main_window = getattr(controller, "main_window", None)

        self.items = items
        self.category_key = category_key
        self.images = {}

        if hasattr(controller, "t") and callable(controller.t):
            self.t = controller.t
        else:
            self.t = lambda key: key

        self.title_key = category_key
        self.build_page()

    def _get_item_value(self, item, key, default=None):
        """
        Return a value from either a dictionary-based or object-based menu item.

        :param item: Menu item as dict or object
        :param key: Field name to retrieve
        :param default: Default value if missing
        :return: Retrieved value or default
        """
        if isinstance(item, dict):
            return item.get(key, default)
        return getattr(item, key, default)

    def _build_order_item_data(self, item, translated_name, price):
        """
        Build normalized order-item data for the order system.

        :param item: Original menu item
        :param translated_name: Display name in the active language
        :param price: Item price
        :return: Dictionary representing the order item
        """
        item_id = (
            self._get_item_value(item, "item_id")
            or self._get_item_value(item, "name_key")
            or translated_name
        )

        name_key = self._get_item_value(item, "name_key")

        return {
            "item_id": item_id,
            "name_key": name_key,
            "name": translated_name,
            "price": price
        }

    def build_page(self):
        """
        Build or rebuild the full category page UI.
        """
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(
            self,
            text=self.t(self.title_key),
            bg="#221a16",
            fg="#f5efe8",
            font=("Georgia", 22, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

        subtitle_key = f"{self.category_key}_subtitle"
        subtitle_text = self.t(subtitle_key)
        if subtitle_text != subtitle_key:
            tk.Label(
                self,
                text=subtitle_text,
                bg="#221a16",
                fg="#c8b8aa",
                font=("Arial", 10)
            ).pack(anchor="w", padx=20, pady=(0, 12))

        for item in self.items:
            name_key = self._get_item_value(item, "name_key")
            desc_key = self._get_item_value(item, "desc_key")
            price = self._get_item_value(item, "price")
            img_filename = self._get_item_value(item, "image")

            name = self.t(name_key) if name_key else self._get_item_value(item, "name", "Unnamed item")
            desc = self.t(desc_key) if desc_key else self._get_item_value(item, "description", "")

            item_frame = tk.Frame(
                self,
                bg="#33261f",
                highlightbackground="#4a352b",
                highlightthickness=1
            )
            item_frame.pack(fill="x", padx=20, pady=10)

            order_item_data = self._build_order_item_data(item, name, price)

            Draggable(
                widget=item_frame,
                item_data=order_item_data,
                drop_target=self.main_window.right_frame,
                on_drop=self._on_item_dropped
            )

            def on_card_enter(e, frame=item_frame):
                frame.config(
                    bg="#3b2d25",
                    highlightbackground="#d6a34a"
                )

            def on_card_leave(e, frame=item_frame):
                frame.config(
                    bg="#33261f",
                    highlightbackground="#4a352b"
                )

            item_frame.bind("<Enter>", on_card_enter)
            item_frame.bind("<Leave>", on_card_leave)

            image_wrapper = tk.Frame(item_frame, bg="#33261f")
            image_wrapper.pack(side="left", padx=10, pady=10)

            try:
                img_path = f"data/images/{img_filename}"
                base_img = Image.open(img_path)

                small = ImageTk.PhotoImage(base_img.resize((120, 90), Image.LANCZOS))
                large = ImageTk.PhotoImage(base_img.resize((140, 105), Image.LANCZOS))

                image_key_base = order_item_data["item_id"]
                self.images[f"{image_key_base}_small"] = small
                self.images[f"{image_key_base}_large"] = large

                img_label = tk.Label(image_wrapper, image=small, bg="#33261f")
                img_label.pack()

                def img_enter(e, lbl=img_label, img=large):
                    lbl.config(image=img)

                def img_leave(e, lbl=img_label, img=small):
                    lbl.config(image=img)

                img_label.bind("<Enter>", img_enter)
                img_label.bind("<Leave>", img_leave)

            except Exception:
                tk.Label(
                    image_wrapper,
                    text="📸",
                    font=("Arial", 36),
                    bg="#33261f",
                    fg="#8d7f74",
                    width=5,
                    height=3
                ).pack()

            info_frame = tk.Frame(item_frame, bg="#33261f")
            info_frame.pack(side="left", fill="x", expand=True, padx=10, pady=12)

            tk.Label(
                info_frame,
                text=name,
                bg="#33261f",
                fg="#f5efe8",
                font=("Arial", 12, "bold"),
                anchor="w"
            ).pack(fill="x")

            tk.Label(
                info_frame,
                text=desc,
                bg="#33261f",
                fg="#c8b8aa",
                font=("Arial", 9),
                anchor="w",
                justify="left",
                wraplength=450
            ).pack(fill="x", pady=(4, 0))

            right_frame = tk.Frame(item_frame, bg="#33261f")
            right_frame.pack(side="right", padx=15, pady=12)

            tk.Label(
                right_frame,
                text=f"{price} kr",
                bg="#33261f",
                fg="#d6a34a",
                font=("Arial", 12, "bold")
            ).pack(pady=(0, 8))

            add_btn = tk.Button(
                right_frame,
                text=self.t("add"),
                bg="#2d7d57",
                fg="white",
                activebackground="#379567",
                activeforeground="white",
                font=("Arial", 10, "bold"),
                width=10,
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda data=order_item_data: self.controller.add_to_order(data)
            )
            add_btn.pack()

            def btn_enter(e, button=add_btn):
                button.config(bg="#379567")

            def btn_leave(e, button=add_btn):
                button.config(bg="#2d7d57")

            add_btn.bind("<Enter>", btn_enter)
            add_btn.bind("<Leave>", btn_leave)

            for child in item_frame.winfo_children():
                child.bind("<Enter>", on_card_enter, add="+")
                child.bind("<Leave>", on_card_leave, add="+")

    def refresh_language(self, lang=None):
        """
        Rebuild the page when the active language changes.

        :param lang: Optional language code, currently unused
        """
        self.build_page()

    def _on_item_dropped(self, item_data):
        """
        Handle an item being dropped onto the order area.

        :param item_data: Normalized order item data
        """
        if self.controller:
            self.controller.add_to_order(item_data)