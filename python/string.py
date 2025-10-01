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

-------------------------------------------------------------


## highest gc count(working meaningful)

def calculate_gc_count(dna):
    """Return (dna_string, GC_count)."""
    gc_count = 0
    for ch in dna:
        if ch == "G" or ch== "C":
            gc_count += 1
    return dna, gc_count


def highest_gc_content(dna_list):
    """Return the DNA string with highest GC% and its percentage."""
    highest_gc_dna = ""
    highest_gc_count = 0

    for dna in dna_list:
        current_dna, current_gc_count = calculate_gc_count(dna)
        if current_gc_count > highest_gc_count:
            highest_gc_count = current_gc_count
            highest_gc_dna = current_dna

    gc_percentage = (highest_gc_count / len(highest_gc_dna)) * 100
    return highest_gc_dna, gc_percentage


# Example usage
dna_samples = [
    "CCCffCGCGCGC",  # contains lowercase letters too
    "GCGC",
    "GC"
]

result_dna, result_gc_percent = highest_gc_content(dna_samples)
print("DNA with highest GC content:", result_dna)
print("GC%:", "{:.2f}".format(result_gc_percent))

--------------------------------------------------------------------
-------------------------------------------------------------
longest common substring

def longest_common_substring(strings):
    # pick the shortest string (to minimize substring search space)
    shortest = min(strings, key=len)
    n = len(shortest)

    # try all substring lengths from longest to shortest
    for length in range(n, 0, -1): # 5 4 3 2 1
        for start in range(n - length + 1):   # total no of subarrays
            candidate = shortest[start:start+length] # slicing[a:b]
            if all(candidate in s for s in strings):
                return candidate  # first found = longest
    return "-1"


# Example usage
dna_strings = [
    "GATTACA",
    "TAGACCA",
    "ATACA"
]

print(longest_common_substring(dna_strings))  # Output: TA

----------------------------------------------------------------------======
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

ex:
dnas="ATACATACA"
op:ATACA
-------------------------------------------------------------

calculate in a string:
loop trough list of strings

def reverse_complement(dna):
    comp_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(comp_map[base] for base in reversed(dna))


def find_reverse_palindromes(dna):
    results = []
    n = len(dna)

    for i in range(n):
        for length in range(4, 13):  # length between 4 and 12
            if i + length <= n:
                substring = dna[i:i+length]
                if substring == reverse_complement(substring):
                    # store (1-based position, length, substring itself)
                    results.append((i+1, length, substring))
    return results


# Example
dna_str = "TCAATGCATGCGGGTCTATATGCAT"
palindromes = find_reverse_palindromes(dna_str)

for pos, length, seq in palindromes:
    print(pos, length, seq)

----------------------------------------------------------------------======
3. Given a DNA sequence, find the longest substring which is a reverse complement palindrome.


def revComp(dna):
    mapping = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(mapping[base] for base in reversed(dna))

def revCompPal(dna):
    longest = ""  # track longest palindrome
    n = len(dna)

    for i in range(n):
        for length in range(4, n - i + 1):  # allow up to full length
            subs = dna[i:i+length]
            if subs == revComp(subs):
                if len(subs) > len(longest):
                    longest = subs  # update if longer
    return longest
----------------------------------------------------------------------======

# k-mer substring

def kmerCounts(dnaStr, k):
    n = len(dnaStr)
    kmers_count = {}  # dictionary to store counts

    for i in range(n - k + 1):
        kmer = dnaStr[i:i+k]
        if kmer in kmers_count:
            kmers_count[kmer] += 1
        else:
            kmers_count[kmer] = 1

    return kmers_count

# Example
dna_str = "ATCGATCGA"
k = 3
print(kmerCounts(dna_str, k))

----------------------------------------------------------------------======

with open("/home/Simon.P/Downloads/test.vcf","r") as f:
    chr_records=[]
    for line in f:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header=line.strip().lstrip("#").split("\t")
            print(header)
            break


standard=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
for i in header:
    if i in standard:
        print("standard")
    else:
        print("not")
----------------------------------------------------------------------======

----------------------------------------------------------------------======


chrom_order={str(i): i for i in range(1,23)}
# print(chrom_order)
chrom_order.update({"X":23,"Y":24,"MT":25})
# print(chrom_order)


last_chrom= None
with open("/home/Simon.P/Downloads/test.vcf","r") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields=line.strip().split("\t")
        chrom=fields[0]

        chrom_clean = chrom.upper()
        if chrom_clean.startswith("CHR"):
            chrom_clean = chrom_clean[3:]  # remove 'CHR' prefix
        if chrom_clean == "M":             # map M → MT
            chrom_clean = "MT"

        if last_chrom is not None:
            if chrom_order[chrom_clean]<chrom_order[last_chrom]:
                print("not sorted")
        last_chrom = chrom_clean
----------------------------------------------------------------------======


----------------------------------------------------------------------======

chrom_order = {str(i): i for i in range(1, 23)}
chrom_order.update({"X": 23, "Y": 24, "MT": 25})

last_chrom = None
is_sorted = True   # assume sorted unless proven otherwise

with open("/home/Simon.P/Downloads/test.vcf", "r") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")
        chrom = fields[0]

        chrom_clean = chrom.upper()
        if chrom_clean.startswith("CHR"):
            chrom_clean = chrom_clean[3:]
        if chrom_clean == "M":
            chrom_clean = "MT"

        if last_chrom is not None:
            if chrom_order[chrom_clean] < chrom_order[last_chrom]:
                is_sorted = False
                break   # stop early if unsorted
        last_chrom = chrom_clean

# 🔹 Final result
if is_sorted:
    print("VCF is sorted ✅")
else:
    print("VCF is NOT sorted ❌")

----------------------------------------------------------------------======


def get_lcs(str1, str2, len1, len2):
    """
    Returns the Longest Common Subsequence (LCS) string between str1 and str2.
    """
    # Base case: if either string is empty
    if len1 == 0 or len2 == 0:
        return ""

    # If last characters match
    if str1[len1 - 1] == str2[len2 - 1]:
        return get_lcs(str1, str2, len1 - 1, len2 - 1) + str1[len1 - 1]

    # If last characters do not match, take the longer LCS
    else:
        lcs1 = get_lcs(str1, str2, len1 - 1, len2)
        lcs2 = get_lcs(str1, str2, len1, len2 - 1)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


# Example
first_string = "AGGTAB"
second_string = "GXTXAYB"

# Get LCS string
lcs_string = get_lcs(first_string, second_string, len(first_string), len(second_string))
# Print both
print("Longest Common Subsequence:", lcs_string)
print("Length of LCS:", len(lcs_string))
