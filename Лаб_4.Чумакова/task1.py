if __name__ == "__main__":
    class ReinforcedConcrete:
        """ Базовый класс железобетона. """

        def __init__(self, name: str,  frost_resistance: float, water_resistance: float) -> None:
            self.name = name
            self.frost_resistance = frost_resistance
            self.water_resistance = water_resistance

        def __str__(self):
            return f"Класс бетона на сжатие: {self.name}. Марка морозостойкости бетона: {self.frost_resistance}. " \
                   f"Марка водонепроницаемости бетона: {self.water_resistance}\n"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, frost_resistance={self.frost_resistance!r})"


    class Prestressed(ReinforcedConcrete):
        """ Класс преднапряженных бетонов. Меняется процесс бетонирования, так как внедряется процесс преднапряжения армтуры """

        def __init__(self, name: str, name_steel: str, stress_resistance: str) -> None:
            super().__init__(name, stress_resistance)
            self.name_steel = name_steel

        def __str__(self):
            return f"Класс бетона на сжатие: {self.name}. Степень преднапряжения: {self.stress_resistance}. " \
                   f"Марка стали: {self.name_steel}\n"

        def producing_time(self, name: str, stress_resistance: str):
            """ Функция выдает сроки изготовления преднапряженных бетонных деталей в заводских условиях """
            ...


    class Сast_in_situ(ReinforcedConcrete):
        """ Класс железобетонов, изготовляемых на площадке """

        def __init__(self, name: str, name_steel: str, situ_conditions: str) -> None:
            super().__init__(name, name_steel)
            self.situ_conditions = situ_conditions

        def __str__(self):
            return f"Класс бетона на сжатие: {self.name}. Марка стали: {self.name_steel}. " \
                   f"Условия стройплощадки: {self.situ_conditions}\n"

        def machine_choice(self, name: str, name_steel: str, situ_conditions: str,
                                type_of_detail: str):
            """ Подбор машин, необходимых бля бетонирования в условиях стройплощадки """
            ...


    example_1 = ReinforcedConcrete("B25", 350.0, 7.0)
    print(example_1.__str__())
    print(example_1.__repr__())

    pass
