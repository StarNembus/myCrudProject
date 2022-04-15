
# Функция принимает на вход список сводной информации по абитуриентам (candidates)
# и возвращает список с именами 20 человек,
# набравших наибольшее СУММАРНОЕ количество баллов (с учетом extra баллов), которые станут студентами университета.
# В случае, если не получается однозначно определить 20 человек (например,
# 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют на 20 место в списке,
# стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
candidates = [

 {"name": "Georg",  "scores": {"math": 32, "russian_language": 35, "computer_science": 25},  "extra_scores": 3},
 {"name": "Sonya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores": 1},
 {"name": "Anna",  "scores": {"math": 93, "russian_language": 30, "computer_science": 31},  "extra_scores": 4},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
]


def find_top_20(candidates):
    my_dict = {}

    for item in candidates:
        student_name = item['name']
        score = item['scores']['math'] + item['scores']['russian_language'] + item['scores']['computer_science'] + item['extra_scores']
        my_dict[student_name] = score  # добавляем значение

    list_student = list(my_dict.items())
    list_student.sort(key=lambda i: i[1], reverse=True)
    for num in list_student:
        print(num[0], ':', num[1])
        # print(list_student)


find_top_20(candidates)


# Функция get_inductees принимает 3 списка одинаковой длины.
# В первом списке (names) — имена студентов, позволяющие их точно идентифицировать.
# Во втором (birthday_years) — год рождения. В третьем (genders) — пол студента.
# Частично они отсутствуют ввиду испорченного листа бумаги. Функция возвращает список с именами студентов мужского пола,
# которые достигли или могут достигнуть 18 лет в 2021 году, но при этом не старше 30 лет.
# Cтуденты, по которым невозможно точно установить - попадают они в список или нет, должны быть
# выведены отдельно. Пример входных данных приведен ниже

names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]