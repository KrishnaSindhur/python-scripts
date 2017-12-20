# A Simple RSA algorithm to encrypt plain text and decrypt the plain text.

# this function finds the number prime or not
def prime(a):
    for i in range(2, a/2 + 1):
        if a % i == 0:
            return 0
        return 1

# this is Euclid's algorithm to find gcd
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# this function is used to encrypt and decrypt using public and private keys
def rsa(text, key, n):
    i = 1
    rem = 1
    while i <= key:
        rem = (rem * text) % n
        i = i + 1
    return rem

""" main function here will asks user to enter message and displays
the decrypted message and checks for prime and also find gcd. """

def main():
    ct = []
    k = []
    a = []
    # this while loop work like do-while loop in c.
    while True:
        print "Enter two large prime numbers"
        p, q = map(int,raw_input().split())
        if prime(p) and prime(q):
            break
        else:
            print "Incorrect Input try again"
            print
    n = p * q
    z = (p-1) * (q-1)
    # this while loop work like do-while loop in c.
    while True:
        e = int(raw_input("Enter the prime number for encryption relative to %d: " %(z)))
        if gcd(e, z) != 1:
            print "Incorrect input try again"
            print
        else:
            break
    # this d gives private key
    for d in range(2,z):
        if (e * d) % z == 1:
            break
    # more number of print statement makes users easy to enter keyboard input
    print "public key are (%d, %d)" %(e,n)
    print "private key are (%d, %d)" %(d,n)
    text = raw_input("enter the text: ")
    for i in range(len(text)):
        a.append(ord(text[i]))
    for i in range(len(text)):
        ct.append(rsa(a[i],e,n))
    # encrypted form of text you entered
    print "cipher text"
    print ct
    print "Plain decrypted text:"
    for i in range(len(text)):
        g = ((rsa(ct[i],d,n)))
        k.append(g)
    characters = [chr(n) for n in k]
    res = "".join(characters)
    print res


if __name__ == '__main__':
    main()
