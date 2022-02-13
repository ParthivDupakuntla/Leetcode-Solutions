class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        alltuples = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):
            
            alltuples[user].append(site)
        
        patterns = Counter()
        for users, site in alltuples.items():
            patterns.update(set(combinations(site,3)))

        return max(sorted(patterns), key = patterns.get)
