from preprocessing import CompanyMaster
from hist_plot import histogram_auth_cap_plot
from bar_plot_year import barplot_by_year_plot
from top_registrations import top_registrations_plot
from group_plot import grouped_bar_plot
import csv

filename = "Data_Gov_Maharashtra.CSV"
fields = []
dataset = []
with open(filename, 'r', encoding='latin1') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        dataset.append(row)

companyMaster = CompanyMaster(dataset)
while True:
    print("Select the Below option for:")
    val = input('''
        Problem 1 press 1
        Problem 2 press 2
        Problem 3 press 3
        Problem 4 press 4
        Quit press q
    ''')
    if val == '1':
        auth_cap = companyMaster.histogram_auth_cap()
        histogram_auth_cap_plot(auth_cap)
    elif val == '2':
        data = companyMaster.barplot_by_year()
        barplot_by_year_plot(data[0], data[1])
    elif val == '3':
        data = companyMaster.top_registrations()
        top_registrations_plot(data[0], data[1])
    elif val == '4':
        data = companyMaster.grouped_bar()
        grouped_bar_plot(data[0], data[1], data[2], data[3])
    elif val == 'q':
        print("Thank You!")
        break
