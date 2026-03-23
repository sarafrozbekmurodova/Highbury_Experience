import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root

        # Main layout frames
        self.left_frame = tk.Frame(root, width=200, bg="#1a1a1a")
        self.center_frame = tk.Frame(root, bg="#2b2b2b")
        self.right_frame = tk.Frame(root, width=250, bg="#1a1a1a")

        self.left_frame.pack(side="left", fill="y")
        self.center_frame.pack(side="left", expand=True, fill="both")
        self.right_frame.pack(side="right", fill="y")

        self.build_left()
        self.build_center()
        self.build_right()

    def build_left(self):
        tk.Label(self.left_frame, text="Categories", fg="white", bg="#1a1a1a").pack(pady=10)

        categories = ["Starters", "Main", "Desserts", "Drinks"]

        for cat in categories:
            tk.Button(self.left_frame, text=cat).pack(fill="x", padx=10, pady=5)

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

        tk.Label(self.right_frame, text="Total: 0 kr", fg="white", bg="#1a1a1a").pack(pady=10)