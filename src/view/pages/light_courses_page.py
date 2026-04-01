from view.pages.menu_category_page import MenuCategoryPage


class LightCoursesPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        light_items = [
            ("Caesar Salad", "95 kr", "Crisp romaine, parmesan, croutons & Caesar dressing", "caesar_salad.jpg"),
            ("Tomato Soup", "85 kr", "Creamy tomato soup with basil & bread", "tomato_soup.jpg"),
            ("Chicken Wrap", "105 kr", "Grilled chicken, salad & garlic sauce", "chicken_wrap.jpg"),
            ("Avocado Toast", "89 kr", "Sourdough with smashed avocado & chili flakes", "avocado_toast.jpg"),
            ("Mini Fish & Chips", "110 kr", "Light portion with tartar sauce", "fish_chips.jpg"),
        ]

        super().__init__(parent, controller, title="Light Courses", items=light_items)