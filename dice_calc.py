import fractions, math
import plotly.graph_objs as go
import plotly.express as px

normal_roll = fractions.Fraction(1, 6).limit_denominator(6) # probability to get any one result on single roll


def roll_dice(target_value):    # return the roll probability on t_v and better
    return sum([normal_roll for elem in range(target_value, 7)])


def get_accurate_number(number: int, target_value: int, k: int):    #n-число бросков, t_v-значение успеха на кости, k-число
    combinations = fractions.Fraction(math.factorial(number), (math.factorial(k)*math.factorial(number-k)))
    result = combinations * roll_dice(target_value)**k*(1-roll_dice(target_value))**(number-k)
    return result


def get_result(number, target_value, k):
    res = 0
    plot_data = {}
    for i in range(0, k+1):
        print(f"Вероятность кинуть {i}+ равна {(1 - res)}")
        res += get_accurate_number(number, target_value, i)

        plot_data[i] = float(get_accurate_number(number, target_value, i))
    print(f"Общая вероятность равна {res}")
    for key in plot_data:
        print(key, round(plot_data[key], 5))
    print(f"Наибольшая вероятность у {max(plot_data, key=plot_data.get)} бросков, равна {round(plot_data[max(plot_data, key=plot_data.get)], 5)}")
    fig = px.line(x=plot_data.keys(), y=plot_data.values())
    fig.show()
    # plt.title("Вероятность получить заданное число успехов")
    # plt.xlabel('Число успехов')
    # plt.ylabel('Вероятность')
    # plt.grid()
    # plt.scatter(plot_data.keys(), [i * 100 for i in plot_data.values()])
    # plt.show()


podstavit = 1
get_result(5, 3, 5)