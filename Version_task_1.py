from string import punctuation

inp = input('Enter the password: ')
low, upp, d, s = 0, 0, 0, 0

if len(inp) >= 14:
    for i in inp:
        if i.islower():
            low += 1

        if i.isupper():
            upp += 1

        if i.isdigit():
            d += 1

        if i in punctuation:
            s += 1

print("Strong password" if low >= 1 and upp >= 1 and d >= 1 and s >= 1 else "Weak password: ")

if low == 0 or upp == 0:
    print("- Password must contain both lowercase and uppercase characters")
if d == 0:
    print("- Password must contain digits")
if s == 0:
    print(f"- Password must contain  at least one punctuation character ({punctuation}")
if len(inp) < 14:
    print("- Password must be at least 14 characters long")
