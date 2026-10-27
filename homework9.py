#99

k, n = map(int, input().split())

page = (n - 1) // k + 1
line = (n - 1) % k + 1

print(page, line)

#177

n = int(input())
digits = []

for i in range(4):
    digits.append(n % 10)
    n //= 10

if len(set(digits)) == 4:
    print("YES")
else:
    print("NO")

#291

n = int(input)
print(n[::-1])

#818

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v


n = int(input())
m = int(input())
k = int(input())

box = MoneyBox(n)
box.add(m)

print(box.can_add(k))

#820

class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)

        while len(self.buffer) >= 5:
            print(sum(self.buffer[:5]))
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer


buf = Buffer()
buf.add(1, 2, 3)
buf.add(4, 5, 6)
buf.add(7, 8, 9, 10, 11, 12)
print(buf.get_current_part())