import datetime
import matplotlib
import matplotlib.dates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import string

def main():
    f = open(r"amplitude_raw.csv", "r").readlines()
    lst = [x.split('\t') for x in f]
    lst = [(datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S.%f"), x[1]) for x in lst]
    lst = [x for x in lst if x[0] >= datetime.datetime(2015, 4, 21, 21, 0, 0) and x[0] <= datetime.datetime(2015, 4, 22, 9, 0, 0)]
    lst2 = list(zip(*lst))
    format = matplotlib.dates.DateFormatter('%H:%M')

    dates = matplotlib.dates.date2num(lst2[0])
    matplotlib.use('PDF')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot_date(dates, lst2[1], 'o-', color="red", markerfacecolor='red', markeredgecolor='red', markersize=2, label="Maks Amplitude", rasterized=True)
    plt.legend(["Maks Amplitude"], loc=2)
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