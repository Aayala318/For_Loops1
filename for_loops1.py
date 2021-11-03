#1 
def basic():
    for i in range(151):
        print(i)
basic()

2
def multiples_of_five():
    for i in range(5, 1001, 5):
        print(i)
multiples_of_five()

3
def the_dojo_way():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
the_dojo_way()

4
def woah_huge():
    final_sum = 0
    for i in range(1, 500000, 2):
        final_sum += i
        print(final_sum)
woah_huge()

5
def countdown_by_fours():
    for i in range(2018, 0, -4):
        print(i)
countdown_by_fours()

6
def flexible_counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1):
        if i % mult == 0:
            print(i)
flexible_counter(2, 9, 3)