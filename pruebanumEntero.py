class serie_num:
    def __init__(self):
        self.prime_numbers = []
    
    def is_prime(self, num) :
        if num < 2:
            return False
        return not any(num % i == 0 for i in range(2, int(num ** 0.5) + 1))
        
    def generate_primes(self, num):
        number = 2
        while len(self.prime_numbers) < num:
            if self.is_prime(number):
                self.prime_numbers.append(number)
            number += 1
            
    def get_primes(self):
        return self.prime_numbers
    
    def set_primes_count(self, num):
        while True:
            try:
                if num > 0:
                    self.generate_primes(num)
                    break
                else:
                    print('El numero que ingreso es menor a cero, añade uno mayor')
                    
            except ValueError:
                print('Invalidado. Ingrese un numero entero valido')
                
if __name__ == "__main__":
    serie = serie_num()
    number = int(input('Ingrese la cantidad de numero que desea en la lista: '))
    serie.set_primes_count(number)
    print(f'Esta es la lista de primos: {serie.get_primes()}')
    