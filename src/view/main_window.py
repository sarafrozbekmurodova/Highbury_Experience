import tkinter as tk

class MainWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Main layout frames
        self.left_frame = tk.Frame(root, width=200, bg="#1a1a1a")
        self.center_frame = tk.Frame(root, bg="#2b2b2b")
        self.right_frame = tk.Frame(root, width=250, bg="#1a1a1a")

        self.left_frame.pack(side="left", fill="y")
        self.center_frame.pack(side="left", expand=True, fill="both")
        self.right_frame.pack(side="right", fill="y")
        
        # Container for pages (Starters, Main, Desserts, etc.)
        self.page_container = tk.Frame(self.center_frame, bg="#2b2b2b")
        self.page_container.pack(fill="both", expand=True)
       
        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        self.build_left()
        self.build_right()
      
        self.confirmation_page = None

    def build_left(self):
        tk.Label(self.left_frame, text="Categories", fg="white", bg="#1a1a1a",font=("Arial", 12, "bold")).pack(pady=15)

        categories = ["Starters", "Main", "Desserts", "Drinks"]

        for cat in categories:
            btn = tk.Button(
                self.left_frame,
                text=cat,
                bg="#3a3a3a",
                fg="white",
                activebackground="#4a4a4a",
                relief="flat",
                height=2
            )
            btn.pack(fill="x", padx=12, pady=6)
            btn.config(command=lambda c=cat: self.controller.show_page(c.lower()))
    def build_center(self):
        tk.Label(self.center_frame, text="Menu Items", bg="#2b2b2b", fg="white").pack(pady=10)

        for i in range(5):
            frame = tk.Frame(self.center_frame, bg="#3a3a3a")
            frame.pack(fill="x", padx=10, pady=5)

            tk.Label(frame, text=f"Item {i+1}", bg="#3a3a3a", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Add").pack(side="right", padx=10)

    def build_right(self):
        tk.Label(self.right_frame, text="Order", fg="white", bg="#1a1a1a").pack(pady=10)

        self.order_list = tk.Frame(self.right_frame, bg="#1a1a1a")
        self.order_list.pack(fill="both", expand=True)

        self.total_label = tk.Label(self.right_frame, text="Total: 0 kr",
                                    fg="#4ade80", bg="#1a1a1a", font=("Arial", 13, "bold"))
        self.total_label.pack(pady=15)
        # Place Order Button
        self.place_order_btn = tk.Button(
            self.right_frame,
            text="PLACE ORDER",
            bg="#4ade80",
            fg="black",
            font=("Arial", 12, "bold"),
            height=2,
            relief="flat",
            command=self.controller.place_order
        )
        self.place_order_btn.pack(fill="x", padx=15, pady=15)
        
    def show_page(self, page_frame):
        """Raise the requested page to the front (stacked frames technique)"""
        page_frame.tkraise()

    def update_order_list(self, order_items, total):
        for widget in self.order_list.winfo_children():
            widget.destroy()

        if not order_items:
            tk.Label(self.order_list, text="Your order is empty", fg="#888888",
                     bg="#1a1a1a", font=("Arial", 10)).pack(pady=40)
            self.total_label.config(text="Total: 0 kr")
            return

        for i, item in enumerate(order_items):
            item_frame = tk.Frame(self.order_list, bg="#2a2a2a")
            item_frame.pack(fill="x", pady=5, padx=5)

            # Item name
            tk.Label(item_frame, text=item['name'], fg="white", bg="#2a2a2a",
                     anchor="w", font=("Arial", 10)).pack(side="left", padx=10, fill="x", expand=True)

            # Quantity controls
            qty_frame = tk.Frame(item_frame, bg="#2a2a2a")
            qty_frame.pack(side="left", padx=8)

            minus_btn = tk.Button(qty_frame, text="−", width=3,
                                  bg="#1f1f1f",          # darker background
                                  fg="#4ade80",          # green color (visible)
                                  activebackground="#333333",
                                  activeforeground="#4ade80",
                                  relief="flat",
                                  font=("Arial", 12, "bold"),
                                  command=lambda idx=i: self.controller.change_quantity(idx, -1))
            minus_btn.pack(side="left", padx=1)

            # Quantity number
            tk.Label(qty_frame, text=str(item['quantity']), bg="#2a2a2a", fg="#4ade80",
                     width=4, font=("Arial", 12, "bold")).pack(side="left")

            # Plus button - Dark background + Bright color
            plus_btn = tk.Button(qty_frame, text="+", width=3,
                                 bg="#1f1f1f",           # darker background
                                 fg="#4ade80",           # green color
                                 activebackground="#333333",
                                 activeforeground="#4ade80",
                                 relief="flat",
                                 font=("Arial", 12, "bold"),
                                 command=lambda idx=i: self.controller.change_quantity(idx, 1))
            plus_btn.pack(side="left", padx=1)

            # Item total price
            item_total = item['price'] * item['quantity']
            tk.Label(item_frame, text=f"{item_total} kr", fg="#4ade80", bg="#2a2a2a",
                     font=("Arial", 11, "bold")).pack(side="left", padx=15)

            # Delete button
            delete_btn = tk.Button(item_frame, text="×", fg="#ff5555", bg="#2a2a2a",
                                   font=("Arial", 14, "bold"), width=3, relief="flat",
                                   command=lambda idx=i: self.controller.remove_from_order(idx))
            delete_btn.pack(side="right", padx=8)

        self.total_label.config(text=f"Total: {total} kr")

    # ==================== New: Confirmation Page ====================
    def show_confirmation_page(self, order_items, total):
        """Create and show a simple thank you / confirmation page"""
        if self.confirmation_page is None:
            self.confirmation_page = tk.Frame(self.page_container, bg="#2b2b2b")
            self.confirmation_page.grid(row=0, column=0, sticky="nsew")

            tk.Label(self.confirmation_page, text="Thank You!",
                     font=("Arial", 24, "bold"), fg="#4ade80", bg="#2b2b2b").pack(pady=50)

            tk.Label(self.confirmation_page, text="Your order has been placed successfully.",
                     font=("Arial", 14), fg="white", bg="#2b2b2b").pack(pady=10)

            self.order_summary_label = tk.Label(self.confirmation_page, text="",
                                               font=("Arial", 11), fg="#aaaaaa", bg="#2b2b2b", justify="left")
            self.order_summary_label.pack(pady=20, padx=40)

            tk.Button(self.confirmation_page, text="Back to Menu", bg="#3a3a3a", fg="#aaaaaa",
                      font=("Arial", 12), width=20, height=2, relief="flat",
                      command=self.go_back_to_menu).pack(pady=30)

        # Update summary text
        summary = "Order Summary:\n\n"
        for item in order_items:
            summary += f"• {item['quantity']} x {item['name']}   ({item['price'] * item['quantity']} kr)\n"
        summary += f"\nTotal: {total} kr"

        self.order_summary_label.config(text=summary)

        # Show the confirmation page
        self.confirmation_page.tkraise()

    def go_back_to_menu(self):
        """Return to the starters page (or first available page)"""
        if "starters" in self.controller.pages:
            self.show_page(self.controller.pages["starters"])
