import tkinter as tk


class Sidebar:
    """
    Sidebar represents the left-hand menu navigation panel in the main window.

    This component is responsible for:
    - rendering the menu category buttons,
    - rebuilding its content when the language changes,
    - notifying the main window when the user navigates to a category page,
    - visually highlighting the currently selected category.

    The Sidebar does not own the navigation state itself. Instead, it reflects
    the current state stored in MainWindow.
    """

    def __init__(self, parent, main_window, controller):
        """
        Initialize the sidebar component.

        Parameters:
            parent: The parent Tk container in which the sidebar is placed.
            main_window: Reference to the MainWindow instance that owns the UI state.
            controller: Reference to the main controller of the application.

        This constructor creates the sidebar frame, initializes the internal
        button registry, and builds the initial sidebar content.
        """
        self.parent = parent
        self.main_window = main_window
        self.controller = controller

        self.frame = tk.Frame(
            self.parent,
            width=210,
            bg=self.main_window.bg_sidebar
        )
        self.frame.pack(side="left", fill="y")
        self.frame.pack_propagate(False)

        self.buttons = {}

        self.build()

    def build(self):
        """
        Build or rebuild the sidebar content.

        This method:
        - clears the existing sidebar widgets,
        - retrieves translated labels for the active language,
        - creates one button per menu category,
        - stores buttons by stable internal category key,
        - reapplies the current highlight after rebuilding.

        Using stable internal keys instead of translated labels ensures that
        the highlight state survives language switching correctly.
        """
        for widget in self.frame.winfo_children():
            widget.destroy()

        t = self.main_window.translations[self.main_window.current_language]

        tk.Label(
            self.frame,
            text=t["menu"],
            fg=self.main_window.text_main,
            bg=self.main_window.bg_sidebar,
            font=("Georgia", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(22, 18))

        categories = [
            (t["starters"], "starters"),
            (t["light_courses"], "light_courses"),
            (t["main_courses"], "main"),
            (t["set_meals"], "set_meals"),
            (t["desserts"], "desserts"),
            (t["beverages"], "drinks"),
        ]

        self.buttons = {}

        for label, key in categories:
            btn = tk.Button(
                self.frame,
                text=label,
                bg=self.main_window.bg_sidebar,
                fg=self.main_window.text_soft,
                activebackground=self.main_window.green,
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=18,
                pady=12,
                font=("Arial", 11),
                cursor="hand2",
                command=lambda p=key, s=key: self.main_window.navigate_to_page(p, s)
            )
            btn.pack(fill="x", padx=14, pady=4)
            self.buttons[key] = btn

        self.update_highlight(self.main_window.current_sidebar_selection)

    def update_highlight(self, selected_label):
        """
        Update the visual highlight of the sidebar buttons.

        Parameters:
            selected_label: The stable internal key of the currently selected
                            sidebar category.

        The selected button is rendered using the active highlight style, while
        all other buttons are reset to the default sidebar style.
        """
        for label, btn in self.buttons.items():
            if label == selected_label:
                btn.config(
                    bg=self.main_window.green,
                    fg="white",
                    activebackground=self.main_window.green_hover,
                    activeforeground="white",
                    font=("Arial", 11, "bold")
                )
            else:
                btn.config(
                    bg=self.main_window.bg_sidebar,
                    fg=self.main_window.text_soft,
                    activebackground=self.main_window.green,
                    activeforeground="white",
                    font=("Arial", 11)
                )