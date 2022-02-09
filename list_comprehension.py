from audioop import mul
import math
from functools import reduce


def main():
    natural_numers = [ num**2  for num in range(1,101) if num % 3 !=0 ]
    #print(natural_numers)
    reto = [mult for mult in range(1,10000) if mult % 36 == 0 ]
    #print(reto)

    # for i in range (1,100):
    #     if i % 3 !=0:
    #         dic_natural[i]=i**3

    dic_natural = {i: i**3 for i in range(1,100) if i%3 != 0 }
    # print(dic_natural)

    reto_2={j: round(math.sqrt(j),2) for j in range (1,1001) }
    #print(reto_2)

    palindrome = lambda string: string == string[::-1]
    #print(palindrome('ana'))

    my_list=[1,2,3,4,5,6,7,8,9]
    odd = [i for i in my_list if i%2 != 0]
    odd_filter = list(filter(lambda x: x%2 != 0, my_list))
    squares= [i**2 for i in my_list]
    squares_map = list(map(lambda x: x*2, my_list))
    all_multiplied=reduce(lambda a,b: a*b, my_list)
    
    print(all_multiplied)

if __name__ == '__main__':
    main()