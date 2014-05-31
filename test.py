with open('index.html') as f:
    lines = f.read().splitlines()
lines.insert(6, "Win")
point = 0
while point < len(lines):
	lines[point] = lines[point] + "\n"
	print lines[point]
	point = point + 1

with open('index.html', 'w') as file:
    file.writelines( lines )