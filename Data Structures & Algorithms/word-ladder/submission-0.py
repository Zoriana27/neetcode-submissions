class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        #creating the adjacency list
        patternToWords = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patternToWords[pattern].append(word)

        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbour in patternToWords[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            res += 1
        return 0


        