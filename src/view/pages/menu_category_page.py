import tkinter as tk
from PIL import Image, ImageTk
import os

class MenuCategoryPage(tk.Frame):
    def __init__(self, parent, controller, items, category_key):
        super().__init__(parent, bg="#221a16")
        self.controller = controller
        self.main_window = getattr(controller, "main_window", None)

        self.items = items
        self.category_key = category_key
        self.images = {}

        default_items = [
            {
                "name_key": "grilled_salmon",
                "desc_key": "grilled_salmon_desc",
                "price": 189,
                "image": "grilled_salmon.jpg"
            },
            {
                "name_key": "beef_burger",
                "desc_key": "beef_burger_desc",
                "price": 145,
                "image": "beef_burger.jpg"
            },
            {
                "name_key": "chicken_parmesan",
                "desc_key": "chicken_parmesan_desc",
                "price": 165,
                "image": "chicken_parmesan.jpg"
            },
            {
                "name_key": "vegetable_stir_fry",
                "desc_key": "vegetable_stir_fry_desc",
                "price": 135,
                "image": "vegetable_stir_fry.jpg"
            },
            {
                "name_key": "ribeye_steak",
                "desc_key": "ribeye_steak_desc",
                "price": 229,
                "image": "ribeye_steak.jpg"
            },
            {
                "name_key": "pasta_carbonara",
                "desc_key": "pasta_carbonara_desc",
                "price": 155,
                "image": "pasta_carbonara.jpg"
            },
        ]
        if hasattr(controller, "t") and callable(controller.t):
            self.t = controller.t
        else:
            self.t = lambda key: key
        self.title_key = category_key
        self.build_page()
        
    
    def build_page(self):
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

            name = self.t(item["name_key"])
            desc = self.t(item["desc_key"])
            price = item["price"]
            img_filename = item["image"]

            item_frame = tk.Frame(
                self,
                bg="#33261f",
                highlightbackground="#4a352b",
                highlightthickness=1
            )

            item_frame.pack(fill="x", padx=20, pady=10)
            # ---------- CARD HOVER EFFECT ----------
            # Hover functions
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

                self.images[f"{name}_small"] = small
                self.images[f"{name}_large"] = large

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
                command=lambda n=name, p=price: self.controller.add_to_order(n, p)
            )
            add_btn.pack()
            def btn_enter(e):
                add_btn.config(bg="#379567")

            def btn_leave(e):
                add_btn.config(bg="#2d7d57")

            add_btn.bind("<Enter>", btn_enter)
            add_btn.bind("<Leave>", btn_leave)
            
            for child in item_frame.winfo_children():
                child.bind("<Enter>", on_card_enter, add="+")
                child.bind("<Leave>", on_card_leave, add="+")

    def refresh_language(self, lang):
        self.build_page()
