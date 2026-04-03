import tkinter as tk

from controller.main_controller import MainController
from service.menu_service import MenuService
from repository.in_memory_menu_repository import InMemoryMenuRepository
from repository.in_memory_order_repository import InMemoryOrderRepository

from drag_drop_test_page import DragDropTestPage


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")

    menu_repo = InMemoryMenuRepository()
    order_repo = InMemoryOrderRepository()

    menu_service = MenuService(menu_repo)

    controller = MainController(
        root=root,
        menu_service=menu_service,
        order_repository=order_repo
    )

    DragDropTestPage(root, controller)

    root.mainloop()