def main():
    n , m = No_OF_city()
    cities = city(n)
    airlines = air_line(m)
    print_k(cities , airlines)

def print_k(cities,airlines):
    for city in cities:
        k = airlines.get(city, [])
        if k :
            print(len(k))#تعداد شهر مقصد
            for end in k:
                print(end) #نام شهر مقصد
        else:
            print(0)

def city(n):
    cities = [input() for _ in range(n)]
    return cities

def air_line(m):
    airlines = dict()
    for i in range(m):
        start , end = input("enter start and end city : ").split()
        k = airlines.get(start,[]) #لیست شهر هایی که میشه از مبدا به آن ها رفت
        k.append(end)
        airlines[start] = k
    return airlines

def No_OF_city():
    n , m = input().split()
    n = int(n)
    m = int(m)
    return n , m



if __name__ =='__main__':
    main()
