import tkinter as tk


class OrderPanel:
    """
    Order summary panel component.

    The name "OrderPanel" reflects its role as the right-hand panel that shows
    the current order, subtotal, tip, total, and order-related actions.

    Responsibilities:
    - render the current order summary,
    - display subtotal, tip, and total,
    - provide tip-selection controls,
    - enable quantity changes and item removal,
    - manage the place-order action and confirmation popup.

    The OrderPanel is a view component. It displays order state and delegates
    order actions to the controller.
    """

    def __init__(self, parent, main_window, controller):
        """
        Initialize the order panel component.

        :param parent: Parent Tk container in which the panel is placed
        :param main_window: Reference to the MainWindow instance for styling and UI state
        :param controller: Main controller handling order-related actions
        """
        self.parent = parent
        self.main_window = main_window
        self.controller = controller

        self.frame = tk.Frame(
            self.parent,
            width=320,
            bg=self.main_window.bg_right
        )
        self.frame.pack(side="right", fill="y")
        self.frame.pack_propagate(False)

        self.tip_buttons = {}
        self.order_list = None
        self.subtotal_label = None
        self.tip_amount_label = None
        self.total_label = None
        self.place_order_btn = None

        self.build()

    def build(self):
        """
        Build or rebuild the full order panel UI.

        This method:
        - clears previous widgets,
        - rebuilds the summary header,
        - creates order mode and tip controls,
        - creates totals labels,
        - creates the place-order button,
        - updates button state based on current order contents.
        """
        for widget in self.frame.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]

        header = tk.Frame(self.frame, bg=self.main_window.bg_right)
        header.pack(fill="x", pady=(14, 0))

        tk.Label(
            header,
            text=t["order_summary"],
            fg=self.main_window.text_main,
            bg=self.main_window.bg_right,
            font=("Georgia", 18, "bold")
        ).pack(side="left", padx=16)

        mode_frame = tk.Frame(self.frame, bg=self.main_window.bg_right)
        mode_frame.pack(fill="x", padx=16, pady=(10, 10))

        tk.Button(
            mode_frame,
            text=t["single_order"],
            bg=self.main_window.green,
            fg="white",
            activebackground=self.main_window.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=12,
            pady=6,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            mode_frame,
            text=t["group_order"],
            state="disabled",
            disabledforeground=self.main_window.text_muted,
            bg=self.main_window.bg_right,
            relief="flat",
            bd=0,
            highlightthickness=0,
            takefocus=False,
            padx=12,
            pady=6,
            font=("Arial", 10)
        ).pack(side="left")

        tip_frame = tk.Frame(self.frame, bg=self.main_window.bg_right)
        tip_frame.pack(fill="x", padx=16, pady=(0, 10))

        no_tip_btn = tk.Button(
            tip_frame,
            text="No Tip",
            bg=self.main_window.green,
            fg="white",
            activebackground=self.main_window.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10, "bold"),
            cursor="hand2",
            command=lambda: self.set_tip_mode(0.0)
        )
        no_tip_btn.pack(side="left", padx=(0, 8))

        ten_tip_btn = tk.Button(
            tip_frame,
            text="10% Tip",
            bg=self.main_window.bg_right,
            fg=self.main_window.text_soft,
            activebackground=self.main_window.green,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            font=("Arial", 10),
            cursor="hand2",
            command=lambda: self.set_tip_mode(0.10)
        )
        ten_tip_btn.pack(side="left")

        self.tip_buttons = {
            0.0: no_tip_btn,
            0.10: ten_tip_btn
        }

        divider = tk.Frame(self.frame, bg=self.main_window.line, height=1)
        divider.pack(fill="x", padx=0, pady=(4, 8))

        self.order_list = tk.Frame(self.frame, bg=self.main_window.bg_right)
        self.order_list.pack(fill="both", expand=True, padx=10, pady=8)

        totals_divider = tk.Frame(self.frame, bg=self.main_window.line, height=1)
        totals_divider.pack(fill="x", padx=16, pady=(8, 10))

        self.subtotal_label = tk.Label(
            self.frame,
            text=t["sub_total"] + ": 0 kr",
            fg=self.main_window.text_soft,
            bg=self.main_window.bg_right,
            font=("Arial", 11)
        )
        self.subtotal_label.pack(anchor="w", padx=16, pady=(0, 2))

        self.tip_amount_label = tk.Label(
            self.frame,
            text=t["tip"] + ": 0 kr",
            fg=self.main_window.text_soft,
            bg=self.main_window.bg_right,
            font=("Arial", 11)
        )
        self.tip_amount_label.pack(anchor="w", padx=16, pady=(0, 2))

        self.total_label = tk.Label(
            self.frame,
            text=t["total"] + ": 0 kr",
            fg=self.main_window.gold,
            bg=self.main_window.bg_right,
            font=("Arial", 14, "bold")
        )
        self.total_label.pack(anchor="w", padx=16, pady=(0, 10))

        self.place_order_btn = tk.Button(
            self.frame,
            text=t["place_order"],
            bg=self.main_window.green,
            fg="white",
            disabledforeground="#d7e6dc",
            activebackground=self.main_window.green_hover,
            activeforeground="white",
            font=("Arial", 12, "bold"),
            height=2,
            relief="flat",
            bd=0,
            command=self.show_order_confirmation,
            cursor="hand2"
        )
        self.place_order_btn.pack(fill="x", padx=16, pady=(0, 16))

        self.update_place_order_button()

    def set_tip_mode(self, tip_percentage):
        """
        Set the active tip percentage and refresh tip button highlighting.

        :param tip_percentage: Tip percentage as a decimal value
        """
        self.controller.set_tip_percentage(tip_percentage)
        self.update_tip_buttons(tip_percentage)

    def update_tip_buttons(self, active_tip_percentage):
        """
        Update the visual state of the tip selection buttons.

        :param active_tip_percentage: Currently selected tip percentage
        """
        for tip_value, btn in self.tip_buttons.items():
            if tip_value == active_tip_percentage:
                btn.config(
                    bg=self.main_window.green,
                    fg="white",
                    activebackground=self.main_window.green_hover,
                    activeforeground="white",
                    font=("Arial", 10, "bold")
                )
            else:
                btn.config(
                    bg=self.main_window.bg_right,
                    fg=self.main_window.text_soft,
                    activebackground=self.main_window.green,
                    activeforeground="white",
                    font=("Arial", 10)
                )

    def update_place_order_button(self):
        """
        Enable or disable the place-order button depending on whether the order is empty.
        """
        if self.place_order_btn is None:
            return

        try:
            order_items, subtotal = self.controller.order_service.get_order_summary()

            if len(order_items) > 0:
                self.place_order_btn.config(
                    state="normal",
                    bg=self.main_window.green,
                    fg="white"
                )
            else:
                self.place_order_btn.config(
                    state="disabled",
                    bg="#5c4a42",
                    disabledforeground="#d7e6dc"
                )
        except Exception as e:
            print(f"[DEBUG] Error updating button: {e}")
            self.place_order_btn.config(
                state="disabled",
                bg="#5c4a42",
                disabledforeground="#d7e6dc"
            )

    def show_order_confirmation(self):
        """
        Show a confirmation popup before placing the order.

        If the user confirms, the controller is asked to place the order.
        """
        try:
            order_items, subtotal = self.controller.order_service.get_order_summary()
        except Exception as e:
            print(f"[DEBUG] Could not read order summary: {e}")
            return

        if len(order_items) == 0:
            return

        popup = tk.Toplevel(self.main_window.root)
        popup.title("Confirm Order")
        popup.configure(bg=self.main_window.bg_center)
        popup.geometry("420x240")
        popup.resizable(False, False)
        popup.transient(self.main_window.root)
        popup.grab_set()

        tk.Label(
            popup,
            text="Confirm your order",
            bg=self.main_window.bg_center,
            fg=self.main_window.text_main,
            font=("Georgia", 18, "bold")
        ).pack(pady=(25, 10))

        tk.Label(
            popup,
            text="Are you sure you want to place this order?",
            bg=self.main_window.bg_center,
            fg=self.main_window.text_soft,
            font=("Arial", 11)
        ).pack(pady=(0, 20))

        button_row = tk.Frame(popup, bg=self.main_window.bg_center)
        button_row.pack(pady=20)

        tk.Button(
            button_row,
            text="Cancel",
            command=popup.destroy,
            bg=self.main_window.red,
            fg="white",
            activebackground=self.main_window.red_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side="left", padx=8)

        def confirm_and_place():
            popup.destroy()
            self.controller.place_order()

        tk.Button(
            button_row,
            text="Confirm",
            command=confirm_and_place,
            bg=self.main_window.green,
            fg="white",
            activebackground=self.main_window.green_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side="left", padx=8)

    def update_order_list(self, order_items, subtotal, total, tip_percentage):
        """
        Rebuild the visible order list and totals.

        :param order_items: Current ordered items
        :param subtotal: Order subtotal before tip
        :param total: Order total including tip
        :param tip_percentage: Active tip percentage
        """
        for widget in self.order_list.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]
        self.update_tip_buttons(tip_percentage)

        tip_amount = total - subtotal

        if not order_items:
            tk.Label(
                self.order_list,
                text=t["empty_order"],
                fg=self.main_window.text_muted,
                bg=self.main_window.bg_right,
                font=("Arial", 11),
                justify="center"
            ).pack(expand=True, pady=80)

            self.subtotal_label.config(text=f"{t['sub_total']}: 0 kr")
            self.tip_amount_label.config(text=f"{t['tip']}: 0 kr")
            self.total_label.config(text=f"{t['total']}: 0 kr")
            self.update_place_order_button()
            return

        for item in order_items:
            item_frame = tk.Frame(
                self.order_list,
                bg=self.main_window.card_bg,
                highlightbackground=self.main_window.card_border,
                highlightthickness=1
            )
            item_frame.pack(fill="x", pady=6, padx=4)

            top_row = tk.Frame(item_frame, bg=self.main_window.card_bg)
            top_row.pack(fill="x", padx=10, pady=(8, 4))

            name_key = item.get("name_key")
            display_name = self.controller.t(name_key) if name_key else item["name"]

            tk.Label(
                top_row,
                text=display_name,
                fg=self.main_window.text_main,
                bg=self.main_window.card_bg,
                anchor="w",
                font=("Arial", 11, "bold")
            ).pack(side="left", fill="x", expand=True)

            delete_btn = tk.Button(
                top_row,
                text="×",
                fg="#ff7a7a",
                bg=self.main_window.card_bg,
                activebackground=self.main_window.card_bg,
                activeforeground="#ff9a9a",
                font=("Arial", 14, "bold"),
                width=2,
                relief="flat",
                bd=0,
                highlightthickness=0,
                takefocus=False,
                cursor="hand2",
                command=lambda item_id=item["item_id"]: self.controller.remove_from_order(item_id)
            )
            delete_btn.pack(side="right")

            bottom_row = tk.Frame(item_frame, bg=self.main_window.card_bg)
            bottom_row.pack(fill="x", padx=10, pady=(0, 10))

            qty_frame = tk.Frame(bottom_row, bg=self.main_window.card_bg)
            qty_frame.pack(side="left")

            minus_btn = tk.Button(
                qty_frame,
                text="−",
                width=3,
                bg="#1f1a17",
                fg=self.main_window.green,
                activebackground="#2b2521",
                activeforeground=self.main_window.green,
                relief="flat",
                bd=0,
                font=("Arial", 12, "bold"),
                cursor="hand2",
                command=lambda item_id=item["item_id"]: self.controller.change_quantity(item_id, -1)
            )
            minus_btn.pack(side="left", padx=2)

            tk.Label(
                qty_frame,
                text=str(item["quantity"]),
                bg=self.main_window.card_bg,
                fg=self.main_window.text_main,
                width=3,
                font=("Arial", 11, "bold")
            ).pack(side="left", padx=4)

            plus_btn = tk.Button(
                qty_frame,
                text="+",
                width=3,
                bg="#1f1a17",
                fg=self.main_window.green,
                activebackground="#2b2521",
                activeforeground=self.main_window.green,
                relief="flat",
                bd=0,
                font=("Arial", 12, "bold"),
                cursor="hand2",
                command=lambda item_id=item["item_id"]: self.controller.change_quantity(item_id, 1)
            )
            plus_btn.pack(side="left", padx=2)

            item_total = item["price"] * item["quantity"]

            tk.Label(
                bottom_row,
                text=f"{item_total} kr",
                fg=self.main_window.gold,
                bg=self.main_window.card_bg,
                font=("Arial", 11, "bold")
            ).pack(side="right")

        self.subtotal_label.config(text=f"{t['sub_total']}: {subtotal} kr")
        self.tip_amount_label.config(text=f"{t['tip']}: {tip_amount} kr")
        self.total_label.config(text=f"{t['total']}: {total} kr")
        self.update_place_order_button()