import tkinter as tk

class Draggable:
    def __init__(self, widget, item_data, drop_target=None, on_drop=None):
        self.widget = widget
        self.item_data = item_data
        self.drop_target = drop_target
        self.on_drop = on_drop

        self.widget.bind("<ButtonPress-1>", self.on_press)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_release)

        self.drag_label = None
        self.offset_x = 0
        self.offset_y = 0

        # Store original drop target bg for visual feedback
        self.drop_target_original_bg = (
            drop_target.cget("bg") if drop_target else None
        )

    def on_press(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

        # Create floating label while dragging
        self.drag_label = tk.Label(
            self.widget.winfo_toplevel(),
            text=self.item_data.get("name", "Item"),
            bg="#d6a34a",
            fg="black",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            relief="solid",
            bd=1
        )
        self.drag_label.place(x=event.x_root, y=event.y_root)

    def on_drag(self, event):
        if not self.drag_label:
            return

        x = event.x_root - self.offset_x
        y = event.y_root - self.offset_y
        self.drag_label.place(x=x, y=y)

        # Optional: highlight drop target when hovering
        if self.drop_target:
            x_root = event.x_root
            y_root = event.y_root
            x1 = self.drop_target.winfo_rootx()
            y1 = self.drop_target.winfo_rooty()
            x2 = x1 + self.drop_target.winfo_width()
            y2 = y1 + self.drop_target.winfo_height()
            if x1 <= x_root <= x2 and y1 <= y_root <= y2:
                self.drop_target.config(bg="#3b2d25")  # highlight color
            else:
                self.drop_target.config(bg=self.drop_target_original_bg)

    def on_release(self, event):
        if self.drag_label:
            self.drag_label.destroy()
            self.drag_label = None

        # Reset drop target background
        if self.drop_target:
            self.drop_target.config(bg=self.drop_target_original_bg)

        # Trigger drop callback if dropped inside target
        if self.drop_target and self.on_drop:
            x_root = event.x_root
            y_root = event.y_root
            x1 = self.drop_target.winfo_rootx()
            y1 = self.drop_target.winfo_rooty()
            x2 = x1 + self.drop_target.winfo_width()
            y2 = y1 + self.drop_target.winfo_height()

            if x1 <= x_root <= x2 and y1 <= y_root <= y2:
                self.on_drop(self.item_data)
