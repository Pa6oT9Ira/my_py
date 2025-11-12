print("Цикл WHILE\n")
num = -3
while num < 5:
	print(f"num = {num}")
	num += 1
else:
	print(f"num = {num}. Работа программы завершена")
# print("Завершение программы")

print("\n\nЦикл for\n")

mes = "Привет!"
print(mes)

for ci in mes:
	print(ci)
else:
	print("Цикл FOR завершен")

print("\n\nВложенные цикл\n")

i = 1
j = 1

while i < 10:
	while j < 10:
		print(f"{j} * {i} = {i * j}", end = "\t")
		j += 1
	print("\n")
	j = 1
	i += 1
# else:
# 	print("Конец вложенных циклов")

print("\n\nвложенные Циклы for\n")

for c1 in "012":
	for c2 in "0123456789":
		print(f"{c1}{c2}")

print("\n\n Break and continue \n")	

num = 0
while num < 10:
	if num == 7: 
		print("Exit")
		break
#	print(num, end = "  ")
	num += 1
	if num == 3: 
		print("Continue")
		continue
	print(num)



print("Конец")