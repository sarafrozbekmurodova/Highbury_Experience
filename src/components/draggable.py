import tkinter as tk

class Draggable:
    def __init__(self, widget, item_data, drop_target, on_drop):
        self.widget = widget
        self.item_data = item_data
        self.drop_target = drop_target
        self.on_drop_callback = on_drop

        self.ghost = None

        self._bind_events()

    def _bind_events(self):
        self.widget.bind("<Button-1>", self._start_drag)
        self.widget.bind("<B1-Motion>", self._on_drag)
        self.widget.bind("<ButtonRelease-1>", self._on_drop)

    def _start_drag(self, event):
        root = self.widget.winfo_toplevel()

        self.ghost = tk.Label(
            root,
            text=self.widget.cget("text"),
            bg="lightyellow",
            bd=1,
            relief="solid",
            padx=10,
            pady=5
        )

        self.ghost.lift()

        x = event.x_root - root.winfo_rootx()
        y = event.y_root - root.winfo_rooty()

        self.ghost.place(x=x, y=y)

    def _on_drag(self, event):
        if not self.ghost:
            return

        root = self.widget.winfo_toplevel()

        x = event.x_root - root.winfo_rootx()
        y = event.y_root - root.winfo_rooty()

        self.ghost.place(x=x + 5, y=y + 5)

    def _on_drop(self, event):
        if not self.ghost:
            return

        x = event.x_root
        y = event.y_root

        target = self.widget.winfo_toplevel().winfo_containing(x, y)

        if self._is_inside_target(target):
            self.on_drop_callback(self.item_data)

        self.ghost.destroy()
        self.ghost = None

    def _is_inside_target(self, widget):
        while widget:
            if widget == self.drop_target:
                return True
            widget = widget.master
        return False