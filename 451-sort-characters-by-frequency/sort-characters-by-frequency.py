class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = Counter(s)
        dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        newstr = ""
        for i in dict1.keys():
            newstr = newstr + i*dict1[i]
        return newstr