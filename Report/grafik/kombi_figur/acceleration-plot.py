import datetime
import matplotlib
import matplotlib.dates
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

def main():
    f = open(r"accel_raw.csv", "r").readlines()
    lst = [(datetime.datetime.strptime(x.split("\t")[0].strip(), "%Y-%m-%d %H:%M:%S.%f"), x.split("\t")[1]) for x in f]
    lst = [x for x in lst if x[0] >= datetime.datetime(2015, 4, 21, 21, 0, 0) and x[0] <= datetime.datetime(2015, 4, 22, 9, 0, 0)]
    lst2 = list(zip(*lst))
    format = matplotlib.dates.DateFormatter('%H:%M')

    dates = matplotlib.dates.date2num(lst2[0])
    matplotlib.use('PDF')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot_date(dates, lst2[1], 'o-', color="red", markerfacecolor='red', markeredgecolor='red', markersize=2, label="Acceleration X", rasterized=True)
    plt.legend(["Acceleration X"], loc=2)
    plt.ylabel(r'Acceleration i $m/s^{2}$', rotation="vertical")
    plt.xlabel('Tidspunkt', rotation="horizontal")
    ax.xaxis.set_major_formatter(format)
    ax.autoscale_view()
    ax.grid(True)
    fig.autofmt_xdate()
    plt.savefig(r"acceleration-plot.pdf", dpi=400)

if __name__ == '__main__':
    main()