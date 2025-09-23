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
#     "CCCffCGCGCGC",  # contains lowercase letters too
#     "GCGC",
#     "GC"
# ]

# print(highestGCCount(dna_samples))


# -------------------------------------------------------------

## longest common substring

def longestCommonSubstring(listOfStr):
    shortest=min(listOfStr)
    n=len(shortest)

    for length in range(n,0,-1):
        for start in range(n-length+1):
            candidate=shortest[start:start+length]
            if all(candidate in s for s in listOfStr):
                return candidate

    return "-1"

# Example usage
dna_strings = [
    "GATTACA",
    "TAGACCA",
    "ATACA"
]

print(longestCommonSubstring(dna_strings))  # Output: TA
