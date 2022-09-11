from time import process_time

known_primes = []

def check_prime(option):
    global known_primes
    if option < 4 and option > 0: 
        if option == 1:
            return False
        elif option == 2 or option == 3:
            known_primes.append(option)
            return option
    else:
        for prime in known_primes:
            if option % prime == 0:
                return False
        known_primes.append(option)
    return option


for unknown_if_prime in range(1,200,2):
    check_prime(unknown_if_prime)

print(known_primes)
print(f"The answer is {sum(known_primes)}.")


print("Process time: " + str(process_time()) + " seconds")

#This literally takes half an hour.