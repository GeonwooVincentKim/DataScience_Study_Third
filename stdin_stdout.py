import sys, re

regex = sys.argv[0]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)

count = 0
for line in sys.stdin:
    count += 1

print(count)

a = input()

for i in range(a):
    b, c = map(int, input().split(" "))
    print("Case: #{0}: {1}".format((i + 1), b + c))
