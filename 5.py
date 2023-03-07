n = int(input("кол-во введенных слов: "))
S = []

for i in range(n):
    S.append(input())

word = ' '.join(S)

print(word)
