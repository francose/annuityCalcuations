"""
Dr.Debananda Chakraborty
Sadik Erisen
John Stulich
Financial Math

*** Case 1 Calcuating present value ***
Assuming our user would like to know the downpayment amount with provided kwargs below;
terms, period and interest amount rate.
Price - (presentValue**N * Repay Amount ) = Down payment

*** Case 2 Calculating the future value ***
Assuming our user pays at the end of the given period, so our program should accumulate the value with gthe iven interest rate;
Accumulated Down payment(1+i)**N = Accumulated Price(1+i)**N - (AccumulatedValue**N * Repay Amount)


*** Case 3 Calculating The Down Payment with Given Time Value ***
Assuming our user wants to calculate the downpayment with the given period of time
Accumulated Down payment = Accumulated Price ** T -(presentValue * Repay Amount ) ** T- (AccumulatedValue * Repay Amount)**-(N+T) / (1+i)**T

"""
from typing import Callable, List
from abc import ABC, abstractclassmethod, abstractmethod
from fractions import Fraction


class CalculateDownPayment(ABC):

    def __init__(self, interestRate: int, nominalInterestTerms: int, year: int, annuityRepays: int, price: int) -> int:
        try:
            self.interestRate = interestRate
            self.nominalInterestTerms = nominalInterestTerms
            self.year = year
            self.annuityRepays = annuityRepays
            self.price = price
            super(CalculateDownPayment, self).__init__()
        except AttributeError as e:
            print(e)

    @abstractmethod
    def execute(self):
        return self.__init__()


class PresentValue(CalculateDownPayment):
    def execute(self):
        i = (self.interestRate / 100) / self.nominalInterestTerms
        period = self.nominalInterestTerms * self.year
        downpayment = self.price - \
            (self.annuityRepays * ((1-(1+i)**-period)/i))
        return (downpayment)


class AccumulatedValue(CalculateDownPayment):
    def execute(self):
        i = (self.interestRate / 100) / self.nominalInterestTerms
        period = self.nominalInterestTerms * self.year
        downpayment = ((self.price * (1+i)**period) -
                       (self.annuityRepays * (((1+i)**period)-1)/i))/(1+i)**period
        return (downpayment)


class CalculateGivenTime(CalculateDownPayment):
    def execute(self, T):
        i = (self.interestRate / 100) / self.nominalInterestTerms
        period = self.nominalInterestTerms * self.year
        downpayment = ((self.price * (1+i)**T) -
                       (self.annuityRepays * (((1+i)**T)-1)/i) - (self.annuityRepays * ((1-(1+i)**-(period-T))/i)))/(1+i)**T
        return (downpayment)


def main(InterestRate, effectiveInterestTerms, fixedPeriod, repayAmount, price, GivenTime) -> int:

    presentValue = PresentValue(
        InterestRate, effectiveInterestTerms, fixedPeriod, repayAmount, price)
    accumulatedValue = AccumulatedValue(
        InterestRate, effectiveInterestTerms, fixedPeriod, repayAmount, price)
    calculateGivenTime = CalculateGivenTime(
        InterestRate, effectiveInterestTerms, fixedPeriod, repayAmount, price)

    return {"PresentValue": presentValue.execute(), "AccumulatedValue": accumulatedValue.execute(), "GivenTimeCalculation": calculateGivenTime.execute(GivenTime)}


if __name__ == "__main__":

    result = main(18, 12, 4, 250, 10000, 24)
    print("\n\n\n\n", result, "\n\n\n\n")
