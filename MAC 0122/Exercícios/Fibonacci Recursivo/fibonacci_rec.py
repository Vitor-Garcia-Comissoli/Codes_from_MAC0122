def main():
    '''(None) -> None
    IMPRIME os menores número de fibonacci consecutivos fib0, fib1 tais 
    que a chamada euclidesR(fib0, fib1) atinge o limite da recursão.
    '''
    fib0 = 0  # i == 0
    fib1 = 1  # j == 1
    i = 0
    while True:
        try:
            d = euclidesR(fib0, fib1)
            if d != 1:
                print("SOCORRO!")
                return
            fib0, fib1 = fib1, fib0+fib1
            i += 1
        except RecursionError:
            print(f"euclidesR(F_{i}, F_{i+1}) atingiu limite de recursão")
            print(f"F_{i} = {fib0}")
            print(f"F_{i+1} = {fib1}")
            return 
  
#-----------------------------------------
def euclidesR(m, n):
    """ (int, int) -> int
    RECEBE dois inteiros m e n.
    Retorna o mdc de m e n.
    
    PRÉ-CONDIÇÃO: m >= 0, n >=0
    """
    if n == 0: return m
    return euclidesR(n, m%n)

if __name__ == "__main__":
    main()