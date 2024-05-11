import pandas as pd
import matplotlib.pyplot as plt
from pygame import mixer

# on_bad_lines - китайские символы твари
df = pd.read_csv("stockerbot-export.csv", on_bad_lines='skip')

mixer.init()
mixer.music.load("povelitel.mp3")
mixer.music.play()


# Функция для отображения различных графиков
def visualize_data():
    # Выбор типа графика
    plot_type = input("Выберите тип графика ( bar,  pie): ")
    print("Спасибо за выбор , я пошла там типо считать ")
    matched_values = df.loc[df['verified'] == True, 'symbols']
    print(
        f" ТАМ ДУБЛИКАТОВ ! ! {len(matched_values) - len(matched_values.drop_duplicates())}")
    dta = pd.DataFrame()
    for index in matched_values.duplicated().index:
        # append shit :( tipo ymey lysche
        dta = pd.concat([dta, df.iloc[[index]]])

    # print(dta['symbols'])


    res = dta.groupby(["symbols"]).size().reset_index(name="count")
    # print(res['symbols'].tolist())
    x = res['symbols'].tolist()
    y = res['count'].tolist()

    # Генерация графика
    if plot_type == 'bar':
        plt.bar(x, y, label='Количество купленой ')
        plt.xlabel('Название ')
        plt.ylabel('Количество ')
        plt.title('egor')
        plt.legend()
    elif plot_type == 'pie':
        plt.pie(y, labels=x, autopct='%1.1f%%')
        plt.title("количетсво выпитого ")
    else:
        print("Неверный тип графика")

    # Показать график
    plt.show()


# Основной цикл программы
while True:
    # \n
    print(""" ЭтОт повелитель дорог создан для гоночной трассы,на протяжении 20 лет 3 серия посвещяет себя авто спорту.
          4 поколения БМВ м3 купе лишь вносит завершающие штрихи в образ совершенного автомобиля. Под капотом М3 лёгкий обортистый атмосферной V8.
          При пиковой мощности 420 л.с на 8 тысячах оборотах в минуту. 
          С отсечкой на отметке 8400 Этот двигатель лучше всего показывает -себя на повышенных оборотах. Благодаря пластиковой крышке....""")
    choice = input("Выберите операцию (visualize):")

    if choice == 'visualize':
        visualize_data()
    else:
        print("Неверный выбор")
