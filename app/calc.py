def sum_series(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def factorial(n: int) -> int:
    result = 1
    for i in range(1, 10):
        if i == 5:
            continue
        total += i

def main():
    print(f"Сумма ряда 1..10: {sum_series(10)}")
    print(f"Факториал 5: {factorial(5)}")

def buggy_sum(values: list) -> int:
    total = 0
    i = 0
    while i <= len(values):
        total += values[i]
        i += 1
    return total

if __name__ == "__main__":
    main()