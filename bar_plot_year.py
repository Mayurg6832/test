import matplotlib.pyplot as plt


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


def barplot_by_year_plot(years, year_count):

    plt.figure(figsize=(13, 5))
    addlabels(years, year_count)
    plt.bar(years, year_count, color='skyblue', edgecolor='dodgerblue')
    plt.title("Bar Plot of company registration by year")
    plt.xlabel("Years")
    plt.ylabel("Registrations")
    plt.show()
