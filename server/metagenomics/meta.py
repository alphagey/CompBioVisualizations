# Richness takes a frequency map(dict). It returns the richness of the frequency map(dict)
# (i.e., the number of keys in the map(dict) corresponding to nonzero values.)
def richness(sample):
    count = 0

    for freq in sample.values():
        if freq > 0:
            count += 1

    return count


# Multiple Richness
def richnessMatrix(allMaps):
    arr = []

    for freqMap in allMaps:
        arr.append(richness(freqMap))

    return arr


# Evenness
def simpsonsIndex(sample):
    total = 0

    for freq in sample.values():
        total += freq

    sIndex = 0.0

    for freq in sample.values():
        sIndex += pow(float(freq) / float(total), 2.0)

    return sIndex


# Multiple Evenness
def simsonsMatrix(allMaps):
    arr = []

    for freqMap in allMaps:
        arr.append(simpsonsIndex(freqMap))

    return arr


def frequencyMap(arr):
    freqMap = {}

    for val in arr:
        if val in freqMap.keys():
            freqMap[val] += 1
        else:
            freqMap[val] = 1

    return freqMap

#modified jaccard distance calculator to return a json of relevant information
def jaccardDistance(sample1, sample2):
    sumOfMins = 0
    sumOfMaxs = 0


    returninfo = {}

    for key, val1 in sample1:
        if key in sample2.keys():
            val2 = sample2[key]
            if (val1 < val2):
                returninfo[key] = 1
            else:
                returninfo[key] = 2
            sumOfMins += MinTwo(val1, val2)
            sumOfMaxs += MaxTwo(val1, val2)
        else:
            sumOfMaxs += val1
            returninfo[key] = 2

    for key, val2 in sample2:
        if key not in sample1.keys():
            sumOfMaxs += val2
            returninfo[key] = 1

    returninfo["minsum"] = sumOfMins
    returninfo["maxsum"] = sumOfMaxs

    returninfo["jaccard"] = 1 - float(sumOfMins) / float(sumOfMaxs)
    return returninfo


def MinTwo(a, b):
    if a < b:
        return a
    return b


def MaxTwo(a, b):
    if a > b:
        return a
    return b


def brayCurtisDistance(sample1, sample2):
    sumOfMins = 0
    total = 0

    returninfo = {}
    #iterate through first dict
    for key, val1 in sample1.items():
        if key in sample2.keys():
            val2 = sample2[key]
            if (val1 < val2):
                returninfo[key] = 1
            else:
                returninfo[key] = 2
            sumOfMins += MinTwo(val1, val2)
            total += val1 + val2
        else:
            total += val1
            returninfo[key] = 2
    #iterate through second dict
    for key, val2 in sample2.items():
        if key not in sample1.keys():
            total += val2
            returninfo[key] = 1
    #calculate bray curtis
    returninfo["summin"] = sumOfMins
    returninfo["total"] = total
    returninfo["avg"] = float(total) / 2.0
    returninfo["bray-curtis"] = 1 - float(sumOfMins) / (float(total) / 2.0)
    return returninfo
