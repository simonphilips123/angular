# def calculateGCCOunt(str):
#     count=0
#     for ch in str:
#         if ch=='G' or ch=='C':
#             count+=1
#         else:
#             continue
#     return str,count
# def highestGCCount(listOfStr):
#     highestStr=""
#     highestCount=0

#     for str in listOfStr:
#         currentStr,currentCount=calculateGCCOunt(str)
#         if currentCount>highestCount:
#             highestCount=currentCount
#             highestStr=currentStr
#             percent=round(highestCount/len(highestStr)*100,2)
#     return highestStr,percent

# dna_samples = [
# "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
# "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
# "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
# ]

# print(highestGCCount(dna_samples))
# -------------------------------------------------------------

def gcContent(str):
    gcCount=0;
    for ch in str:
        if ch =="G" or ch == "C":
            gcCount += 1
        else:
            continue
    return str,gcCount

def lowestGcContent(listStr):
    # highestGcCount=0
    # highestGcStr=""
    lowestGcStr, lowestGcCount = gcContent(listStr[0])
    for str in listStr[1:]:
        currStr,currGcCount=gcContent(str)
        if currGcCount<lowestGcCount:
            lowestGcCount=currGcCount
            lowestGcStr=currStr
    return lowestGcCount,lowestGcStr

# Example usage
dna_samples = [
    "CCCffCGCGCGCcc",  # contains lowercase letters too
    "GCGC",
    "GC",
]

print(lowestGcContent(dna_samples))


# -------------------------------------------------------------

## longest common substring

# def longestCommonSubstring(listOfStr):
#     shortest=min(listOfStr)
#     n=len(shortest)

#     for length in range(n,0,-1):
#         for start in range(n-length+1):
#             candidate=shortest[start:start+length]
#             if all(candidate in s for s in listOfStr):
#                 return candidate

#     return "-1"

# # Example usage
# dna_strings = [
#     "GATTACA",
#     "TAGACCA",
#     "ATACA"
# ]

# print(longestCommonSubstring(dna_strings))  # Output: TA

# -------------------------------------------------------------

# ## reverse complement palindrome

# def revComplement(dna):
#     mapping={"A":"T","T":"A","C":"G","G":"C"}
#     return "".join(mapping[base] for base in reversed(dna))

# def complementPalindrome(dna):
#     results=[]
#     n=len(dna)

#     for i in range(n):
#         for length in range(4,13):
#             if i+length<=n:
#                 substring=dna[i:i+length]
#                 if substring==revComplement(substring):
#                     print(substring)
#                     results.append((i+1,length,substring))
#     return results

# # # Example
# dna_str = "TCAATGCATGCGGGTCTATATGCAT"
# comp = complementPalindrome(dna_str)

# print(comp)
