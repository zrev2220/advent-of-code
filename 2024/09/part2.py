from dataclasses import dataclass


@dataclass
class File:
    id: int | None  # None if this represents empty space
    size: int


line = input().strip()
disk = []
file_id = 0
for i, digit in enumerate(list(line)):
    is_file = i % 2 == 0
    n = int(digit)
    disk.append(File(id=file_id if is_file else None, size=n))
    if is_file:
        file_id += 1

moved = set()

i = len(disk) - 1
while i > 0:
    file = disk[i]
    if file.id is None:
        i -= 1
        continue
    for j in range(i):
        item = disk[j]
        if item.id is not None or item.id in moved:
            continue
        if item.size >= file.size:
            disk[i] = File(id=None, size=file.size)
            disk[j : j + 1] = [file, File(id=None, size=item.size - file.size)]
            moved.add(file.id)
            break
    i -= 1

checksum = 0
i = 0
for file in disk:
    if file.id is not None:
        for j in range(file.size):
            checksum += (i + j) * file.id
    i += file.size
print(checksum)
