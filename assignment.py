# Here we are replacing the one item of list to entered one
def replace_value(values, index, new_value):
    values[index] = new_value
    
# Here we are finding match elements from list with our target
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
# Here we are tend to find the min, max, and the total of list items 
def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record

days = int(input("Enter the number of days: "))
original = []

# The moment of receiving emails by the number of entered days
for i in range(days):
    emails = int(input("Enter the number of received emails: "))
    original.append(emails)
# Here we are cloning the original list
updated = original[:]
index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of emails: "))
target = int(input("Enter the number of emails to search for: "))

replace_value(updated, index, new_value)
find_index = find_first(updated,target)
match_count = updated.count(target)
minimum, maximum,total = summarize(updated)
sorted_list = sorted(updated)
# Printing the outputs
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum number of emails: {minimum}")
print(f"Maximum number of emails: {maximum}")
print(f"Total number of emails: {total}")
# Here we are checking if the entered number is similar with item in the list
if find_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {find_index}")
print(f"Matching values: {match_count}")


# This code was written by student of FMCO-04 group --------- SHAKIROV BOVURBEK -----------


# Here is the translated condition of the task, if I will need to solve any quizzes! :)

# Определите три функции:

# replace_value(values, index, new_value) изменяет элемент в позиции index на new_value. Это изменяет значения в списке и возвращает None.
# find_first(values, target) возвращает индекс первого элемента, равный target. Если ни один элемент не равен target, возвращает значение -1. Используйте цикл и ==. Не используйте .index() или target в значениях.
# summary(значения) возвращает кортеж с тремя значениями: наименьшим значением, наибольшим значением и итогом, в таком порядке. Используйте min(), max() и sum(). Не изменяйте значения в списке.
# Требования к программе
# Ваша программа должна:

# Запросите количество дней и преобразуйте его в целое число.
# Для каждого дня запросите количество полученных электронных писем и преобразуйте его в целое число. Добавьте каждое значение в список с именем original с помощью функции append().
# Используйте разделку, чтобы создать новый список с именем updated, содержащий копию оригинала. Сохраните оригинал без изменений.
# Запросите индекс и новое количество электронных писем. Вызовите replace_value(), чтобы изменить элемент с этим индексом в updated.
# Запросите несколько электронных писем для поиска и сохранения их в target.
# Используйте функцию find_first(), чтобы найти индекс первого элемента, равный target в updated. Сохраните возвращаемый индекс в переменной. Используйте функцию .count(), чтобы подсчитать, сколько раз target появляется в updated, и сохранить это значение в другой переменной.
# Вызовите summarize() с updated. Распакуйте возвращаемый кортеж в три переменные: minimum, maximum и total.
# Используйте sorted() с updated, чтобы создать новый список, отсортированный от наименьшего к наибольшему. Сохраните новый список в переменной. Сохраните updated без изменений.
# Печатать с использованием f-строк:
# исходный, обновленный и отсортированный списки;
# наименьшее количество электронных писем, наибольшее количество электронных писем и общее количество электронных писем;
# индекс первого элемента равен target или Target не найден, если функция вернула значение -1;
# сколько раз target появляется в обновленном виде.
# Сообщения во входных примерах являются предложениями. Вы можете использовать свои собственные сообщения при запросе ввода.

# Для обеспечения согласованности сохраните кортеж, возвращаемый с помощью `summary(values)`, в `stats_record` перед его возвратом и распакуйте его в `minimum`, `maximum` и `total` в основной программе.


# Input:

# Enter the number of days: 5
# Enter the number of emails received: 8
# Enter the number of emails received: 12
# Enter the number of emails received: 8
# Enter the number of emails received: 20
# Enter the number of emails received: 4
# Enter the index to correct: 1
# Enter the new number of emails: 8
# Enter the number of emails to search for: 8
# Copy
# Output:

# Original: [8, 12, 8, 20, 4]
# Updated: [8, 8, 8, 20, 4]
# Sorted: [4, 8, 8, 8, 20]
# Minimum number of emails: 4
# Maximum number of emails: 20
# Total number of emails: 48
# First matching index: 0
# Matching values: 3
# Copy
# Example 2
# Input:

# Enter the number of days: 1
# Enter the number of emails received: 10
# Enter the index to correct: 0
# Enter the new number of emails: 6
# Enter the number of emails to search for: 10
# Copy
# Output:

# Original: [10]
# Updated: [6]
# Sorted: [6]
# Minimum number of emails: 6
# Maximum number of emails: 6
# Total number of emails: 6
# Target not found
# Matching values: 0