def form_line(letters, size):
    s = ""
    for i in range(len(letters)):
        s += letters[i] + "-"
    s = s[0:len(s) - 1]
    print(s)
    rs = s[::-1]
    print(rs)
    rez =rs+s[1:]
    length = int((4 * size -3 - len(rez))/2)
    rez = "".join(["-"]*length) + rez + "".join(["-"]*length)
    return rez


def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefefghijklmnoprstuvwxyz"
    letters = alphabet[:size]
    rar = []
    for i in range(size):
        let = letters[i:]
        s = form_line(let, size)
        rar.append(s)

    rrar = rar[::-1]
    result = rrar + rar[1:]
    for ind in result:
        print(ind)



if __name__ == '__main__':
    #n = int(input())
    n = 5
    n = 22
    n = 27
    print_rangoli(n)