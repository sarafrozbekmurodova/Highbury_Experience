import tkinter as tk
from components.draggable import Draggable
from theme.theme_manager import ThemeManager


class DragDropTestPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.theme = ThemeManager.get_instance().get_theme()

        self._build_ui()
        self._render_order()

    def _build_ui(self):
        self.root.configure(bg=self.theme.background.get("root"))

        self.container = tk.Frame(
            self.root,
            bg=self.theme.background.get("main")
        )
        self.container.pack(fill="both", expand=True)

        self.menu_frame = tk.Frame(
            self.container,
            bg=self.theme.background.get("sidebar"),
            width=300
        )
        self.menu_frame.pack(side="left", fill="y")

        self.order_frame = tk.Frame(
            self.container,
            bg=self.theme.background.get("center")
        )
        self.order_frame.pack(side="right", fill="both", expand=True)

        title = tk.Label(
            self.menu_frame,
            text="Drag Menu",
            bg=self.theme.background.get("sidebar"),
            fg=self.theme.text.get("main"),
            font=("Arial", 16)
        )
        title.pack(pady=10)

        items = self.controller.menu_service.menu_repository.get_all()

        for item in items:
            self._create_menu_item(item)

    def _create_menu_item(self, item):
        label = tk.Label(
            self.menu_frame,
            text=f"{item['name_key']} ({item['price']} kr)",
            bg=self.theme.card.get("bg"),
            fg=self.theme.text.get("main"),
            bd=1,
            relief="solid",
            padx=10,
            pady=5
        )
        label.pack(pady=8, padx=10, fill="x")

        item_data = {
            "item_id": item["item_id"],
            "name": item["name_key"],
            "price": item["price"]
        }

        Draggable(
            widget=label,
            item_data=item_data,
            drop_target=self.order_frame,
            on_drop=self._handle_drop
        )

    def _handle_drop(self, item_data):
        self.controller.add_to_order(item_data)
        self._render_order()


    def _render_order(self):
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        items, total = self.controller.order_service.get_order_summary()

        for item in items:
            label = tk.Label(
                self.order_frame,
                text=f"{item['name']} - {item['price']} kr x{item['quantity']}",
                bg=self.theme.card.get("bg"),
                fg=self.theme.text.get("main"),
                padx=10,
                pady=5
            )
            label.pack(anchor="w", padx=10, pady=5)

        total_label = tk.Label(
            self.order_frame,
            text=f"Total: {total} kr",
            bg=self.theme.background.get("center"),
            fg=self.theme.text.get("main"),
            font=("Arial", 14)
        )
        total_label.pack(pady=10)