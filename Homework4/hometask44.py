def lala(srtng=3, las=3, exclaim=0):
    """Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
стоит «!». По умолчанию 0"""
    result = 'la-' * las
    result = result[:-1]
    list = []
    for i in range(srtng):
        list.append(result)
    if exclaim:
        print(*list, sep="\n", end="!")
    else:
        print(*list, sep="\n")


lala(exclaim=1)
print()
lala(8, 10, 0)
