import refeicoesru as ru

present = 0
ausent = 0

for item in ru.data:
    if item['WASPRESENT'] == 1:
        present += 1
    else:
        ausent += 1

print(f" {present} alunos estiveram presentes no dia 10/04/2024 em todas as refeições \n")

total = present + ausent
porcP = (present/total) * 100

print(f" A a porcentagem de presença geral dos alunos em todas as refeições do dia 2024-04-10: {porcP:.2f}% \n")

creme_galinhaP = 0
creme_galinhaA = 0

for item in ru.data:
    if item['MENU_ID'] == 2421 and item['WASPRESENT'] == 1:
        creme_galinhaP += 1
        
    elif item['MENU_ID'] == 2421 and item['WASPRESENT'] == 0:
        creme_galinhaA += 1
            
print(f"{creme_galinhaP} alunos estiveram presentes na refeição que serviu Creme de Galinha no dia 10/04/2024 \n")
print(f"{creme_galinhaA} alunos estiveram ausentes na refeição que serviu Creme de Galinha no dia 10/04/2024 \n")

arr = []

for item2 in ru.data:
    id_student = item2['STUDENT_ID']
    cont = 0
    for item2 in ru.data:
        if (id_student == item2['STUDENT_ID']):
            cont += 1
            
    if cont > 1:
        if id_student not in arr:
            arr.append(id_student)     
            
            
print(arr)   
