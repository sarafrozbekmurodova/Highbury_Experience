from view.pages.menu_category_page import MenuCategoryPage

class LightCoursesPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        light_items = [
            {"name_key": "caesar_salad", "desc_key": "caesar_salad_desc", "price": 95, "image": "caesar_salad.jpg"},
            {"name_key": "tomato_soup", "desc_key": "tomato_soup_desc", "price": 85, "image": "tomato_soup.jpg"},
            {"name_key": "chicken_wrap", "desc_key": "chicken_wrap_desc", "price": 105, "image": "chicken_wrap.jpg"},
            {"name_key": "avocado_toast", "desc_key": "avocado_toast_desc", "price": 89, "image": "avocado_toast.jpg"},
            {"name_key": "mini_fish_chips", "desc_key": "mini_fish_chips_desc", "price": 110, "image": "fish_chips.jpg"},
        ]

        super().__init__(parent, controller, light_items, category_key="light_courses")
