import datetime
import matplotlib
import matplotlib.dates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

def main():
    f = open(r"C:\Users\Mink\Desktop\asd.txt", "r").readlines()
    lst = [(datetime.datetime.strptime(x.split("\t")[0].strip(), "%Y-%m-%d %H:%M:%S.%f"), x.split("\t")[1]) for x in f]
    lst2 = zip(*lst)
    format = matplotlib.dates.DateFormatter('%H:%M')

    dates = matplotlib.dates.date2num(lst2[0])
    matplotlib.use('PDF')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot_date(dates, lst2[1], 'o-', color="red", markerfacecolor='red', markeredgecolor='red', markersize=2, label="Acceleration X", rasterized=True)
    plt.legend(["Acceleration X"])
    ax.xaxis.set_major_formatter(format)
    ax.autoscale_view()
    ax.grid(True)
    fig.autofmt_xdate()
    plt.savefig(r"C:\Users\Mink\Desktop\asd.pdf", dpi=400)

if __name__ == '__main__':
    main()