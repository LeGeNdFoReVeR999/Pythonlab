number = int(input("Enter a number: "))
arr = []

# Find all prime numbers less than the input number
for i in range(2, number):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        arr.append(i)

print("Prime numbers less than", number, ":", arr)

# Check if any two primes sum up to the number
found = False
for i in range(len(arr)):
    for j in range(i, len(arr)):  # include j=i to allow (5,5) type pairs
        if arr[i] + arr[j] == number:
            found = True
            print(f"{arr[i]} and {arr[j]} are prime numbers that sum to {number}")
            break
    if found:
        break

if not found:
    print("No prime pair found that sums to", number)
