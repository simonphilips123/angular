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


# # k-mer substring

# def longest_common_substring(strings):
#     # pick the shortest string (to minimize substring search space)
#     shortest = min(strings, key=len)
#     n = len(shortest)

#     # try all substring lengths from longest to shortest
#     for length in range(n, 0, -1):
#         for start in range(n - length + 1):   #total no of subarrays
#             candidate = shortest[start:start+length]
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
