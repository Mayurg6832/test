import matplotlib.pyplot as plt


def grouped_bar_plot(year_x, year_y, pba_x, pba_y):
    width = 0.35
    plt.figure(figsize=(13, 5))
    plt.bar(year_x, year_y, width=width,
            color='skyblue', edgecolor='dodgerblue')
    plt.bar(pba_x, pba_y, width=width, color='lightpink', edgecolor='deeppink')
    plt.legend(["Year", "Principle Buisness Activity"])
    plt.title("Grouped Bar Plot")
    plt.xlabel("Year of registration/Principle Buisness Activity")
    plt.ylabel("Registrations")
    plt.xticks(range(17))
    plt.show()
