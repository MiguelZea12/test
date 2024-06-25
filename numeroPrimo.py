class serieNum:
    def __init__ (self):
        self.prime_numbers = []
        
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False 
            return True
    
    def generate_primes(self, n):
        number = 2
        while len(self.prime) < n:
            if self.NumPrime(number):
                self.prime.append(number)
            number +=1
            
    def get_primes ( self):
        return self.prime
    
    def set_prime_count(self, n):
        while True:
            try:
                if n > 0:
                    self.ListNumPrime(n)
                    break
                else: 
                    print('El numero ingresado es menor a 0, ingrese uno mayor')
            except ValueError:
                print('Ingrese un valor entero valido.')
                
if __name__ == "__main__":
    serie = serieNum()
    n = int(input('Ingrese la cantidad de numero que desea en su lista: '))
    serie.setListCount(n)
    print(f'Este es la serie de numero primos: {serie.getLis()}')
            
        