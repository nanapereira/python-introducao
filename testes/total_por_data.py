from decimal import Decimal
from datetime import datetime, date

total = Decimal('0')
start_date = date(2009, 1, 1)
end_date = date(year=2010, month=1, day=1)

def get_value(info):
    try:
        signature_date = datetime.strptime(info[7], "%d/%m/%Y").date()

        if end_date > signature_date < start_date:
            str_value = info[5]
            value = Decimal(str_value)
            return value
    except Exception as e:
        print(e)
        pass
    return Decimal('0')

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        total += get_value(line.split(';'))

print("Total gasto com assinaturas entre {} e {} : {}".format(start_date, end_date, total))