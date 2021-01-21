# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from random import randint, uniform
from collections import defaultdict
from typing import List, Dict, Tuple


def income_evaluator(simulation_mode: bool = False) -> Tuple[float, Dict[str, float]]:

    def get_company_number(simulation_mode: bool = False) -> int:
        number: int = 0
        if simulation_mode:
            number = randint(-1, 9)
        else:
            number = int(input('Введите количество предприятий: '))
        return number

    def get_company_name(i: int, simulation_mode: bool = False) -> str:
        name: str = ''
        if simulation_mode:
            name = 'Company_' + str(i)
        else:
            name = input(f'Введите название предприятия #{i + 1}: ')
        return name

    def get_quarter_income(q: int, simulation_mode: bool = False) -> float:
        income: float = 0
        if simulation_mode:
            income = uniform(-1, 999)
        else:
            income = float(input(f'Введите выручку за квартал #{j + 1} предприятия {company}: '))
        return income

    n: int = get_company_number(simulation_mode)

    while n < 1:
        n: int = get_company_number(simulation_mode)

    annual_statement: Dict[str, float] = defaultdict(float)

    annual_income: float = 0
    total_income: float = 0

    company: str = ''
    income: float = 0

    for i in range(n):
        company = get_company_name(i, simulation_mode)
        annual_income = 0
        for j in range(4):
            income = get_quarter_income(j, simulation_mode)
            annual_income += income
            total_income += income
        annual_statement[company] = annual_income

    average_income: float = total_income / n

    above_average: List[str] = list()
    below_average: List[str] = list()

    if n == 1:
        print(f'Колчество предприятий: {n}.\n'
              f'Невозможно определить предприятия с прибылью выше или ниже средней.\n'
              f'Введите больше предприятий для сравнения.')
    else:
        for company, income in annual_statement.items():
            if income > average_income:
                above_average.append(company)
            elif income < average_income:
                below_average.append(company)
        if len(above_average) > 0 and len(below_average) > 0:
            print(f'Колчество предприятий: {n}')
            print(f'Средняя прибыль: {average_income}')
            print('Компании с прибылью выше средней: {}'.format(', '.join(above_average)))
            print('Компании с прибылью ниже средней: {}'.format(', '.join(below_average)))
        else:
            print(f'Колчество предприятий: {n}.\n'
                  f'Невозможно определить предприятия с прибылью выше или ниже средней.\n'
                  f'Прибыль предприятий совпадает.')
    return average_income, annual_statement


if __name__ == '__main__':
    average_income, annual_statement = income_evaluator(True)
    print(f'Средняя прибыль: {average_income}')
    print(f'Годовая прибыль по каждому предприятию: {annual_statement}')
