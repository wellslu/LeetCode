class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        lookout_dict = {}
        for word in strs:
            word_sort = sorted(word)
            word_index = ''
            for w in word_sort:
                word_index+=w
            if word_index in lookout_dict.keys():
                answer[lookout_dict[word_index]].append(word)
            else:
                lookout_dict[word_index] = len(lookout_dict)
                answer.append([word])
        return answer
