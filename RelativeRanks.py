def findRelativeRanks(score: list[int]) -> list[str]:
    sortedscore = score.copy()
    sortedscore.sort(reverse=True)
    answer = [0]*len(score)
    ranks = dict() 
    for i in range(len(sortedscore)):
        ranks[sortedscore[i]] = i + 1
    print(ranks)
    for i in range(len(score)):
        k = ranks.get(score[i])
        if k == 1: 
            answer[i] = "Gold Medal"
        elif k == 2: 
            answer[i] = "Silver Medal"
        elif k == 3: 
            answer[i] = "Bronze Medal"
        else: answer[i] = str(ranks[score[i]])
    return answer

score = [5,4,3,2,1]
A = findRelativeRanks(score)
print(A)

