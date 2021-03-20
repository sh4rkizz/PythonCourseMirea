from lxml.html import document_fromstring
from requests import get
import matplotlib.pyplot as plt


def counting_sort(array_to_sort, reverse=False):
    lst = [0] * (max(array_to_sort) + 1)
    for i in array_to_sort:
        lst[i] += 1

    srt = []
    for i in range(len(lst)):
        srt.extend([i] * lst[i])

    if reverse:
        return reversed(srt)
    return srt


def get_db():
    url = 'https://github.com/Newbilius/Old-Games_DOS_Game_Gauntlet/blob/master/GAMES.csv'
    return document_fromstring(get(url).text).xpath('//*[@class="blob-code blob-code-inner js-file-line"]/text()')


def popular_years(text):
    years = [int(line.split(';')[3][1:-1]) for line in text if line[-10:-1] != 'не издана']
    m = min(years)
    lst = [0] * (max(years) + 1 - m)
    for i in years:
        lst[i - m] += 1

    years = counting_sort(set(years))
    out = dict()
    for i in range(len(lst) - 1):
        out.update({years[i]: lst[i]})

    return out


def popular_genres(text):
    genres = [line.split(';')[1][1:-1] for line in text]
    pair = dict()

    for i in list(set(genres)):
        pair.update({i: genres.count(i)})
    return pair


def analyze_db(text):
    return popular_years(text), popular_genres(text)


def graph_analysis(main_list, counter_list, settings):
    if settings['circle_diagram']:
        _, ax1 = plt.subplots(1, figsize=(16, 12))
        ax1.pie(counter_list, shadow=True, autopct='%1.1f%%', pctdistance=0.9, radius=1.25, textprops={'fontsize': 18})
        ax1.legend(fontsize=18, bbox_to_anchor=(-0.013, 1.152), labels=main_list)
        ax1.set_title(settings['name'], y=1.05, fontdict={'fontsize': 25})
        plt.savefig('database_analysis/Popular_game_genres.png', bbox_inches='tight')
        plt.show()
    else:
        plt.plot(main_list, counter_list, label=settings['legend'])
        plt.xlabel(settings['x_axis'], fontsize=13)
        plt.ylabel(settings['y_axis'], fontsize=13)
        plt.title(settings['name'])
        plt.legend()
        plt.grid()
        plt.savefig('database_analysis/Popular_game_dev_years.png', dpi=200, bbox_inches='tight')
        plt.show()


if __name__ == '__main__':
    database = get_db()

    gr_settings = {'name': 'Game dev per year graph',
                   'legend': 'Games per year',
                   'x_axis': 'Years',
                   'y_axis': 'Games',
                   'circle_diagram': False}
    popularity = popular_years(database)
    arg_1 = popularity.keys()
    arg_2 = popularity.values()
    graph_analysis(arg_1, arg_2, gr_settings)

    gr_settings = {'name': 'The most popular genres',
                   'legend': None,
                   'x_axis': None,
                   'y_axis': None,
                   'circle_diagram': True}

    popularity = popular_genres(database)
    arg_1 = popularity.keys()
    arg_2 = popularity.values()
    graph_analysis(arg_1, arg_2, gr_settings)
