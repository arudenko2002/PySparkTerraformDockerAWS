def gen_words(s, letters):
    ss = list(s)
    rez = set()
    for i in range(len(ss)):
        c = ss[i]

        if c in letters:
            sss = ss[i:]
            for ind in range(len(sss)):
                rez.add("".join(sss[:ind+1]))
    return rez

def count_occ(s, occ):
    i = 0
    counter = 0
    while len(s)>0:
        if s.startswith(occ):
            counter += 1
        i += 1
        s = s[1:]
    return counter

def count_all(string, rez):
    counter = 0
    for ind in rez:
        counter += count_occ(string, ind)
    return counter


def minion_game(string):
    vowels = "AEIOU"
    consonants = "QWRTYPSDFGHJKLZXCVBNM"
    rez = gen_words(string, vowels)
    counter_kevin = count_all(string, rez)
    rez = gen_words(string, consonants)
    counter_stuart = count_all(string, rez)
    if  counter_stuart > counter_kevin:
        print("Stuart", counter_stuart)
    elif counter_stuart == counter_kevin:
        print("Draw")
    else:
        print("Kevin", counter_kevin)


if __name__=="__main__":
    s = "BANANA"
    minion_game(s)