class OrderRepository:
    def get_order(self):
        raise NotImplementedError

    def save_order(self, order):
        raise NotImplementedError

    def clear_order(self):
        raise NotImplementedError

    def get_tip_percentage(self):
        raise NotImplementedError

    def set_tip_percentage(self, tip_percentage):
        raise NotImplementedError