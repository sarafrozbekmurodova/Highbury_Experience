"""
Set meals page implementation.

Defines the set meal menu items and delegates rendering to MenuCategoryPage.
"""

from view.pages.menu_category_page import MenuCategoryPage


class SetMealsPage(MenuCategoryPage):
    """
    Page representing the set meals category.

    This class provides set meal item data and relies on MenuCategoryPage
    for rendering and interaction logic.
    """

    def __init__(self, parent, controller):
        """
        Initialize the set meals page with predefined items.
        """
        set_meals_items = [
            {
                "item_id": "set_2_course_meal",
                "name_key": "2_course_meal",
                "desc_key": "2_course_meal_desc",
                "price": 199,
                "image": "set_meal_2.jpg"
            },
            {
                "item_id": "set_3_course_meal",
                "name_key": "3_course_meal",
                "desc_key": "3_course_meal_desc",
                "price": 249,
                "image": "set_meal_3.jpg"
            },
            {
                "item_id": "set_family_bundle",
                "name_key": "family_bundle",
                "desc_key": "family_bundle_desc",
                "price": 399,
                "image": "family_meal.jpg"
            },
        ]

        super().__init__(
            parent,
            controller,
            set_meals_items,
            category_key="set_meals"
        )