import datetime
import matplotlib
import matplotlib.dates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

def main():
    f = open(r"amplitude-data.txt", "r").readlines()
    lst = [(datetime.datetime.strptime(x.split("\t")[0].strip(), "%Y-%m-%d %H:%M:%S.%f"), x.split("\t")[1]) for x in f]
    lst = [x for x in lst if x[0] >= datetime.datetime(2015, 4, 22, 19, 6, 14) and x[0] <= datetime.datetime(2015, 4, 23, 9, 0, 0)]
    lst2 = zip(*lst)
    format = matplotlib.dates.DateFormatter('%H:%M')

    dates = matplotlib.dates.date2num(lst2[0])
    matplotlib.use('PDF')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot_date(dates, lst2[1], 'o-', color="red", markerfacecolor='red', markeredgecolor='red', markersize=2, label="Amplitude", rasterized=True)
    plt.legend(["Amplitude"])
    ax.set_ylabel('Max amplitude')
    ax.set_xlabel('Tidspunkt')
    plt.ylabel('Max amplitude', rotation="vertical")
    plt.xlabel('Tidspunkt', rotation="horizontal")
    ax.xaxis.set_major_formatter(format)
    ax.autoscale_view()
    ax.grid(True)
    fig.autofmt_xdate()
    plt.savefig(r"amplitude-plot-ingen-snorken.pdf", dpi=400)

if __name__ == '__main__':
    main()