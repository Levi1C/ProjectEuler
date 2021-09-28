import numpy as np
import problem_functions as pf


def timeit_func(i, *fcts):
    from timeit import Timer

    time_list = []
    for fct in fcts:

        if "." not in fct:
            import_stmt = "from __main__ import " + fct
        else:
            import_stmt = "from %s import %s" % (fct.split(".")[0], fct.split(".")[1])
            fct = fct.split(".")[1]

        time_list.append(Timer(fct + "(" + str(i) + ")", import_stmt).timeit(3))

    print_stmt = ""
    for fct, fct_time in zip(fcts, time_list):
        print_stmt += fct + ":\t" + str(fct_time) + "\n"
    print(print_stmt)  # todo: testen

    # # for i in range(100, 10001, 100):
    # #     print(Timer("problem3(" + str(i) + ")", "from __main__ import problem3").timeit(3))
    # for i in range(500, 1001, 20):
    #     s = "problem1(" + str(i) + ")"
    #     t1 = Timer(s, "from __main__ import problem1")
    #     time1 = t1.timeit(3)
    #     s = "problem1_dif(" + str(i) + ")"
    #     t2 = Timer(s, "from __main__ import problem1_dif")
    #     time2 = t2.timeit(3)
    #     print("n=%2d, meth1: %8.6f, meth2:  %7.6f, percent: %10.2f" % (i, time1, time2, time1 / time2))


def problem1(n=1000):
    mult_of_3 = pf.mult_of_x_smaller_n(3, n)
    mult_of_5 = pf.mult_of_x_smaller_n(5, n)
    union_of_mults = list(set().union(mult_of_3, mult_of_5))
    sum_of_union = sum(union_of_mults)
    print(sum_of_union)


def problem1_dif(n=1000):
    union_of_mults = list(filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(n)))
    sum_of_union = sum(union_of_mults)
    print(sum_of_union)


def problem2(n=4e6):
    fib_list = pf.fibonacci(n)
    fib_list_even = list(filter(lambda x: (x % 2 == 0), fib_list))
    fib_list_even_sum = sum(fib_list_even)
    print(fib_list_even_sum)


def problem3(number=600851475143):
    print(pf.prime_factorization(number))


def problem4(maxi=999):
    largest = 0
    x = maxi
    y = x
    while x * y > largest:
        while x * y > largest and y > 0:
            prod = x * y
            if pf.is_palindrom(prod):
                largest = prod
                print(x, y)
            else:
                y -= 1

        x -= 1
        y = x
    print(x, y)
    # print(largest)


def problem5(maxi=20):
    prime_dict = pf.find_generating_set_of_primes(range(2, maxi + 1))
    print(prime_dict)
    print(pf.prime_factors_product(prime_dict))


def problem6(start=1, end=100):
    arr = np.arange(start, end + 1)
    solution = np.sum(arr) ** 2 - np.sum(arr ** 2)
    print(solution)


def problem7(no=10001):
    pf.prime_list_func_by_no_of_primes(no)
    print(pf.prime_list[no - 1])


def problem8(digits=13,
             num_to_check="73167176531330624919225119674426574742355349194934"
                          "96983520312774506326239578318016984801869478851843"
                          "85861560789112949495459501737958331952853208805511"
                          "12540698747158523863050715693290963295227443043557"
                          "66896648950445244523161731856403098711121722383113"
                          "62229893423380308135336276614282806444486645238749"
                          "30358907296290491560440772390713810515859307960866"
                          "70172427121883998797908792274921901699720888093776"
                          "65727333001053367881220235421809751254540594752243"
                          "52584907711670556013604839586446706324415722155397"
                          "53697817977846174064955149290862569321978468622482"
                          "83972241375657056057490261407972968652414535100474"
                          "82166370484403199890008895243450658541227588666881"
                          "16427171479924442928230863465674813919123162824586"
                          "17866458359124566529476545682848912883142607690042"
                          "24219022671055626321111109370544217506941658960408"
                          "07198403850962455444362981230987879927244284909188"
                          "84580156166097919133875499200524063689912560717606"
                          "05886116467109405077541002256983155200055935729725"
                          "71636269561882670428252483600823257530420752963450"):
    num_to_check = np.array(list(num_to_check), np.int64)
    biggest_product = 0
    range_to_check = range(len(num_to_check) - digits)
    for x in range_to_check:
        area_to_check = num_to_check[x:x + digits]
        product_of_area = np.prod(area_to_check)
        if product_of_area > biggest_product:
            biggest_product = product_of_area
    print(biggest_product)


def problem9(summe=1000):
    for a in range(1, summe - 1):
        for b in range(a + 1, summe):
            c = summe - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                return a * b * c


def problem10(maxi=2e6):
    pf.prime_list_func(maxi)
    prime_list = pf.prime_list
    print(sum(prime_list))


def problem11(digits=4, grid_to_check="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""):
    # conversion to np array
    grid = grid_to_check.split("\n")
    grid = [row.split(" ") for row in grid]
    grid = np.array(grid, dtype=np.int64)

    biggest_product = 0
    # check in x-direction
    for x in range(grid.shape[0] - digits):
        for y in range(grid.shape[1]):
            area_to_check = grid[x:x + digits, y]
            product_of_area = np.prod(area_to_check)
            if product_of_area > biggest_product:
                biggest_product = product_of_area

    # check in y-direction
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1] - digits):
            area_to_check = grid[x, y:y + digits]
            product_of_area = np.prod(area_to_check)
            if product_of_area > biggest_product:
                biggest_product = product_of_area

    for flip_grid in [False, True]:
        if flip_grid:
            grid = np.flipud(grid)
        for diag_no in range(-grid.shape[0] + digits, grid.shape[0] - digits + 1):
            diag = grid.diagonal(diag_no)
            for i in range(diag.shape[0] - digits + 1):
                area_to_check = diag[i:i + digits]
                product_of_area = np.prod(area_to_check)
                if product_of_area > biggest_product:
                    biggest_product = product_of_area

    print(biggest_product)
    return biggest_product


def problem12(no_divisors_limit=500):
    # pf.prime_list_func(1e7)
    for i in pf.triangle_numbers_generator():
        # print(i)

        # no_divisors = len(pf.divisors(i))
        # print(no_divisors)

        # prime_factors = pf.prime_factorization(i)
        # no_divisors = 1
        # for val in prime_factors.values():
        #     no_divisors *= (val + 1)

        no_divisors = pf.get_factors_no_numpy(i)

        # print(no_divisors)

        if no_divisors > no_divisors_limit:
            print(i)
            # return i

    # pf.prime_list_func(8)
    #
    # prime_list = [2,3]
    # # prime_list = pf.prime_list
    #
    # comb_over_limit = []
    # comb = {}
    # for prime in prime_list:
    #     comb[prime] = 0
    # def_comb = comb
    # biggest_num = 1
    # prod = 1
    #
    # def gen():
    #     i = 1
    #     while True:
    #         yield i
    #         i += 1
    #
    # def generate(k):
    #     if k < len(prime_list)-1:
    #         y = -1
    #         while prod < 20:
    #             y += 1
    #             rest = generate(k + 1)
    #             for x in rest:
    #                 yield [y] + x
    #     else:
    #         i = -1
    #         while prod < 20:
    #             i += 1
    #             yield [i]
    #
    # for x in generate(0):
    #     print(x)
    #     comb = dict(zip(prime_list, x))
    #     prod = pf.prime_factors_product(comb)


def problem13(file="problems_data//p013_numbers.txt"):
    data = open(file, "r")
    nums = data.read()
    data.close()

    nums = np.array([int(i) for i in nums.split("\n")])

    nums_sum = np.sum(nums)
    first_ten = str(nums_sum)[:10]
    print(first_ten)


def problem14(limit=1e6):
    longest_no = 0
    longest = 0
    for n in range(1, int(limit)):
        length = pf.collatz_seq_length(n)
        if length > longest:
            longest = length
            longest_no = n

    print(longest_no)


def problem15(length=20):
    from math import factorial

    zaehler = factorial(length * 2)
    nenner = factorial(length) ** 2
    print(zaehler / nenner)


def problem16(base=2, exponent=1000):
    print(sum(map(int, str(base ** exponent)[::])))


def problem17(limit=1000):
    sum_of_lens = 0
    for num in range(1, limit + 1):
        sum_of_lens += pf.give_len_of_num_word(num)
    print(sum_of_lens)


def problem18(triang="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""", cut=None):
    if "\n" in triang[-2:]:
        triang = triang[:-2]
    triang = [list(map(int, row.split(" "))) for row in triang.split("\n")[:cut]]
    # print(triang)
    triang_flipped = triang[::-1]
    for row_no in range(len(triang)):
        for j in range(len(triang_flipped[row_no])-1):
            triang_flipped[row_no+1][j] += max(triang_flipped[row_no][j:j+2])

    print(triang_flipped[-1])



def problem18_brute_force(triang="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""", cut=None):
    from itertools import product

    triang = [list(map(int, row.split(" "))) for row in triang.split("\n")[:cut]]
    row_nums = len(triang)

    combos = product([0, 1], repeat=row_nums-1)
    biggest_sum = 0
    biggest_seq = []
    for combo in combos:
        idx = 1
        seq = [triang[0][0]]
        for i, row in zip(combo, triang[1:]):
            seq.append(row[idx])
            idx += i
        seq_sum = sum(seq)
        if seq_sum > biggest_sum:
            biggest_seq = seq
            biggest_sum = seq_sum

    print(biggest_seq)
    print(biggest_sum)  # 1074


def problem67(file="problems_data//p067_triangle.txt"):
    data = open(file, "r")
    triang = data.read()
    data.close()

    problem18(triang)


def problem19(start_date="1.1.1901", end_date="31.12.2000", weekday_to_check="sun", day_of_month=1):
    start_day, start_month, start_year = map(int, start_date.split("."))
    end_day, end_month, end_year = map(int, end_date.split("."))

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    weekday_no = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = 1900

    counting_active = False
    count = 0
    while True:
        for month_no in range(12):
            month_len = days_in_month[month_no]
            if month_no == 1:
                if year % 4 == 0 and year % 100 != 0:
                    month_len += 1
                elif year % 400 == 0:
                    month_len += 1

            for day in range(month_len):
                if start_day == day + 1 and start_month == month_no + 1 and start_year == year:
                    counting_active = True

                if counting_active:
                    if weekdays[weekday_no] == weekday_to_check and day == day_of_month-1:
                        count += 1

                if end_day == day + 1 and end_month == month_no + 1 and end_year == year:
                    print(count)
                    return  count

                weekday_no += 1
                if weekday_no > 6:
                    weekday_no = 0

        year += 1


    pass


def problem20(num=100):
    fact = pf.factorial(num)
    print(fact)
    print(sum(map(int, str(fact))))


def problem21(limit=10000):
    pf.prime_list_func(limit)
    am_nums = set()
    for i in range(limit):
        if i in pf.prime_list or i in am_nums:
            continue

        am = pf.check_amicable(i)
        if am and am < limit and am != i:
            am_nums.update([i, am])

    print(sum(am_nums))


def problem24(digits=range(10)):
    pass

problem12()