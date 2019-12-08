### Calcuating present value

**_Assuming our user would like to know the downpayment amount with provided kwargs below;_**

###### Logic

> terms, period and interest amount rate.
> Price - (presentValue\* _N _ Repay Amount ) = Down payment

### Calculating the future value

**_Assuming our user pays at the end of the given period, so our program should accumulate the value with gthe iven interest rate;_**

###### Logic

> Accumulated Down payment(1+i)**N = Accumulated Price(1+i)**N - (AccumulatedValue\*_N _ Repay Amount)

### Calculating The Down Payment with Given Time Value

**_Assuming our user wants to calculate the downpayment with the given period of time_**

###### Logic

> Accumulated Down payment = Accumulated Price ** T -(presentValue \* Repay Amount ) ** T- (AccumulatedValue \* Repay Amount)**-(N+T) / (1+i)**T
