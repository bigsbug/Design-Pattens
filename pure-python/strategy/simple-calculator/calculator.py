from re import A
from strategy_interface import StrategyInterface
import calculator_strategys as strategys


class Calculator:
    strategy: StrategyInterface

    def __init__(self, first_number, second_number) -> None:
        self.first_number = first_number
        self.second_number = second_number

    def calculate(self) -> int:
        """calculating depended on the strategy

        Returns:
            int: result of calculate
        """
        return self.strategy.calculate(self.first_number, self.second_number)


calculator = Calculator(10, 2)
calculator.strategy = strategys.Multiply()
result = calculator.calculate()
print(result)
