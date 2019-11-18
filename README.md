**_ Case 1 Calcuating present value _**
Assuming our user would like to know the downpayment amount with provided kwargs below;
terms, period and interest amount rate.
Price - (presentValue\*_N _ Repay Amount ) = Down payment

**_ Case 2 Calculating the future value _**
Assuming our user pays at the end of the given period, so our program should accumulate the value with gthe iven interest rate;
Accumulated Down payment(1+i)**N = Accumulated Price(1+i)**N - (AccumulatedValue\*_N _ Repay Amount)

**_ Case 3 Calculating The Down Payment with Given Time Value _**
Assuming our user wants to calculate the downpayment with the given period of time
Accumulated Down payment = Accumulated Price ** T -(presentValue \* Repay Amount ) ** T- (AccumulatedValue \* Repay Amount)**-(N+T) / (1+i)**T
