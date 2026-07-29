from itertools import product

k = 10
alphabet = ["A", "C", "G", "T"]

with open("kmers.fa", "w") as out:
    for i, tup in enumerate(product(alphabet, repeat=k), start=1):
        seq = "".join(tup)
        out.write(f">{seq}\n")
        out.write(seq + "\n")
