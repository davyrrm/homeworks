import my_math

def main():
    choice = input("Тебе нужна комбинаторика или геометрия? (к/г): ").lower()
    if choice == 'к':
        func_choice = input("Выбери функцию: факториал (f), перестановка (p), или комбинации (c): ").lower()
        if func_choice == 'f':
            n = int(input("Введите n: "))
            print(my_math.combinatorics.factorial(n))
        elif func_choice == 'p':
            n = int(input("Введите n: "))
            r = int(input("Введите r: "))
            print(my_math.combinatorics.permutations(n, r))
        elif func_choice == 'c':
            n = int(input("Введите n: "))
            r = int(input("Введите r: "))
            print(my_math.combinatorics.combinations(n, r))
    elif choice == 'г':
        func_choice = input("Выбери функцию: прямоугольник (r), квадрат (s), треугольник (t), или сфера (sp): ").lower()
        if func_choice == 'r':
            length = float(input("Введите длину: "))
            breadth = float(input("Введите ширину: "))
            print(my_math.areas.rectangle_area(length, breadth))
        elif func_choice == 's':
            side = float(input("Введите сторону: "))
            print(my_math.areas.square_area(side))
        elif func_choice == 't':
            base = float(input("Введите основание: "))
            height = float(input("Введите высоту: "))
            print(my_math.areas.triangle_area(base, height))
        elif func_choice == 'sp':
            radius = float(input("Введите радиус: "))
            print(my_math.areas.sphere_area(radius))

if __name__ == '__main__':
    main()

