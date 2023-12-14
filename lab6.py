fixed_price = int(input('Введите цену детали: '))
time = int(input('Введите время работы станка часах : '))
class Stanok:
    def __init__(self, productivity, cost, average_price):
        self.productivity = productivity
        self.cost = cost
        self.average_price = average_price

    def quantity_for_payback(self):
        return self.cost / self.average_price

    def payback_time(self, fixed_price):
        return self.cost / (fixed_price * self.productivity)


class FrezernyStanok(Stanok):
    def __init__(self, productivity, cost, average_price, DetailMass):
        super().__init__(productivity, cost, average_price)
        self.DetailMass = DetailMass

    def massOfDetails(self):
        return time* self.productivity * self.DetailMass


class StanokChPU(Stanok):
    def __init__(self, productivity, cost, average_price, power):
        super().__init__(productivity, cost, average_price)
        self.power = power

    def detail_amount(self, time):
        return self.productivity * time


frezerny_stanok = FrezernyStanok(60, 90000, 20, 150)
stanok_chpu = StanokChPU(200, 10**6, 25, 7.5)
print(f' Количество деталей для окупаемости фрезерного станка: {frezerny_stanok.quantity_for_payback()} шт.')
print(f' Количество деталей для окупаемости станка ЧПУ: {stanok_chpu.quantity_for_payback()} шт.')
print(f' Время окупаемости станка ЧПУ при фиксированной цене детали {fixed_price}: \
{stanok_chpu.payback_time(fixed_price)} часов')
print(f' Количество деталей выпущенное на станке с ЧПУ за {time} часов :{stanok_chpu.detail_amount(time)} шт.')
print(f' Общая масса деталей выпущенных на фрезерном станке за {time} часов: {frezerny_stanok.massOfDetails()} кг.')
