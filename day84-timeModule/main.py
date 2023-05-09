import time

def usingWhile():
    i = 0
    while i<5000:
        i+=1
        print(i)
    pass
def usingFor():
    for i in range(5000):
        print(i)
    pass


# init = time.time()
# usingFor()
# timeFor = time.time()-init

# init = time.time()
# usingWhile()
# timeWhile = time.time()-init


# print(f"\nWhile Time: {timeWhile}, For Time: {timeFor}")

unFormatedTime = time.localtime()
formatedTime = time.strftime("%Y-%m-%d %H:%M:%S", unFormatedTime)
print(formatedTime)