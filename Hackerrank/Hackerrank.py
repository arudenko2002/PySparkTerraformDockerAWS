def distinct(ar):
    rez = ""
    d = dict()
    for c in ar:
        if not c in d:
            d[c] = ""
            rez += c
    return rez


def merge_the_tools(string, k):
    # your code goes here
    arrays = []
    for i in range(0, len(string), k):
        arrays.append(string[i:i + k])
    for ar in arrays:
        print(distinct(ar))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

