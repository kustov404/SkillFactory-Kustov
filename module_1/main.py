import pandas as pd
from IPython.display import display

df = pd.read_csv('movie_bd_v5.csv')
display(df.columns)

# Вопрос 1. У какого фильма из списка самый большой бюджет?
display('1 - Фильм с самым большим бюджетом:', df[df['budget'] == df['budget'].max()]['original_title'])

# Вопрос 2. Какой из фильмов самый длительный (в минутах)?
display('2 - Самый длинный фильм:', df[df['runtime'] == df['runtime'].max()]['original_title'])

# Вопрос 3. Какой из фильмов самый короткий (в минутах)?
display('3 - Самый короткий фильм:', df[df['runtime'] == df['runtime'].min()]['original_title'])

# Вопрос 4. Какова средняя длительность фильмов?
display('4 - Средняя длительность фильмов:', round(df['runtime'].mean()))

# Вопрос 5. Каково медианное значение длительности фильмов?
display('5 - Медианное значение длительности фильмов:', round(df['runtime'].median()))

df['profit'] = df['revenue'] - df['budget']  # расчитаем прибыль для каждого фильма

# Вопрос 6. Какой фильм самый прибыльный?
display('6 - Самый прибыльный фильм:', df[df['profit'] == df['profit'].max()]['original_title'])

# Вопрос 7. Какой фильм самый убыточный?
display('7 - Самый убыточный фильм:', df[df['profit'] == df['profit'].min()]['original_title'])

# Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
display('8 - Объем сборов оказался выше бюджета у', df[df['revenue'] > df['budget']]['original_title'].count(), 'фильмов')

# Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?
s = df[df['release_year'] == 2008][['revenue', 'original_title']].sort_values('revenue', ascending=False)
display('9 - Самый кассовый фильм в 2008 году:', s.iloc[0]['original_title'])

# Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?
display('10 - Самый убыточный фильм за период с 2012 по 2014 годы:',
        df[(df['release_year'] >= 2012) & (df['release_year'] <= 2012)][['profit', 'original_title']]
        .sort_values('profit')
        .iloc[0]['original_title'])


# Вопрос 11. Какого жанра фильмов больше всего?
df['genres'] = df['genres'].str.split('|')
df = df.explode('genres')
display('11 - Больше всего фильмов жанра:', df['genres'].value_counts().index[0])

# Вопрос 12. Какого жанра среди прибыльных фильмов больше всего?
display('12 - Жанр, которого больше всего среди прибыльных фильмов:', df[df['profit'] > 0]['genres'].value_counts().index[0])

# Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом

df['director'] = df['director'].str.split('|')
df = df.explode('director')

display('13 - Режисср с самыми большими суммарными кассовыми сборами:',
        df.groupby(['director'])['revenue'].sum().sort_values(ascending=False).index[0])

# Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?
s = df[df.genres.str.contains('Action')]    # во временный датафрейм поместим все строки где есть жанр Action
display('14 - Режиссер, который снял больше всего фильмов в стиле Action:',
        s.groupby(['director'])['genres'].count().sort_values(ascending=False).index[0])

# Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом
df['cast'] = df['cast'].str.split('|')
df = df.explode('cast')

films_2012 = df[df['release_year'] == 2012]
display('15 - Самые кассовые фильмы в 2012 году с актером:',
        films_2012.groupby('cast')['revenue'].sum().sort_values(ascending=False).index[0])

# Вопрос 16. Какой актер снялся в большем количестве высокобюджетных фильмов?
# Примечание: в фильмах, где бюджет выше среднего по данной выборке.
s = df[df['budget'] > df['budget'].mean()]
display('16 - Актер, который снялся в большем количестве высокобюджетных фильмов:', s['cast'].value_counts().index[0])

# Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?
df['genres'] = df['genres'].str.split('|')
df = df.explode('genres')
display('17 - Nicolas Cage больше всего снялся в фильмах жанра:',
        df[df['cast'] == 'Nicolas Cage']['genres'].value_counts().index[0])

# Вопрос 18. Самый убыточный фильм от Paramount Pictures?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом
df['profit'] = df['revenue'] - df['budget']  # расчитаем прибыль для каждого фильма
df['production_companies'] = df['production_companies'].str.split('|')
df = df.explode('production_companies')

display('18 - Самый убыточный фильм от Paramount Pictures:',
        df[df['production_companies'] == 'Paramount Pictures'][['original_title', 'profit']]
        .sort_values('profit').iloc[0]['original_title'])

# Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?
display('19 - Самый успешный год по суммарным кассовым сборам:',
        df.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False).index[0])

# Вопрос 20. Какой самый прибыльный год для студии Warner Bros?
display('20 - Самый прибыльный год для студии Warner Bros',
        df[df['production_companies'].str.contains('Warner Bros.', regex=False)]
        .groupby(['release_year'])['profit'].sum().sort_values(ascending=False).index[0])


# Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом


def fill_month(date_):    # функция вычленения месяца (который стоит на 0 месте)
    return date_[0]


df['release_date'] = df['release_date'].str.split('/')
df['release_month'] = ""
df['release_month'] = df['release_date'].apply(fill_month)
display('21 - За все годы в', df['release_month'].value_counts().index[0], 'месяце вышло больше всего фильмов')

# Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?
display('22 - Суммарно вышло фильмов летом (за июнь, июль, август):',
        df[(df['release_month'] == '6') |
           (df['release_month'] == '7') |
           (df['release_month'] == '8')].count().iloc[0])

# Вопрос 23. Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?
df['director'] = df['director'].str.split('|')
df = df.explode('director')

pivot = df.pivot_table(
    values = 'original_title',
    index = 'director',
    columns='release_month',
    aggfunc='count',
    fill_value=0)

pivot['winter'] = pivot['12'] + pivot['1'] + pivot['2']
display('23 - Больше всего фильмов зимой выпускает:',
        pivot.sort_values('winter', ascending=False)['winter'].index[0])

# Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом
df.production_companies = df.production_companies.str.split('|')
df = df.explode('production_companies')

df['length_title'] = df['original_title'].str.len()    # в новом столбце считаем длинну названия
display('24 - Самые длинные названия своим фильмам по количеству символов даёт студия:',
        df.groupby(['production_companies'])['length_title'].mean()
        .sort_values(ascending=False).index[0])


# Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?


def word_count(str_):    # разделяем предложения на слова
    return len(str_.split())


df['desc_len'] = df['overview'].apply(word_count)    # считаем для каждого описания свою длинну
display('25 - Самые длинные по количеству слов описания от студии:',
        df.groupby(['production_companies'])['desc_len'].mean().sort_values(ascending=False).index[0])

# Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?
df = pd.read_csv('movie_bd_v5.csv')    # откроем файл заново, чтобы работать с оригинальным файлом
display('26 - Самые лучшие фильмы по рейтингу:\n',
        df.sort_values('vote_average', ascending=False)['original_title'].head(5), '\n')


# Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?
df.cast = df.cast.str.split('|')
df = df.explode('cast')


def freq(df_t):    # обьявляем функцию которая будет заниматься перебором и подсчетом "частоты"
    frequency = {}

    for Title in pd.unique(df_t['original_title']):    # сначала перебираем по уникальным фильмам
        # для каждого фильма будем перебирать актеров по парно и добавляеть в словарь +1 если они вместе работали
        for Actor1 in df_t[df_t['original_title'] == Title]['cast']:
            for Actor2 in df_t[df_t['original_title'] == Title]['cast']:
                if Actor1 + ' & ' + Actor2 not in frequency:    # если пары нет в словаре, то создаем ее
                    frequency[Actor1 + ' & ' + Actor2] = 0
                frequency[Actor1 + ' & ' + Actor2] += 1    # если пара была в словаре, то +1 к счетчику

                if Actor1 == Actor2:    # если пара - это один и тот же актер, то приравниваем к 0
                    frequency[Actor1 + ' & ' + Actor2] = 0

    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)    # сортируем получившийся словарь
    return sorted_freq


display('27 - Актеры, которые чаще всего снимаются в одном фильме вместе:', freq(df)[0][0])
