class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        
        if len(A) < 1 :
            return []
        
        res = []
        curLineLen = len(A[0])
        start = 0
        i = 1
        while i < len(A) :
            #print "%s %d %d %d" % (A[i], curLineLen, curLineLen + 1 + len(A[i]), B)
            if curLineLen + 1 + len(A[i]) <= B :
                curLineLen = curLineLen + 1 + len(A[i])
                i = i + 1
                continue
            res.append(self.lineJustify(A, start, i, B))
            start = i
            curLineLen = len(A[i])
            i = i + 1
        
        if curLineLen != 0:
            res.append(self.leftJustify(A, start, len(A), B))
            
        return res
            
    def lineJustify(self, A, start, end, count) :
        res = ""
        wordCount = end - start
        if wordCount == 1 :
            return self.leftJustify(A, start, end, count)
        spacesCount = wordCount - 1
        
        relevantWords = A[start:end]
        #print "relevantWords = %s" % ",".join(relevantWords)
        charCount = 0
        for w in relevantWords :
            charCount = charCount + len(w)
        #print "charCount = %d" % charCount
        while charCount < count:
            for iw in range(len(relevantWords) - 1) :
                if (charCount >= count):
                    break
                relevantWords[iw] = relevantWords[iw] + " "
                charCount = charCount + 1
                
        return "".join(relevantWords)
        
    def leftJustify(self, A, start, end, count) :
        res = ""
        for i in range(start,end) :
            if i != start :
                res = res + " "
            res = res + A[i]
        return res + " " * (count - len(res))
            
