from datetime import datetime

from dateutil.relativedelta import relativedelta

total_value = 1_000_000
loan_date = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
final_date = loan_date + delta_years

date_installment = []
date_loan_installment = loan_date
while date_loan_installment < final_date:
    date_installment.append(date_loan_installment)
    date_loan_installment += relativedelta(months=1)

number_installment = len(date_installment)
installment_value = total_value / number_installment
total_paid = 0
count = 1
for date in date_installment:
    total_paid += installment_value
    print(f'{date} | Total paid: {total_paid:,.2f} | Installment: {count}')
    count += 1
