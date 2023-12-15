from matplotlib import pyplot as plt
from Data import Drawer

def main():
    # Приклад використання класу
    file_path = 'src\lab8\customers-1000.csv'
    drawer = Drawer(file_path)
    drawer.read_data()

# Побудова кругової діаграми кількості користувачів з кожного країни
    plot: plt = drawer.plot_pie_chart('Country')
    # plot.show()
    # drawer.save(plot)

# Побудова стовпчикової діаграми середнього віку користувачів з кожної країни
    drawer.plot_bar_chart('Country', 'Company')#.show()

    drawer.plot_unique_countries_count('Company')#.show()

if __name__ == '__main__':
    main()