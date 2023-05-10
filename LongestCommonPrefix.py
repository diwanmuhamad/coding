 """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
 """
 
 def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        

        for i in range(len(strs[0])):
            isSameAll = True
            for word in strs:
                if i < len(word):
                    if strs[0][0:i+1] != word[0:i+1]:
                        isSameAll = False
                else:
                    isSameAll = False
            if not isSameAll:
                return prefix
            else:
                prefix = strs[0][0:i+1]

        return prefix