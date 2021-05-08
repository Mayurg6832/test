import matplotlib.pyplot as plt


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


def top_registrations_plot(pba, pba_count):
    plt.figure(figsize=(15, 10))
    plt.bar(pba, pba_count, color='skyblue', edgecolor='dodgerblue')
    addlabels(pba, pba_count)
    plt.xticks(rotation='vertical')
    plt.gcf().subplots_adjust(bottom=0.55, top=1)
    plt.title("Top registrations by 'PBA' for the year 2015")
    plt.xlabel("Principal Business Activity")
    plt.ylabel("Registrations")
    plt.show()
