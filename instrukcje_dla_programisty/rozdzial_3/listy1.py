bicycles = ['trekingowy', 'szosowy', 'miejski', 'górski']
print(bicycles[1])
message = f'moim rowerem jest rower {bicycles[1].title()}'
print(message)
motocykle = []
motocykle.append('honda')
motocykle.append('suzuki')
motocykle.append('yamaha')
print(motocykle)
pop_motocykle = motocykle.pop()
print(pop_motocykle)
magicians = ['alicja', 'dawid', 'karolina']
for magician in magicians:
    print(f"{magician.title()}, to była doskonała sztuczka!")
    print(f"Nie mogę się doczekać Twojej kolejnej sztuczki, {magician.title()}.\n")

print("Dziękuję wszystkim. To był naprawdę wspaniały występ!")
numbers = list(range(2, 11, 2))
print(numbers)
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
