# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1      # 24 -> 4  16  4        # 60 -> 10  40  10

s = input("Общее количество журавликов: ")
s = int(s)

k = 2 * s // 3
pors = s // 6

print("Катя сделала журавликов:", k)
print("Петя сделал журавликов:", pors)
print("Серёжа сделал журавликов:", pors)
print("Петя, Катя и Серёжа сделали журавликов, соответственно:", pors, k, pors)