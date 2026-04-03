from view.pages.menu_category_page import MenuCategoryPage

class SetMealsPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        set_meals_items = [
            {"name_key": "2_course_meal", "desc_key": "2_course_meal_desc", "price": 199, "image": "set_meal_2.jpg"},
            {"name_key": "3_course_meal", "desc_key": "3_course_meal_desc", "price": 249, "image": "set_meal_3.jpg"},
            {"name_key": "family_bundle", "desc_key": "family_bundle_desc", "price": 399, "image": "family_meal.jpg"},
        ]

        super().__init__(parent, controller, set_meals_items, category_key="set_meals")
