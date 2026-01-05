"""
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм 
та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою 
сумарною калорійністю в межах обмеженого бюджету.
Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, 
де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, 
максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, 
яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

- Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. 
Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, 
не перевищуючи заданий бюджет.

- Програмно реалізовано функцію, яка використовує принцип динамічного програмування. 
Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""

### Let's assume it is not allowed to order the same food twice ###

def greedy_algorithm(items: dict[dict], budget: int) -> list[str]:
    """
    Function calculates a set of dishes using greedy algorithm.
    Returns a list of items selected.
    """
    food_preference = sorted(
        [ (attr["calories"]/attr["cost"], name) for name, attr in items.items() ], 
        reverse=True)
    result = []
    current_budget = budget
    for item in food_preference:
        item_cost = items[item[1]]["cost"]
        if current_budget >= item_cost:
            current_budget -= item_cost
            result.append(item[1])
    return result

def dynamic_programming(items: dict[dict], budget: int) -> list[str]:
    """
    Function calculates a set of dishes using dynamic programming approach.
    Returns a list of items selected.
    """
    food_names = list(items.keys())
    calories = [ items[food]["calories"] for food in food_names ]
    cost = [ items[food]["cost"] for food in food_names ]
    n = len(food_names)
    sub_choices = [[0 for _ in range(budget + 1)] for i in range(n + 1)]
    food_choices = [[ [] for _ in range(budget + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                sub_choices[i][b] = 0
                food_choices[i][b] = []
            elif cost[i - 1] <= b:
                new_profit = calories[i - 1] + sub_choices[i - 1][b - cost[i - 1]]
                old_profit = sub_choices[i - 1][b]
                if new_profit > old_profit:
                    food_choices[i][b] = food_choices[i - 1][b - cost[i - 1]][:]
                    food_choices[i][b].append(food_names[i - 1])
                else:
                    food_choices[i][b] = food_choices[i - 1][b][:]
                sub_choices[i][b] = max(new_profit, old_profit)
            else:
                sub_choices[i][b] = sub_choices[i - 1][b]
                food_choices[i][b] = food_choices[i - 1][b][:]
    return food_choices[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print("Greedy algorithm result: ", greedy_algorithm(items, 100))
print("Dynamic programming result: ", dynamic_programming(items, 100))
