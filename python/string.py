# b=("hello world")
# print(b[2:5])
# llo

# -------------------------------------------------------------

# slice from the start

# Get the characters from the start to position 5 (not included):
# b="hello world"
# print(b[:5])
# -------------------------------------------------------------

# Slice To the End

# By leaving out the end index, the range will go to the end:
# Get the characters from position 2, and all the way to the end:
# b="hello world"
# print(b[2:])
# -------------------------------------------------------------

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example

# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

# b="hello world"
# print(b[-1])

# -------------------------------------------------------------
# toremove space
# b="hello world"
# print(b.replace(" ",""))

# csv_data=[" john"," ss  ","vvvvv    "]
# clean=[i.strip() for i in csv_data]
# print(clean)

# csv_data=[" john"," ss  ","vvvvv    "]
# clean=(i.strip() for i in csv_data)
# print((clean))
# -------------------------------------------------------------
# Replace String
# Example

# The replace() method replaces a string with another string:

# b="hello world"
# print(b.replace("e","s"))
# -------------------------------------------------------------

# Split String

# The split() method returns a list where the text between the specified separator becomes the list items.# -------------------------------------------------------------
# b="hello, world"
# print(b.split(","))


# To add a space between them, add a " ":
# b="helloi"
# c="world"
# print(b+" "+c)
# -------------------------------------------------------------
# age=35

# print(f"age is {age}")

# -------------------------------------------------------------

# price=59
# txt=f"the price is {price:.2f}"
# print(txt)

# -------------------------------------------------------------
# def fact(n):
    # if n==0:
    #     return 1
    # else:
        # return n*(fact(n-1))

# r=fact(5)
# print(r)
# -------------------------------------------------------------

# a=12122
# s=str(a)
# print(s[::-1])

# -------------------------------------------------------------

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or i==n or j==0 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# -------------------------------------------------------------
# n=int(input("enter"))
# a,b=0,1
# for i in range(0,n):
#     if i==n-1:
#         print(a,end=" ")
#     a,b=b,a+b
# -------------------------------------------------------------
# txt="hello"
# x=txt[0]
# print(x)
# -------------------------------------------------------------
# x=5>3
# print(bool(0))
# -------------------------------------------------------------

# def myfuc(fnmae):
#     return fnmae
# res=myfuc("aa")
# print(res)

# def my_function(*kids):
#   print("The youngest child is " , *kids)

# my_function("Emil", "Tobias", "Linus")

# -------------------------------------------------------------
# from collections import Cou

# a='a'
# b='3'
# print(a*int(b))
# -------------------------------------------------------------

#REverse complement

# a="ATCG"
# res=""
# for i in a:
#     if i=="A":
#         res+="C"
#     elif i=="T":
#         res+="G"
#     elif i=="C":
#         res+="A"
#     elif i=="G":
#         res+="T"
# print(res)

#mapping

# a="ATCGTTaa"
# mapping = {"A": "C", "T": "G", "C": "A", "G": "T","a": "c", "t": "g", "c": "a", "g": "t"}
# res= "".join(mapping[ch] for ch in a)
# print(res)

# CGATGGcc

# -------------------------------------------------------------


# ## highest gc count(working meaningful)

# def calculate_gc_count(dna):
#     """Return (dna_string, GC_count)."""
#     gc_count = 0
#     for ch in dna:
#         if ch == "G" or ch== "C":
#             gc_count += 1
#     return dna, gc_count


# def highest_gc_content(dna_list):
#     """Return the DNA string with highest GC% and its percentage."""
#     highest_gc_dna = ""
#     highest_gc_count = 0

#     for dna in dna_list:
#         current_dna, current_gc_count = calculate_gc_count(dna)
#         if current_gc_count > highest_gc_count:
#             highest_gc_count = current_gc_count
#             highest_gc_dna = current_dna

#     gc_percentage = (highest_gc_count / len(highest_gc_dna)) * 100
#     return highest_gc_dna, gc_percentage


# # Example usage
# dna_samples = [
#     "CCCffCGCGCGC",  # contains lowercase letters too
#     "GCGC",
#     "GC"
# ]

# result_dna, result_gc_percent = highest_gc_content(dna_samples)
# print("DNA with highest GC content:", result_dna)
# print("GC%:", "{:.2f}".format(result_gc_percent))

# --------------------------------------------------------------------
# -------------------------------------------------------------
# longest common substring

# def longest_common_substring(strings):
#     # pick the shortest string (to minimize substring search space)
#     shortest = min(strings, key=len)
#     n = len(shortest)

#     # try all substring lengths from longest to shortest
#     for length in range(n, 0, -1): # 5 4 3 2 1
#         for start in range(n - length + 1):   # total no of subarrays
#             candidate = shortest[start:start+length] # slicing[a:b]
#             if all(candidate in s for s in strings):
#                 return candidate  # first found = longest
#     return "-1"


# # Example usage
# dna_strings = [
#     "GATTACA",
#     "TAGACCA",
#     "ATACA"
# ]

# print(longest_common_substring(dna_strings))  # Output: TA

# -------------------------------------------------------------

#calculate in a string:
#loop trough list of strings

# def reverse_complement(dna):
#     comp_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
#     return "".join(comp_map[base] for base in reversed(dna))


# def find_reverse_palindromes(dna):
#     results = []
#     n = len(dna)

#     for i in range(n):
#         for length in range(4, 13):  # length between 4 and 12
#             if i + length <= n:
#                 substring = dna[i:i+length]
#                 if substring == reverse_complement(substring):
#                     # store (1-based position, length, substring itself)
#                     results.append((i+1, length, substring))
#     return results


# # Example
# dna_str = "TCAATGCATGCGGGTCTATATGCAT"
# palindromes = find_reverse_palindromes(dna_str)

# for pos, length, seq in palindromes:
#     print(pos, length, seq)

# ----------------------------------------------------------------------======

# # k-mer substring

# def kmerCounts(dnaStr, k):
#     n = len(dnaStr)
#     kmers_count = {}  # dictionary to store counts

#     for i in range(n - k + 1):
#         kmer = dnaStr[i:i+k]
#         if kmer in kmers_count:
#             kmers_count[kmer] += 1
#         else:
#             kmers_count[kmer] = 1

#     return kmers_count

# # Example
# dna_str = "ATCGATCGA"
# k = 3
# print(kmerCounts(dna_str, k))

# ----------------------------------------------------------------------======

# with open("/home/Simon.P/Downloads/test.vcf","r") as f:
#     chr_records=[]
#     for line in f:
#         if line.startswith("##"):
#             continue
#         elif line.startswith("#"):
#             header=line.strip().lstrip("#").split("\t")
#             print(header)
#             break

# ----------------------------------------------------------------------======

# standard=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
# for i in header:
#     if i in standard:
#         print("standard")
#     else:
#         print("not")
# ----------------------------------------------------------------------======

# def is_vcf_sorted(vcf_file):
#     prev_chrom = None
#     prev_pos = -1

#     with open(vcf_file, "r") as f:
#         for line in f:
#             if line.startswith("#"):
#                 continue  # skip header/meta lines

#             parts = line.strip().split("\t")
#             chrom, pos = parts[0], int(parts[1])

#             if prev_chrom is None:  # first record
#                 prev_chrom, prev_pos = chrom, pos
#                 continue

#             # If same chromosome, positions must be ascending
#             if chrom == prev_chrom:
#                 if pos < prev_pos:
#                     return False, f"Unsorted at {chrom}:{pos} after {prev_chrom}:{prev_pos}"

#             # If chromosome changes, rely on lexicographic order
#             elif chrom < prev_chrom:
#                 return False, f"Chromosome order incorrect: {chrom} after {prev_chrom}"

#             prev_chrom, prev_pos = chrom, pos

#     return True, "VCF is sorted "
# vcf_path = "/home/Simon.P/Downloads/test.vcf"
# status, message = is_vcf_sorted(vcf_path)
# print(message)


# ----------------------------------------------------------------------======


# chrom_order={str(i): i for i in range(1,23)}
# print(chrom_order)
# chrom_order.update({"X":23,"Y":24,"MT":25})
# print(chrom_order)


# last_chrom= None
# with open("/home/Simon.P/Downloads/test.vcf","r") as f:
#     for line in f:
#         if line.startswith("#"):
#             continue

#         fields=line.strip().split("\t")
#         chrom=fields[0]

#         if chrom_order[chrom]<chrom_order[last_chrom]:
#             print("not sorted")
# ----------------------------------------------------------------------======

chrom_order = {str(i): i for i in range(1, 23)}
chrom_order.update({"X": 23, "Y": 24, "MT": 25, "M": 25, "chrM": 25})

last_chrom = None
last_pos = -1

with open("/home/Simon.P/Downloads/test.vcf", "r") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")
        chrom = fields[0].replace("chr", "") if fields[0].startswith("chr") else fields[0]
        pos = int(fields[1])

        # Normalize chromosome name to match chrom_order keys
        if fields[0] in ["chrM", "MT", "M"]:
            chrom = "MT"

        # Skip unknown chromosomes
        if chrom not in chrom_order:
            print(f"Skipping unknown chromosome: {chrom}")
            continue

        if last_chrom is None:
            last_chrom, last_pos = chrom, pos
            continue

        # Check chromosome order
        if chrom_order[chrom] < chrom_order[last_chrom]:
            print(f"Not sorted: {chrom}:{pos} comes after {last_chrom}:{last_pos}")
            break

        # If same chromosome, check position order
        if chrom == last_chrom and pos < last_pos:
            print(f"Not sorted: {chrom}:{pos} comes after {chrom}:{last_pos}")
            break

        last_chrom, last_pos = chrom, pos

# ----------------------------------------------------------------------======
def longestRepeatedSubstring(dnaStr):
    n = len(dnaStr)

    for length in range(n-1, 0, -1):  # start from longest
        seen = set()
        for start in range(n - length + 1):
            substr = dnaStr[start:start+length]
            if substr in seen:
                return substr  # first repeated substring of this length
            seen.add(substr)
            print(seen)
    return ""