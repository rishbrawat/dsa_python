def compress(chars: list[str]):
    s = []
    occurred = 1
    write = 0

    for read in range(1, len(chars)):
        if chars[read-1] != chars[read]:
            s.append(chars[read])
            write += 1
            occurred = 1
        else:
            occurred += 1
            s.append(chars[read])
            s.append(occurred)
            write += 1
    return s

print(compress(chars=["a","a","b","b","c","c","c"]))