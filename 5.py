n = int(input("количество слов которых вы введете: "))
S = []

for i in range(n):
    S.append(input())

word = ' '.join(S)

print(word)
