import datetime
import matplotlib
import matplotlib.dates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

def main():
    f = open(r"amplitude-data.txt", "r").readlines()
    lst = [(datetime.datetime.strptime(x.split("\t")[0].strip(), "%Y-%m-%d %H:%M:%S.%f"), x.split("\t")[1]) for x in f]
    lst2 = zip(*lst)
    format = matplotlib.dates.DateFormatter('%H:%M')

    dates = matplotlib.dates.date2num(lst2[0])
    matplotlib.use('PDF')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot_date(dates, lst2[1], 'o-', color="red", markerfacecolor='red', markeredgecolor='red', markersize=2, label="Amplitude", rasterized=True)
    plt.legend(["Amplitude"])
    ax.set_ylabel('Maks amplitude')
    ax.set_xlabel('Tidspunkt')
    plt.ylabel('Maks amplitude', rotation="vertical")
    plt.xlabel('Tidspunkt', rotation="horizontal")
    ax.xaxis.set_major_formatter(format)
    ax.autoscale_view()
    ax.grid(True)
    fig.autofmt_xdate()
    plt.savefig(r"amplitude-plot.pdf", dpi=400)

if __name__ == '__main__':
    main()