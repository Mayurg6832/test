import matplotlib.pyplot as plt


def histogram_auth_cap_plot(auth_cap):
    plt.figure()
    plt.hist(auth_cap, color="skyblue", edgecolor="dodgerblue")
    plt.xticks(
        [1, 2, 3, 4, 5],
        ["<= 1L", "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
    )
    plt.xlabel("Authorized Capital")
    plt.title("Histogram of Authorized Cap")
    plt.show()
