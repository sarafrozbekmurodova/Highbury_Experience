from view.pages.menu_category_page import MenuCategoryPage


class SetMealsPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        set_meals_items = [
            ("2-Course Meal", 199, "Starter + Main Course", "set_meal_2.jpg"),
            ("3-Course Meal", 249, "Starter + Main + Dessert", "set_meal_3.jpg"),
            ("Family Bundle", 399, "2 mains + 2 desserts + drinks", "family_meal.jpg"),
        ]

        super().__init__(parent, controller, title="Set Meals", items=set_meals_items)