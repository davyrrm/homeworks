import m_module

def main():
    choice = input("Do you need combinatorics or geometry? (c/g): ").lower()
    if choice == 'c':
        func_choice = input("Choose function: factorial (f), permutations (p), or combinations (c): ").lower()
        if func_choice == 'f':
            n = int(input("Enter n: "))
            print(my_math.combinatorics.factorial(n))
        elif func_choice == 'p':
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(my_math.combinatorics.permutations(n, r))
        elif func_choice == 'c':
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(my_math.combinatorics.combinations(n, r))
    elif choice == 'g':
        func_choice = input("Choose function: rectangle_area (r), square_area (s), triangle_area (t), or sphere_area (sp): ").lower()
        if func_choice == 'r':
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            print(my_math.areas.rectangle_area(length, breadth))
        elif func_choice == 's':
            side = float(input("Enter side: "))
            print(my_math.areas.square_area(side))
        elif func_choice == 't':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print(my_math.areas.triangle_area(base, height))
        elif func_choice == 'sp':
            radius = float(input("Enter radius: "))
            print(my_math.areas.sphere_area(radius))

if __name__ == '__main__':
    main()
