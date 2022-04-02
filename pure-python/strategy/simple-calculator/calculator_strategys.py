from strategy_interface import StrategyInterface


class Sum(StrategyInterface):
    @staticmethod
    def calculate(a, b):
        return a + b


class Subtract(StrategyInterface):
    @staticmethod
    def calculate(a, b):
        return a - b


class Divide(StrategyInterface):
    @staticmethod
    def calculate(a, b):
        return a / b


class Multiply(StrategyInterface):
    @staticmethod
    def calculate(a, b):
        return a * b
