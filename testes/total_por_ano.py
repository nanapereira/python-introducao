from datetime import datetime, timedelta

totals = {
    2009: 0,
    2010: 0,
    2011: 0,
    2012: 0,
    2013: 0,
    2014: 0,
    2015: 0,
}

def check_signature_interval(info, year_start_date, year_end_date):
    try:
        start_str_date = info[8]
        start_date = datetime.strptime(start_str_date, "%d/%m/%Y")

        if year_end_date > start_date > year_start_date:
            return 1
    except Exception as e:
        pass

    return 0

with open("data/data/ExecucaoFinanceira.csv", "r") as data:
    for line in data:
        data_splitada = line.strip().split(";")
        ano = int(data_splitada[8].split('/')[-1])
        if ano in totals:
            data_inicial = datetime(ano, 1, 1)
            ano_final = data_inicial + timedelta(days=365)
            totals[ano] += check_signature_interval(data_splitada, data_inicial, ano_final)

for year, signed in totals.items():
    print("{} execucoes assinadas em {}".format(signed, year))