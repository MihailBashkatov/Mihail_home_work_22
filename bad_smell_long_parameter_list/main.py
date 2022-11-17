# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    speed = 1

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    @classmethod
    def get_fly_speed(cls):
        return cls.speed * 1.2

    @classmethod
    def get_crawl_speed(cls):
        return cls.speed * 0.5

    def fly_direction_up(self):
        self.y += self.get_fly_speed()
        return self.x, self.y

    def fly_direction_down(self):
        self.y -= self.get_fly_speed()
        return self.x, self.y

    def fly_direction_left(self):
        self.x -= self.get_fly_speed()
        return self.x, self.y

    def fly_direction_right(self):
        self.x += self.get_fly_speed()
        return self.x, self.y

    def crawl_direction_up(self):
        self.y += self.get_crawl_speed()
        return self.x, self.y

    def crawl_direction_down(self):
        self.y -= self.get_crawl_speed()
        return self.x, self.y

    def crawl_direction_left(self):
        self.x -= self.get_crawl_speed()
        return self.x, self.y

    def crawl_direction_right(self):
        self.x += self.get_crawl_speed()
        return self.x, self.y