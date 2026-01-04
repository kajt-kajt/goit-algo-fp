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
    for item in food_preference:
        item_cost = items[item[1]]["cost"]
        if budget >= item_cost:
            budget -= item_cost
            result.append(item[1])
    return result

def dynamic_programming(items: dict[dict], budget: int) -> list[str]:
    """
    Function calculates a set of dishes using dynamic programming approach.
    Returns a list of items selected.
    """
    food_names = list(items.keys())
    n = len(food_names)
    sub_choices = [[0 for b in range(budget + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                sub_choices[i][b] = 0
            elif items[food_names[i - 1]]["cost"] <= b:
                # K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                sub_choices[i][b] = max(items[food_names[i - 1]]["calories"] + sub_choices[i - 1][b - items[food_names[i - 1]]["cost"]], sub_choices[i - 1][b])
            else:
                sub_choices[i][b] = sub_choices[i - 1][b]
    return sub_choices[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 100))

print(dynamic_programming(items, 100))
