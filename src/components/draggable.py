import tkinter as tk


class Draggable:
    """
    Add drag-and-drop behavior to a Tkinter widget.

    This helper makes a widget draggable and allows it to be dropped onto
    a specific target widget. While dragging, a floating label is shown as
    visual feedback. If the mouse is released inside the drop target, the
    provided callback is triggered with the associated item data.

    Args:
        widget: The Tkinter widget that should become draggable.
        item_data: A dictionary or object containing the dragged item's data
            (for example name, id, and price).
        drop_target: The widget that accepts the drop action, such as the
            order panel. Optional.
        on_drop: Callback function called on a successful drop. The callback
            receives item_data as its argument. Optional.
    """

    def __init__(self, widget, item_data, drop_target=None, on_drop=None):
        """
        Initialize drag-and-drop behavior for the given widget.
        """
        self.widget = widget
        self.item_data = item_data
        self.drop_target = drop_target
        self.on_drop = on_drop

        self.drag_label = None
        self.offset_x = 0
        self.offset_y = 0

        # Store the original background color so hover highlighting can be reset.
        self.drop_target_original_bg = (
            self.drop_target.cget("bg") if self.drop_target else None
        )

        # Bind mouse events to support the full drag-and-drop interaction.
        self.widget.bind("<ButtonPress-1>", self.on_press)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        """
        Start the drag operation.

        Saves the mouse offset relative to the widget and creates a floating
        label that follows the cursor while the item is being dragged.
        """
        self.offset_x = event.x
        self.offset_y = event.y

        item_name = self.item_data.get("name", "Item")

        # Create a floating visual representation of the dragged item.
        self.drag_label = tk.Label(
            self.widget.winfo_toplevel(),
            text=item_name,
            bg="#d6a34a",
            fg="black",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            relief="solid",
            bd=1,
        )

        # Place the label near the cursor.
        self.drag_label.place(
            x=event.x_root - self.offset_x,
            y=event.y_root - self.offset_y,
        )

    def on_drag(self, event):
        """
        Continue the drag operation.

        Moves the floating label with the cursor and highlights the drop target
        when the cursor is inside it.
        """
        if not self.drag_label:
            return

        x = event.x_root - self.offset_x
        y = event.y_root - self.offset_y
        self.drag_label.place(x=x, y=y)

        if self.drop_target:
            self._update_drop_target_highlight(event.x_root, event.y_root)

    def on_release(self, event):
        """
        Complete the drag operation.

        Removes the floating label, resets the drop target styling, and triggers
        the drop callback if the mouse was released inside the drop target.
        """
        if self.drag_label:
            self.drag_label.destroy()
            self.drag_label = None

        self._reset_drop_target_highlight()

        if (
            self.drop_target
            and self.on_drop
            and self._is_inside_drop_target(event.x_root, event.y_root)
        ):
            self.on_drop(self.item_data)

    def _is_inside_drop_target(self, x_root, y_root):
        """
        Return True if the given screen coordinates are inside the drop target.
        """
        if not self.drop_target:
            return False

        x1 = self.drop_target.winfo_rootx()
        y1 = self.drop_target.winfo_rooty()
        x2 = x1 + self.drop_target.winfo_width()
        y2 = y1 + self.drop_target.winfo_height()

        return x1 <= x_root <= x2 and y1 <= y_root <= y2

    def _update_drop_target_highlight(self, x_root, y_root):
        """
        Highlight the drop target when the cursor is hovering over it.
        """
        if self._is_inside_drop_target(x_root, y_root):
            self.drop_target.config(bg="#3b2d25")
        else:
            self._reset_drop_target_highlight()

    def _reset_drop_target_highlight(self):
        """
        Restore the original background color of the drop target.
        """
        if self.drop_target and self.drop_target_original_bg is not None:
            self.drop_target.config(bg=self.drop_target_original_bg)