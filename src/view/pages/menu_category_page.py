import tkinter as tk
from PIL import Image, ImageTk


class MenuCategoryPage(tk.Frame):
    def __init__(self, parent, controller, title="Main Courses", items=None):
        super().__init__(parent, bg="#221a16")
        self.controller = controller
        self.title = title
        self.images = {}

        default_items = [
            ("Grilled Salmon", 189, "With lemon butter sauce, asparagus & potatoes", "grilled_salmon.jpg"),
            ("Beef Burger", 145, "Premium beef, cheddar, bacon & fries", "beef_burger.jpg"),
            ("Chicken Parmesan", 165, "Breaded chicken, marinara & mozzarella", "chicken_parmesan.jpg"),
            ("Vegetable Stir Fry", 135, "Mixed vegetables, tofu & teriyaki", "vegetable_stir_fry.jpg"),
            ("Ribeye Steak", 229, "250g steak with garlic butter", "ribeye_steak.jpg"),
            ("Pasta Carbonara", 155, "Classic Italian with pancetta", "pasta_carbonara.jpg"),
        ]

        self.items = items if items is not None else default_items

        self.build_page()

    def build_page(self):
        tk.Label(
            self,
            text=self.title,
            bg="#221a16",
            fg="#f5efe8",
            font=("Georgia", 22, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

        tk.Label(
            self,
            text="Choose from our selection and add items to your order.",
            bg="#221a16",
            fg="#c8b8aa",
            font=("Arial", 10)
        ).pack(anchor="w", padx=20, pady=(0, 12))

        for name, price, desc, img_filename in self.items:
            item_frame = tk.Frame(
                self,
                bg="#33261f",
                highlightbackground="#4a352b",
                highlightthickness=1
            )
            item_frame.pack(fill="x", padx=20, pady=10)

            image_wrapper = tk.Frame(item_frame, bg="#33261f")
            image_wrapper.pack(side="left", padx=10, pady=10)

            try:
                img_path = f"assets/images/{img_filename}"
                pil_img = Image.open(img_path).resize((120, 90), Image.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)
                self.images[name] = tk_img

                img_label = tk.Label(image_wrapper, image=tk_img, bg="#33261f")
                img_label.pack()
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
                text="Add",
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