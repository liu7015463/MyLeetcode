startingPointOfTaxation = 5000


def totalTax(taxDeterminationAmount, month):
    total = taxDeterminationAmount * month
    result = 0
    if total <= 36000:
        result = total * 0.03
    elif 36000 < total <= 144000:
        result = total * 0.1 - 2520
    elif 144000 < total <= 300000:
        result = total * 0.2 - 16920
    elif 300000 < total <= 420000:
        result = total * 0.25 - 31920
    elif 420000 < total <= 660000:
        result = total * 0.3 - 52920
    elif 660000 < total <= 960000:
        result = total * 0.35 - 85920
    elif 960000 < total:
        result = total * 0.45 - 181920
    return result


def calculate(monthSalary, socialInsurancePremiums, specialAdditions):
    result = []
    paidWithTax = monthSalary - socialInsurancePremiums
    taxDeterminationAmount = paidWithTax - specialAdditions - startingPointOfTaxation

    for month in range(1, 13):
        currentYearTax = totalTax(taxDeterminationAmount, month)
        currentMonthTax = currentYearTax
        if month > 1:
            currentMonthTax = currentYearTax - result[month - 2]['currentYearTax']
        result.append({})
        result[month - 1]['month'] = month
        result[month - 1]['currentYearTax'] = currentYearTax
        result[month - 1]['currentMonthTax'] = currentMonthTax
        result[month - 1]['salary'] = paidWithTax - currentMonthTax

    totalSalary = 0
    for data in result:
        print('%d %.2f %.2f %.2f' % (data['month'], data['currentYearTax'], data['currentMonthTax'], data['salary']))
        totalSalary = totalSalary + data['salary']

    print(totalSalary)


if __name__ == '__main__':
    print('hello')
    calculate(30114.94, 4225, 1000)
