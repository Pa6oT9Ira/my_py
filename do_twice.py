def do_four(f, zn):
	do_twice(f, zn)
	do_twice(f, zn)

def print_twice(bruce):
	print(bruce)
	print(bruce)

def do_twice(f, zn):
	f(zn)
	f(zn)

def print_spam(c):
	print(c)


print_spam('fssdfdss')
print_twice(234+789)

do_twice(print_spam, 'qweqwe')

do_twice(print_twice, 'Спам')

do_four(print_spam, '4444444')
