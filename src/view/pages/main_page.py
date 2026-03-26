import tkinter as tk
from PIL import Image, ImageTk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2b2b2b")
        self.controller = controller
        self.images = {}

        tk.Label(self, text="Main Course", bg="#2b2b2b", fg="white",
                 font=("Arial", 18, "bold")).pack(pady=20)

        main_items = [
            ("Grilled Salmon", "189 kr", "With lemon butter sauce, asparagus & potatoes", "grilled_salmon.jpg"),
            ("Beef Burger", "145 kr", "Premium beef, cheddar, bacon & fries", "beef_burger.jpg"),
            ("Chicken Parmesan", "165 kr", "Breaded chicken, marinara & mozzarella", "chicken_parmesan.jpg"),
            ("Vegetable Stir Fry", "135 kr", "Mixed vegetables, tofu & teriyaki", "vegetable_stir_fry.jpg"),
            ("Ribeye Steak", "229 kr", "250g steak with garlic butter", "ribeye_steak.jpg"),
            ("Pasta Carbonara", "155 kr", "Classic Italian with pancetta", "pasta_carbonara.jpg"),
        ]

        for name, price, desc, img_filename in main_items:
            item_frame = tk.Frame(self, bg="#3a3a3a")
            item_frame.pack(fill="x", padx=20, pady=10)

            # Image
            try:
                img_path = f"assets/images/{img_filename}"
                pil_img = Image.open(img_path).resize((120, 90), Image.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)
                self.images[name] = tk_img

                img_label = tk.Label(item_frame, image=tk_img, bg="#3a3a3a")
                img_label.pack(side="left", padx=10, pady=10)
            except Exception:
                tk.Label(item_frame, text="📸", font=("Arial", 40), bg="#3a3a3a", fg="#555").pack(side="left", padx=20, pady=10)

            # Info
            info_frame = tk.Frame(item_frame, bg="#3a3a3a")
            info_frame.pack(side="left", fill="x", expand=True, padx=10, pady=10)

            tk.Label(info_frame, text=name, bg="#3a3a3a", fg="white",
                     font=("Arial", 11, "bold"), anchor="w").pack(fill="x")
            tk.Label(info_frame, text=desc, bg="#3a3a3a", fg="#aaaaaa",
                     font=("Arial", 9), anchor="w").pack(fill="x")

            # Price + Add
            right_frame = tk.Frame(item_frame, bg="#3a3a3a")
            right_frame.pack(side="right", padx=15)

            tk.Label(right_frame, text=price, bg="#3a3a3a", fg="#4ade80",
                     font=("Arial", 12, "bold")).pack(pady=8)

            add_btn = tk.Button(right_frame, text="Add", bg="#4ade80", fg="black",
                                font=("Arial", 10, "bold"), width=10, relief="flat")
            add_btn.pack(pady=5)
            add_btn.config(command=lambda n=name, p=price: self.controller.add_to_order(n, p))
