import random

print("Girando o tamborkkkk")
num = random.randint(1, 6)
print(f"O número sorteado foi: {num}")

if num == 6:
        print("SE FUDEU KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        lista = []
        try:
            while True:
                lista.append(bytearray(10**6))  
        except MemoryError:
            print("Overflow.")
else:
        print("Infelizmente sobreviveu.")





