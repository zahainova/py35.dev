from calc_package.menu import display_menu, calc_help
from calc_package.utils import extract, result

def main():
    while True:
        display_menu()
        choice = input("| Enter choice (h|c|q): ".title()).lower()

        if choice == 'q':
            print('Thank you for using Super Calc!')
            break

        if choice == 'h':
            calc_help()
            continue

        if choice == 'c':
            entry = input("Enter x operator y (e.g., 2 + 2): ")
            a, b, operator = extract(entry)

            if not operator:
                calc_help("Invalid format or unsupported operator.")
                continue

            res, err = result(a, b, operator)
            if err:
                print(err)
            else:
                print(f"{a} {operator} {b} = {res}")

if __name__ == "__main__":
    main()