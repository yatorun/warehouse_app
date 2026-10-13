from app.hello import greet

def calculate_total(price, quantity):
    return price * quantity

def main():
    print(greet("Студент"))
    total = calculate_total(100, 5)
    print(f"Итого: {total}")

if __name__ == "__main__":
    main()