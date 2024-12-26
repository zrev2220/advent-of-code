line = input().strip()
disk = []
file_id = 0
for i, digit in enumerate(list(line)):
    is_file = i % 2 == 0
    n = int(digit)
    disk.extend(([file_id] if is_file else [None]) * n)
    if is_file:
        file_id += 1

i = 0
j = len(disk) - 1
while i < j:
    while disk[i] is not None and i < j:
        i += 1
    while disk[j] is None and j > i:
        j -= 1
    disk[i], disk[j] = disk[j], disk[i]

checksum = sum([i * file_id for i, file_id in enumerate(disk) if file_id is not None])
print(checksum)
