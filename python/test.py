def calculateGCCOunt(str):
    count=0
    for ch in str:
        if ch=='G' or ch=='C':
            count+=1
        else:
            continue
    return str,count
def highestGCCount(listOfStr):
    highestStr=""
    highestCount=0

    for str in listOfStr:
        currentStr,currentCount=calculateGCCOunt(str)
        if currentCount>highestCount:
            highestCount=currentCount
            highestStr=currentStr
            percent=round(highestCount/len(highestStr)*100,2)
    return highestStr,percent

dna_samples = [
    "CCCffCGCGCGC",  # contains lowercase letters too
    "GCGC",
    "GC"
]

print(highestGCCount(dna_samples))