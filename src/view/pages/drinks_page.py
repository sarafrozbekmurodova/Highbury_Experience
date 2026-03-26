import tkinter as tk
from PIL import Image, ImageTk

class DrinksPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2b2b2b")
        self.controller = controller
        self.images = {}

        tk.Label(self, text="Drinks", bg="#2b2b2b", fg="white",
                 font=("Arial", 18, "bold")).pack(pady=20)

        drinks = [
            ("Espresso", "35 kr", "Freshly brewed Italian espresso", "espresso.jpg"),
            ("Cappuccino", "45 kr", "With velvety milk foam", "cappuccino.jpg"),
            ("Fresh Orange Juice", "48 kr", "Freshly squeezed", "orange_juice.jpg"),
            ("House Red Wine", "89 kr", "Glass of Cabernet Sauvignon", "red_wine.jpg"),
            ("House White Wine", "85 kr", "Glass of Chardonnay", "white_wine.jpg"),
            ("Craft Beer", "65 kr", "Local IPA", "beer.jpg"),
            ("Virgin Mojito", "52 kr", "Mint, lime & soda", "mojito.jpg"),
        ]

        for name, price, desc, img_filename in drinks:
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

            # Price + Add button
            right_frame = tk.Frame(item_frame, bg="#3a3a3a")
            right_frame.pack(side="right", padx=15)

            tk.Label(right_frame, text=price, bg="#3a3a3a", fg="#4ade80",
                     font=("Arial", 12, "bold")).pack(pady=8)

            add_btn = tk.Button(right_frame, text="Add", bg="#4ade80", fg="black",
                                font=("Arial", 10, "bold"), width=10, relief="flat")
            add_btn.pack(pady=5)
            add_btn.config(command=lambda n=name, p=price: self.controller.add_to_order(n, p))
