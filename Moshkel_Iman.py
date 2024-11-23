import math


def main():
    n = tedad_nomre()
    vazn_nomre = vazn_nomre_emtehan(n)
    nomre_n = mohasebe_nomre(vazn_nomre)
    r = tabdil2(math.ceil(nomre_n))
    return r


def tedad_nomre():
    n = input()
    return int(n)


def vazn_nomre_emtehan(n):
    vazn_nomre = []
    for i in range(n):
        vazn, nomre = input().split()
        vazn = int(vazn)
        vazn_nomre.append((vazn, nomre))
    return vazn_nomre


def mohasebe_nomre(vazn_nomre):#تابعی برای محاسبه معدل
    sum_ = 0
    t = 0
    for vazn, nomre in vazn_nomre:
        sum_ += vazn * tabdil1(nomre)
        t += vazn
    nomre_n = sum_ / t
    return nomre_n


def tabdil1(nomre_tosifi):
    nomre = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    return nomre[nomre_tosifi]


def tabdil2(nomre_adadi):
    nomre = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E', 0: 'F'}
    return nomre[nomre_adadi]


if __name__ == '__main__':
    nomre_nahayi = main()
    print(" moadel : ",nomre_nahayi)