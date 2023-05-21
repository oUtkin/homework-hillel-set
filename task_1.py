# 1. Дано дві множини A і B
# У багатьох А знаходяться імена боржників за Червень
# У безлічі B знаходяться імена боржників за Липень
# Знайти:
# * Вивести імена людей які повинні за Червень та Липень
# * Вивести боржників за Липень у яких немає боргу за Червень

A = {'James', 'Bob', 'John', 'Larry',
     'Otto', 'Jimmie', 'Richard', 'Kyle',
     'Samantha', 'Alex', 'Phill', 'Mitchel',
     'Stacy', 'Pam', 'Jose', 'Diana'
     }

B = {'James', 'Bob', 'Ivan', 'Larry',
     'Melany', 'Jimmie', 'Jenny', 'Brian',
     'Lucy', 'Alex', 'Phill', 'Mitchel',
     'Stacy', 'Marshall'
     }

both_months_debtors = ', '.join(A & B)
july_but_not_june_debtors = ', '.join(B - A)
print(f'Боржники за червень та липень: {both_months_debtors}\n'
      f'Боржники за липень у яких немає боргу за червень: {july_but_not_june_debtors}')
