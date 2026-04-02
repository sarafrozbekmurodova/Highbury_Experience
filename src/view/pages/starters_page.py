from view.pages.menu_category_page import MenuCategoryPage


class StartersPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        self.raw_data = [
            {
                "en_name": "Classic Bruschetta",
                "sv_name": "Klassisk Bruschetta",
                "price": 48,
                "en_desc": "Toasted bread with tomatoes & basil",
                "sv_desc": "Rostat surdegsbröd med tomat, basilika och balsamico",
                "image": "bruschetta.jpg"
            },
            {
                "en_name": "Caesar Salad",
                "sv_name": "Caesarsallad",
                "price": 65,
                "en_desc": "Romaine, parmesan & croutons",
                "sv_desc": "Romainsallad, parmesan, krutonger och caesardressing",
                "image": "caesar_salad.jpg"
            },
            {
                "en_name": "Garlic Bread with Cheese",
                "sv_name": "Vitlöksbröd med Ost",
                "price": 39,
                "en_desc": "Freshly baked with mozzarella",
                "sv_desc": "Nygräddat bröd med vitlökssmör och mozzarella",
                "image": "garlic_bread.jpg"
            },
            {
                "en_name": "Soup of the Day",
                "sv_name": "Dagens Soppa",
                "price": 52,
                "en_desc": "Ask staff for today's special",
                "sv_desc": "Fråga personalen om dagens soppa",
                "image": "soup.jpg"
            },
            {
                "en_name": "Fried Calamari",
                "sv_name": "Friterad Calamari",
                "price": 89,
                "en_desc": "With lemon aioli",
                "sv_desc": "Friterad bläckfisk med citronaioli",
                "image": "calamari.jpg"
            },
        ]
        lang = "EN"
        if hasattr(controller, 'main_window') and hasattr(controller.main_window, 'current_language'):
            lang = controller.main_window.current_language

        title = "Förrätter" if lang == "SV" else "Starters"

        super().__init__(parent, controller, title=title, items=self.raw_data, language=lang)
