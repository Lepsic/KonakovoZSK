from calculate.calculate import Calculate
# вот так делаются импорты между файлами


class App:
    """Класс которой является мостиком между твоей логикой и терминалом.
    порядок такой
    класс App опеределяет какой метод нужно вызвать у класса Calculate а класс Calculate уже обращается к Parser
    """
    hi_str = "Hi! \n please input mark metal: "
    request_time_resist = "Please input time resists\n if operation is done input me '/stop' \n"
    stop_input = "/stop"

    def start(self):
        mark_metal = int(input(self.hi_str))
        calculator = Calculate(mark_metal)
        time_resists = []
        while True:
            time_resist = input(self.request_time_resist)
            try:
                value = float(time_resist)
            except ValueError:
                if time_resist == self.stop_input:
                    break
                else:
                    raise ValueError("Что-то не то...")
            time_resists.append(value)

        response = calculator.calculate_resist(time_resist_values=time_resists)
        print(response)


if __name__ == '__main__':
    App().start()