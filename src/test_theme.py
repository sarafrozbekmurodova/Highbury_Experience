import tkinter as tk
from components.button import StyledButton
from theme.theme_manager import ThemeManager


def main():
    root = tk.Tk()
    root.title("Theme Test")
    root.geometry("400x300")

    theme = ThemeManager.get_instance().get_theme()

    root.configure(bg=theme.background.get("root", "#000"))

    # Buttons (IMPORTANT: use Label, not Button)
    btn1 = tk.Label(root, text="Primary")
    btn1.pack(pady=10)

    btn2 = tk.Label(root, text="Danger")
    btn2.pack(pady=10)

    btn3 = tk.Label(root, text="Large Button")
    btn3.pack(pady=10)

    # Apply styles
    StyledButton(btn1, variant="primary", command=lambda: print("Primary"))
    StyledButton(btn2, variant="danger", command=lambda: print("Danger"))
    StyledButton(btn3, variant="primary", size="lg")

    root.mainloop()


if __name__ == "__main__":
    main()