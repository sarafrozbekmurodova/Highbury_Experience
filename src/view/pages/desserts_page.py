import tkinter as tk
from PIL import Image, ImageTk

class DessertsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2b2b2b")
        self.controller = controller
        self.images = {}   # Keep references to prevent garbage collection
        self.frames = {}

        tk.Label(self, text="Desserts", bg="#2b2b2b", fg="white",
                 font=("Arial", 18, "bold")).pack(pady=20)

        desserts = [
            ("Chocolate Lava Cake", "75 kr", "Warm chocolate cake with molten center & vanilla ice cream", "chocolate_lava.jpg"),
            ("Tiramisu", "68 kr", "Classic Italian coffee-flavored dessert", "tiramisu.jpg"),
            ("New York Cheesecake", "72 kr", "With strawberry coulis", "cheesecake.jpg"),
            ("Crème Brûlée", "65 kr", "Vanilla custard with caramelized sugar", "creme_brulee.jpg"),
            ("Apple Pie à la Mode", "59 kr", "Warm apple pie served with vanilla ice cream", "apple_pie.jpg"),
            ("Panna Cotta", "62 kr", "With berry compote", "panna_cotta.jpg"),
        ]

        for name, price, desc, img_filename in desserts:
            item_frame = tk.Frame(self, bg="#3a3a3a", bd=0, highlightthickness=0)
            item_frame.pack(fill="x", padx=20, pady=10)

    # CARD HOVER EFFECT
            def card_enter(event, frame=item_frame):
                frame.config(bg="#444444", highlightbackground="#4ade80", highlightthickness=2)

            def card_leave(event, frame=item_frame):
               frame.config(bg="#3a3a3a", highlightthickness=0)

            item_frame.bind("<Enter>", card_enter)
            item_frame.bind("<Leave>", card_leave)

            # Image on the left
            try:
                img_path = f"data/images/{img_filename}"

                # ====================== Pre-generate Animation Frames ======================
                frames = []
                base_img = Image.open(img_path)

                for i in range(7):  # 0 = small, 6 = large (7 frames total)
                    scale = 1.0 + (i * 0.42) / 6      # from 1.0x to 1.42x
                    new_width = int(120 * scale)
                    new_height = int(90 * scale)

                    resized = base_img.resize((new_width, new_height), Image.LANCZOS)
                    tk_frame = ImageTk.PhotoImage(resized)
                    frames.append(tk_frame)

                # Store frames and final small image
                self.frames[name] = frames
                self.images[name] = frames[0]                   # small image
                self.images[f"{name}_large"] = frames[-1]       # large image

                # Create label with initial small image
                img_label = tk.Label(item_frame, image=frames[0], bg="#3a3a3a", bd=0)
                img_label.pack(side="left", padx=12, pady=10)

                # Animation variables
                self.current_frame = {name: 0}

                # ====================== Smooth Hover Animation ======================
                def animate_to(label, item_name, target_frame, step=1):
                    current = self.current_frame[item_name]
                    current += step
                    if step > 0 and current > target_frame:
                        current = target_frame
                    elif step < 0 and current < target_frame:
                        current = target_frame

                    self.current_frame[item_name] = current
                    label.config(image=self.frames[item_name][current])

                    # Continue animation if not reached target
                    if current != target_frame:
                        label.after(25, lambda: animate_to(label, item_name, target_frame, step))

                def on_enter(event, lbl=img_label, item=name):
                    animate_to(lbl, item, target_frame=6, step=1)   # zoom in to max

                def on_leave(event, lbl=img_label, item=name):
                    animate_to(lbl, item, target_frame=0, step=-1)  # zoom out to original

                img_label.bind("<Enter>", on_enter)
                img_label.bind("<Leave>", on_leave)

                # Optional: Add green border on hover
                def on_enter_border(e, lbl=img_label):
                    lbl.config(bd=3, relief="solid", highlightbackground="#4ade80", highlightthickness=3)

                def on_leave_border(e, lbl=img_label):
                    lbl.config(bd=0, relief="flat")

                img_label.bind("<Enter>", on_enter_border, add="+")
                img_label.bind("<Leave>", on_leave_border, add="+")
                

            except Exception as e:
                print(f"Failed to load image {img_filename}: {e}")
                tk.Label(item_frame, text="📸", font=("Arial", 45), bg="#3a3a3a", fg="#555")\
                    .pack(side="left", padx=25, pady=10)

            # Info
            info_frame = tk.Frame(item_frame, bg="#3a3a3a")
            info_frame.pack(side="left", fill="x", expand=True, padx=10, pady=10)

            tk.Label(info_frame, text=name, bg="#3a3a3a", fg="white",
                     font=("Arial", 11, "bold"), anchor="w").pack(fill="x")
            tk.Label(info_frame, text=desc, bg="#3a3a3a", fg="#aaaaaa",
                     font=("Arial", 9), anchor="w").pack(fill="x")

            # Price + Add button
            right_frame = tk.Frame(item_frame, bg="#3a3a3a")
            right_frame.pack(side="right", padx=15)

            tk.Label(right_frame, text=price, bg="#3a3a3a", fg="#4ade80",
                     font=("Arial", 12, "bold")).pack(pady=8)

            add_btn = tk.Button(right_frame, text="Add", bg="#4ade80", fg="black",
                                font=("Arial", 10, "bold"), width=10, relief="flat")
            add_btn.pack(pady=5)
            add_btn.config(command=lambda n=name, p=price: self.controller.add_to_order(n, p))
            for widget in item_frame.winfo_children():
                widget.bind("<Enter>", card_enter)
                widget.bind("<Leave>", card_leave)
