#python
#Ramsay: "(...) você vence se conseguir adivinhar quem eu sou e por que estou torturando você."
#Theon deve pensar rápido e adivinhar quem é seu algoz! Entretanto, Ramsay já decidiu o que ele irá fazer depois que Theon der sua resposta.
#Theon pode dizer que seu algoz é alguma dentre N pessoas. Considere que as pessoas são numeradas de 1 a N. Se Theon responder que seu algoz é a pessoa i, Ramsay irá atingi-lo Ti vezes.
#Sua tarefa é ajudar Theon a determinar qual deve ser sua resposta de forma a minimizar o número de vezes que ele será atingido.
N = int(input())
person = input().split()
for i in range(N):
    person[i] = int(person[i])
lowest = min(person)
p = person.index(lowest) + 1
print(p)