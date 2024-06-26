class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
            
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1
    
# Time complexity: O(N)
# find indegree and outdegree of each person by counting the number of people who trust him and the number of people he trusts

# function findJudge(N, trust):
#     # Initialize a list to count trust levels, with N+1 elements set to 0
#     Trusted = array of size (N+1) initialized with 0

#     # Iterate through the trust list
#     for each pair (a, b) in trust:
#         # Decrease the trust level of person a
#         Trusted[a] -= 1
#         # Increase the trust level of person b
#         Trusted[b] += 1

#     # Iterate through the Trusted list starting from index 1 to N
#     for i from 1 to N:
#         # Check if the trust level of person i is equal to N-1
#         if Trusted[i] == N-1:
#             # If yes, return i as the judge
#             return i
    
#     # If no judge is found, return -1
#     return -1
