class MenuRepository:
    """Abstract menu repository (interface-like)"""

    def get_main_courses(self):
        raise NotImplementedError

    def get_starters(self):
        raise NotImplementedError

    def get_desserts(self):
        raise NotImplementedError

    def get_drinks(self):
        raise NotImplementedError