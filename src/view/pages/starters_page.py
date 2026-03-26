import tkinter as tk

class StartersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2b2b2b")
        self.controller = controller

        # Title
        tk.Label(
            self,
            text="Starters",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # Sample starters data (you can later move this to model/data)
        starters = [
            ("Classic Bruschetta", "48 kr", "Toasted bread with tomatoes, garlic & basil"),
            ("Caesar Salad", "65 kr", "Romaine, parmesan, croutons & caesar dressing"),
            ("Garlic Bread with Cheese", "39 kr", "Freshly baked with mozzarella"),
            ("Soup of the Day", "52 kr", "Ask staff for today's special"),
            ("Fried Calamari", "89 kr", "With lemon aioli and marinara sauce"),
        ]

        for name, price, desc in starters:
            item_frame = tk.Frame(self, bg="#3a3a3a", relief="flat")
            item_frame.pack(fill="x", padx=20, pady=8)

            # Left side: name + description
            left_frame = tk.Frame(item_frame, bg="#3a3a3a")
            left_frame.pack(side="left", fill="x", expand=True, padx=15, pady=10)

            tk.Label(left_frame, text=name, bg="#3a3a3a", fg="white", font=("Arial", 11, "bold"), anchor="w").pack(fill="x")
            tk.Label(left_frame, text=desc, bg="#3a3a3a", fg="#aaaaaa", font=("Arial", 9), anchor="w").pack(fill="x")

            # Right side: price + Add button
            right_frame = tk.Frame(item_frame, bg="#3a3a3a")
            right_frame.pack(side="right", padx=10)

            tk.Label(right_frame, text=price, bg="#3a3a3a", fg="#4ade80", font=("Arial", 11, "bold")).pack(pady=5)

            add_btn = tk.Button(
                right_frame,
                text="Add",
                bg="#4ade80",
                fg="black",
                font=("Arial", 10, "bold"),
                width=10,
                relief="flat"
            )
            add_btn.pack(pady=5)

            # Connect button
            add_btn.config(command=lambda n=name, p=price: self.controller.add_to_order(n, p))
