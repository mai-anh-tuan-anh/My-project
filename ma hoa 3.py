nfor _ in range(int(input())):
    s = input()
    mid = len(s) // 2
    nuadau, nuasau = list(s[:mid]), list(s[mid:])
    xoaydau = sum(ord(c) - 65 for c in nuadau)
    xoaysau = sum(ord(c) - 65 for c in nuasau)
    nuasau = [chr((ord(c) - 65 + xoaysau) % 26 + 65) for c in nuasau]
    nuadau = [chr((ord(c) - 65 + xoaydau + ord(nuasau[i]) - 65) % 26 + 65) for i, c in enumerate(nuadau)]
    print("".join(nuadau))
    