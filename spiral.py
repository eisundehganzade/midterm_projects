HOPS = int(input("Enter number of hops: ")) 
P = [0, 0]  
ARROW = [+1, +1]  
BOARD = [[' ' for _ in range(2 * (HOPS + 1 - (HOPS % 2)))] for _ in range(2 * ((HOPS + 1) // 2) - 1)]  # ایجادِ صفحه‌ی خالی
CENR, CENC = 2 * ((HOPS + 1) // 4), 4 * (HOPS // 4)
JUJU = [CENR, CENC]  
BOARD[CENR][CENC] = '*'  
for HOP in range(HOPS - 1):  
    LEN = 1 + HOP // 2  
    P[HOP % 2] += ARROW[HOP % 2] * LEN  
    PR, PC = JUJU
    for _ in range(2 * LEN):  
        PC += 2 * (1 - HOP % 2) * ARROW[HOP % 2]  
        PR -= (HOP % 2) * ARROW[HOP % 2]  
        BOARD[PR][PC] = '-'  
    JUJU = [PR, PC]  
    BOARD[PR][PC] = '*'  
    ARROW[HOP % 2] *= -1  
print(*P, sep=", ")  
for r in BOARD[:]:  
    for c in r:
        print(c, end="")
    print()