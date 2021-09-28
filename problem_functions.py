import numpy as np

"################ Prime Stuff ######################"

prime_list = [2, 3, 5]
"list of primes"


def prime_list_func(upper_limit):
    """
    with sieve of atkin
    :param upper_limit:
    :return:
    """
    start_limit = prime_list[-1] + 2
    upper_limit = int(upper_limit) + 1
    candidates = list(range(start_limit, upper_limit))
    candidates_statuses = [True] * len(candidates)

    for prime in prime_list:
        to_remove = prime ** 2
        if to_remove >= upper_limit:
            break
        while to_remove < upper_limit:
            if to_remove >= start_limit:
                candidates_statuses[to_remove - start_limit] = False
            to_remove += prime

    for cand, status in zip(candidates, candidates_statuses):
        if status:
            to_remove = cand ** 2

            if to_remove >= upper_limit:
                break
            while to_remove < upper_limit:
                candidates_statuses[to_remove - start_limit] = False
                to_remove += cand

    for cand, status in zip(candidates, candidates_statuses):
        if status:
            prime_list.append(cand)


def is_prime(x):
    """
    get's slow for large numbers, because prime list is being updated
    :param x:
    :return:
    """
    if x in prime_list:
        return True
    elif not prime_list[-1] > x // 2:
        prime_list_func(x // 2 + 1)
    if 0 in x % np.array(prime_list):
        return False
    else:
        return True


def prime_factorization(number, as_dict=True):
    """
    :param number:
    :return:
    """
    if prime_list[-1] < number // 2:
        prime_list_func(number // 2)
    x = number
    prime_factors = {}
    i = 2
    while x >= i:
        if is_prime(i):
            while x % i == 0:
                prime_factors[i] = prime_factors.get(i, 0) + 1
                x //= i
        if i == 2:
            i += 1
        else:
            i += 2

    if as_dict:
        return prime_factors
    else:
        return prime_factor_dict_to_list(prime_factors)


def prime_factor_dict_to_list(prime_factor_dict):
    prime_factors_list = []
    for prime in prime_factor_dict.keys():
        prime_factors_list.extend(prime_factor_dict[prime] * [prime])
    return prime_factors_list


def prime_factors_product(prime_factors):
    if type(prime_factors) is dict:
        prod = 1
        for key, val in prime_factors.items():
            prod *= key ** val
        return prod
    elif type(prime_factors) is list:
        return np.prod(np.array(prime_factors))


"################ Problem 1 ######################"


def mult_of_x_smaller_n(x, n):
    return [i for i in range(x, n, x)]


"################ Problem 2 ######################"


def fibonacci(maximum):
    pass
    fib_list = [1, 2, 3]
    next_num = fib_list[-1] + fib_list[-2]
    while next_num < maximum:
        fib_list.append(next_num)
        next_num = fib_list[-1] + fib_list[-2]
    return fib_list


def fibonacci2(no):
    memo = {0: 0, 1: 1}

    def fibm(n):
        if not n in memo:
            memo[n] = fibm(n - 1) + fibm(n - 2)
        return memo[n]

    return fibm(no)


"################ Problem 3 ######################"


def prime_list_func_old1(upper_limit):
    prime_list = [2, 3, 5]

    for i in np.arange(prime_list[-1] + 1, upper_limit + 1, dtype=int):
        if 0 in i % np.array(prime_list):
            continue
        else:
            prime_list.append(i)


def prime_list_func_old2(upper_limit):
    prime_list = [2, 3, 5]

    i = prime_list[-1] + 2
    while i < upper_limit:
        divider_found = False
        for prime in prime_list[1:]:
            if i % prime == 0:
                divider_found = True
                break
        if not divider_found:
            prime_list.append(i)
        i += 2


def prime_factorization_old1(number):
    """
    crashes for big numbers
    """
    x = number
    if not prime_list[-1] > x / 2:
        prime_list_func(int(x / 2 + 1))
    prime_factors = []
    for i in prime_list:
        while x % i == 0:
            x = x / i
            prime_factors.append(i)
    return prime_factors


"################ Problem 4 ######################"


def is_palindrom(x):
    x = str(x)
    y = x[::-1]
    return x == y


"################ Problem 5 ######################"


def find_generating_set_of_primes(group):
    """
    gibt das Tupel an Primzahlen, mit welcher jedes Element von group gebildet werden kann
    :param group: Satz an Zahlen
    :return:
    """
    gen_set = {}
    group = np.array(group)
    for i in group:
        prime_factors = prime_factorization(i)
        for pr_fct_prime, pr_fct_power in prime_factors.items():
            if pr_fct_prime not in gen_set.keys():
                gen_set[pr_fct_prime] = pr_fct_power
            elif gen_set[pr_fct_prime] < pr_fct_power:
                gen_set[pr_fct_prime] = pr_fct_power
    return gen_set


"################ Problem 7 ######################"


def prime_list_func_by_no_of_primes(no, step=100):
    upper_limit = step
    while len(prime_list) < no:
        prime_list_func(upper_limit)
        upper_limit += step


"################ Problem 9 ######################"


def is_square(apositiveint):
    x = apositiveint // 2
    seen = {x}
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


"################ Problem 9 ######################"


def prime_list_func_step(maxi, step=100):
    upper_limit = step
    while prime_list[-1] < maxi:
        prime_list_func(upper_limit)
        upper_limit += step


"################ Problem 12 ######################"


def divisors(n):
    """
    from: https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number/37058745#37058745
    :param n:
    :return:
    """
    if is_prime(n):
        return [1, n]

    factors = prime_factorization(n)
    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k + 1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    return list(generate(0))


def divisors_gen(n):
    """
    from: https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number/37058745#37058745
    :param n:
    :return:
    """
    factors = prime_factorization(n)
    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k + 1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    yield from generate(0)


def divisors_old(n):
    if is_prime(n):
        return [1, n]

    divis = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            divis.append(i)
    return divis


def get_factors_no(n):
    return sum(2 for i in range(1, int(np.sqrt(n) + 0.5) + 1) if not n % i)


def get_factors_no_numpy(num):
    arr = num % np.arange(1, int(np.sqrt(num) + 0.5) + 1)
    return arr[arr == 0].size


def triangle_numbers_generator():
    i = 1
    number = i
    while True:
        yield number
        i += 1
        number += i


def triangle_numbers(limit):
    triang_nums = []
    i = 1
    number = i
    while number < limit:
        triang_nums.append(number)
        i += 1
        number += i
    return triang_nums


def is_triangle_number(num):
    from math import sqrt
    root = sqrt(8 * num + 1)
    if root % 1 != 0:
        return False
    elif (root + 1) / 2 % 1 != 0:
        return False
    else:
        return True


def find_divisor_multiplicities(limit=500):
    prod = 1

    def generator(depth):
        depth -= 1
        if depth == 0:
            i = 1
            while prod < limit:
                yield [i]
                i += 1
        else:
            rest = generator(depth - 1)
            i = 0
            while True:
                for x in rest:
                    yield [i] + x
                i += 1
                rest = generator(depth - 1)

    d = 1
    while True:
        exp_base_range = range(2, 2 + d)
        for exponent_list in generator(d):
            prod_dict = dict(zip(exp_base_range, exponent_list))
            prod = prime_factors_product(prod_dict)
            if prod >= limit:
                yield prod_dict
            if exp_base_range[-1] ** exponent_list[-1]:
                d += 1
                break



"################ Problem 14 ######################"


def collatz_seq_length(n):
    length = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        length += 1
    return length


"################ Problem 15 ######################"


def factorial(n):
    # oder einfach math.factorial
    if n == 0:
        return 1
    else:
        # np.prod(np.arange(2, n+1, dtype=np.uint64))
        prod = 1
        for i in range(2, n + 1):
            prod *= i
        return prod


"################ Problem 17 ######################"


def give_len_of_num_word(num):
    # len of nums to 20
    num_to_20 = ", one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, " \
                "fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"
    num_to_20 = num_to_20.split(", ")
    num_len_to_20 = list(map(len, num_to_20))
    # print(num_len_to_20)
    num_len_to_20_old = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # print(num_len_to_20_old)
    num_len_to_20 = num_len_to_20_old
    # len of decimals
    decimals_num = "zero, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety"
    decimals_num = decimals_num.split(", ")
    # decimals_len = list(map(len, decimals_num))
    decimals_len = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

    thous_len_of_num = 0
    thous_digit = num // 1000
    if thous_digit:
        thous_len_of_num += num_len_to_20[thous_digit]
        thous_len_of_num += 8       # len("thousand")
        num = num % 1000
    hun_len_of_num = 0
    hun_digit = num // 100
    if hun_digit:
        hun_len_of_num += num_len_to_20[hun_digit]
        hun_len_of_num += 7         # len("hundred")
        num = num % 100
        if num:
            hun_len_of_num += 3     # len("and")
    dec_len_of_num = 0
    if num < 20:
        dec_len_of_num += num_len_to_20[num]
    else:
        dec_digit = num // 10
        dec_len_of_num += decimals_len[dec_digit]
        dec_len_of_num += num_len_to_20[num % 10]

    return dec_len_of_num + hun_len_of_num + thous_len_of_num


"################ Problem 18 ######################"


def binomial(x, y):
    from math import factorial as fac
    try:
        return fac(x) // fac(y) // fac(x - y)
    except ValueError:
        return 0


def pascal(m):
    return [[binomial(x, y) for y in range(x + 1)] for x in range(m+1)]


def flat_list(original_list):
    return [item for l in original_list for item in l]


def product(iter_obj):
    prod = 1
    for i in iter_obj:
        prod *= i
    return prod


"################ Problem 21 ######################"


def check_amicable(num):
    am_cand = sum(divisors(num)[:-1])

    if sum(divisors(am_cand)[:-1]) == num:
        return am_cand
    else:
        return False
