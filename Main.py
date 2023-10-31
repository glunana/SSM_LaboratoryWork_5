x = (0, 0, 0, 0, 1, 1, 1, 1)
y = (0, 0, 1, 1, 0, 0, 1, 1)
z = (0, 1, 0, 1, 0, 1, 0, 1)
F = (0, 1, 1, 0, 0, 1, 0, 0)

table = []
for i in range(8):
    table.append((x[i], y[i], z[i], F[i]))

print("Таблиця істинності: \n x  y  z  F")
for row in table:
    print(row)
def dualF(F):
    reversed = []

    for row in table:
        reversed.append(int(not row[3]))
    dual = reversed[::-1]

    return dual
print("Двоїста F*: ")
print(dualF(F))

def ddnfForF():
    ddnfResult = ""

    for i in range(len(F)):
        if not F[i]:
            continue

        ddnf = ""

        ddnf += "x" if x[i] else "x̅"
        ddnf += "∧"

        ddnf += "y" if y[i] else "y̅"
        ddnf += "∧"

        ddnf += "z" if z[i] else "z̅"

        ddnfResult += f"({ddnf}) v "

    return ddnfResult[:-3]

result = ddnfForF()
print("ДДНФ: ")
print(result)

def dknfForF():
    dknfResult = ""

    for i in range(len(F)):
        if F[i]:
            continue

        dknf = ""

        dknf += "x̅" if x[i] else ("x")
        dknf += "v"

        dknf += "y̅" if y[i] else ("y")
        dknf += "v"

        dknf += "z̅" if z[i] else ("z")

        dknfResult += f"({dknf}) ∧ "

    return dknfResult[:-3]

result = dknfForF()
print("ДКНФ: ")
print(result)
def xor(list1, list2):
    xorResult = []

    for i in range(len(list1)):
        xorResult.append(list1[i] != list2[i])

    return (xorResult)

def yatsMethod(F):
    if len(F) == 1:
        return list(F)

    firstHalf = F[:len(F) // 2]
    secondHalf = F[len(F) // 2:]

    return yatsMethod(firstHalf) + yatsMethod(xor(firstHalf, secondHalf))

def polynomialZhegalkin(x, y, z, F):
    polynominalResult = ""

    bits = yatsMethod(F)

    for i in range(len(bits)):
        if not bits[i]:
            continue

        if x[i]:
            polynominalResult += "x∧"
        if y[i]:
            polynominalResult += "y∧"
        if z[i]:
            polynominalResult += "z∧"

        polynominalResult = polynominalResult[:-1]

        polynominalResult += " ⊕ "

    return polynominalResult[:-3]

print("Поліном Жегалкіна:")
print(polynomialZhegalkin(x, y, z, F))

def const0(F):
        if all (value == 0 for value in F):
            print("Функція зберігає константу 0.")
        else:
            print("Функція не зберігає константу 0.")
const0(F)


def const1(F):
    if all(value == 1 for value in F):
        print("Функція зберігає константу 1.")
    else:
        print("Функція не зберігає константу 1.")
const1(F)

def selfDual(F):
    if F == dualF(F):
        print("Функція самодвоїста.")
    else:
        print("Функція не самодвоїста.")
selfDual(F)

def monotone(x, y, z, F):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):

            if ( x[i] >= x[j] and y[i] >= y[j] and z[i] >= z[j] and F[i] < F[j] ):
                return True
    return False

if monotone(x, y, z, F):
    print("Функція монотонна.")
else:
    print("Функція не монотонна.")

def linear(x, y, z, F):
    if "∧" not in polynomialZhegalkin(x, y, z, F):
        print("Функція лінійна.")
    else:
        print("Функція не лінійна.")
linear(x, y, z, F)
    















