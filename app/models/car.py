class Car:
    def __init__(self, car_id, model, brand, year, available=True):
        self.car_id = car_id
        self.model = model
        self.brand = brand
        self.year = year
        self.available = available