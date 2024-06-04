from typing import Dict, List


class Calculate:
    """Вот класс который будет хранить в себе логику вычислений.
    Частично перенесу то, что у тебя там есть, но концепция такая, что именно эта сущность отвечает
    за все вычисления"""
    koef_for_calculate_destruction = 1000  # у тебя везде по коду это 1000 s1 = round((n1 * 1000) / 160, 1)
    koef_for_calculate_destruction_2 = 160  # у тебя по коду это 160 но че это за коефициент не знаю s1 = round((n1 * 1000) / 160, 1)

    metal_parameters = {
        3: {"left_value": 380, "right_value": 490},
        9: {"left_value": 490, "right_value": None}
        # то как я сделал не правильно но я думаю там не бывает больше ляма значение а так можно чтобы вызывались
        # а так можно чтобы вызывались разные методы но мне впадлу
    }

    def __init__(self, metal_type: int):
        # В todo писал про аннотации metal_type: int - это оно
        #  pass - это затычка когда не знаешь как определить
        self.metal_type = metal_type

    def calculate_resist(self, time_resist_values) -> Dict:
        """Calculate time resist.
        пока сделаю на args если временных сопротивлений может быть только 3, тогда сделай массив
        в todo написал про args kwargs"""
        #  Пока time resist я так и не понял что за сопротивление
        for resist_index in range(len(time_resist_values)):
            time_resist_values[resist_index] = round((time_resist_values[resist_index] *
                                                      self.koef_for_calculate_destruction) /
                                                     self.koef_for_calculate_destruction_2, 1)
        middle_value = round(sum(time_resist_values) / len(time_resist_values), 1)
        string_response = self.check_norm(middle_value=middle_value)

        return {"result": time_resist_values, "string_response": string_response}

    def check_norm(self, middle_value: float) -> str:
        condition = self.metal_parameters.get(self.metal_type)
        if condition is None:
            raise ValueError("Марки такой стали не существует или для нее не определны кондиции")
        if None not in condition.values():
            if condition["left_value"] >= middle_value and middle_value <= condition["right_value"]:
                return self.get_string(**condition)  # TODO все та же работа с kwargs
        elif condition["left_value"] >= middle_value:
            return self.get_string(**condition)

    @staticmethod
    def get_string(**kwargs) -> str:
        """TODO **kwargs почти тоже самое что args"""
        str_out_with_all_condition = "Временное сопротивление норма: {} - {} \n годен \n Угол загиба 80 градусов"
        str_out_with_right_condition = "Временное сопротивление норма: более {} \n годен \n Угол загиба 120 градусов"
        if kwargs.get("right_value") is None:
            return str_out_with_all_condition.format(kwargs.get("left_value"), kwargs.get("right_value"))
        return str_out_with_right_condition.format(kwargs.get("left_value"), kwargs.get("right_value"))
