from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from decimal import Decimal
import gmpy2

with open('k1.pub', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

n1 = public_key.public_numbers().n

with open('k2.pub', 'rb') as key_file2:
    public_key2 = serialization.load_pem_public_key(key_file2.read())

n2 = public_key2.public_numbers().n


with open('text1.txt', 'r') as file:
    content = file.read()

c1 = int(content.strip())


with open('text2.txt', 'r') as file2:
    content2 = file2.read()

c2 = int(content2.strip())

with open('k3.pub', 'rb') as key_file3:
    public_key3 = serialization.load_pem_public_key(key_file3.read())

n3 = public_key3.public_numbers().n


with open('text3.txt', 'r') as file3:
    content3 = file3.read()

c3 = int(content3.strip())

with open('k4.pub', 'rb') as key_file4:
    public_key4 = serialization.load_pem_public_key(key_file4.read())

n4 = public_key4.public_numbers().n


with open('text4.txt', 'r') as file4:
    content4 = file4.read()

c4 = int(content4.strip())

with open('k5.pub', 'rb') as key_file5:
    public_key5 = serialization.load_pem_public_key(key_file5.read())

n5 = public_key5.public_numbers().n


with open('text5.txt', 'r') as file5:
    content5 = file5.read()

c5 = int(content5.strip())

with open('k6.pub', 'rb') as key_file6:
    public_key6 = serialization.load_pem_public_key(key_file6.read())

n6 = public_key6.public_numbers().n


with open('text6.txt', 'r') as file6:
    content6 = file6.read()

c6 = int(content6.strip())


with open('k7.pub', 'rb') as key_file7:
    public_key7 = serialization.load_pem_public_key(key_file7.read())

n7 = public_key7.public_numbers().n


with open('text7.txt', 'r') as file7:
    content7 = file7.read()

c7 = int(content7.strip())

def chinese_remainder_theorem(n, a):
    """
    Löse System von Kongruenzgleichungen x ≡ a_i (mod n_i)
    mit den teilerfremden Moduln n_i und Resten a_i.
    Rückgabe ist x modulo das Produkt aller n_i.
    """
    from functools import reduce
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('Kein multiplikatives Inverses')
        else:
            return x % m

    prod = reduce(lambda a, b: a*b, n)
    result = 0
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        result += a_i * modinv(p, n_i) * p
    return result % prod

n = [n1, n2, n3, n4, n5, n6, n7]
a = [c1, c2, c3, c4, c5, c6, c7]
x = chinese_remainder_theorem(n, a)
print(x) # Ausgabe: 23

n = gmpy2.mpz(x)
root, is_exact = gmpy2.iroot(n, 7)

print("Die 7. Wurzel aus n ist:", root)
print("die Wurzel geht auf?: ",is_exact)