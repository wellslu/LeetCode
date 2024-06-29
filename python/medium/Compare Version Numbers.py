class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        len1 = len(version1)
        version2 = version2.split('.')
        len2 = len(version2)
        index = 0
        while True:
            if index == len1 and index == len2:
                return 0
            elif index == len1 and index < len2:
                for i in range(index, len2):
                    if int(version2[i]) > 0:
                        return -1
                return 0
            elif index < len1 and index == len2:
                for i in range(index, len1):
                    if int(version1[i]) > 0:
                        return 1
                return 0
            else:
                if int(version1[index]) > int(version2[index]):
                    return 1
                elif int(version1[index]) < int(version2[index]):
                    return -1
            index+=1
