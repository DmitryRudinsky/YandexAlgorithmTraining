# Чтение ввода
score_first_match = input().split(':')
score_second_match = input().split(':')
location = int(input())

# Преобразование строк в целые числа
goals_first_match = int(score_first_match[0])
goals_second_match = int(score_first_match[1])
goals_current_match_first_team = int(score_second_match[0])
goals_current_match_second_team = int(score_second_match[1])

# Расчет необходимого количества голов
if location == 1:
    # Команда играет дома
    total_goals_first_team = goals_first_match + goals_current_match_first_team
    total_goals_second_team = goals_second_match + goals_current_match_second_team
else:
    # Команда играет в гостях
    total_goals_first_team = goals_current_match_first_team + goals_second_match
    total_goals_second_team = goals_current_match_second_team + goals_first_match

# Определение необходимого количества голов для победы
if total_goals_first_team > total_goals_second_team:
    # Команда уже впереди в общем счете, ей не нужно больше голов
    required_goals = 0
elif total_goals_first_team == total_goals_second_team:
    # Команды сравниваются по гостевым голам
    if goals_second_match > goals_first_match:
        required_goals = 0
    else:
        required_goals = goals_first_match - goals_second_match + 1
else:
    # Команда отстает в общем счете, ей нужно выровнять результат
    required_goals = total_goals_second_team - total_goals_first_team + 1

# Вывод результата
print(required_goals)
