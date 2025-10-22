def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_beams4():
    do_four(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_posts4():
    do_four(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

def print_row4x4():
    print_beams4()
    do_four(print_posts4)

def print_grid4():
    do_four(print_row4x4)
    print_beams4()

def print_grid():
    do_twice(print_row)
    print_beams()

#print_grid()

print_grid()
print('')
print('')
print('')
print_grid4()

