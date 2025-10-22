
import math
def print_twice(bruce):
 print(bruce)
 print(bruce)

print_twice('Спам' * 5)
print_twice(6)
print_twice(math.pi)

michael = 'Эрик, полпчелы.'
print_twice(michael)

def cat_twice(part1, part2):
	cat = part1 + part2
	print_twice(cat)

cat_twice(2,4)
cat_twice('рАЗ','Два')

line1 = 'Тили-тили '
line2 = 'трали-вали.'
cat_twice(line1, line2)

print(cat)
print(bruce)