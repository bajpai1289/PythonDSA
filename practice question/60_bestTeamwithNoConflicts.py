def bestTeamScore(scores: list[int], ages: list[int]) -> int:
    sortedTeam=sorted(list(zip(ages, scores)))
    scores.clear()
    ages.clear()
    for i, j in sortedTeam:
        ages.append(i)
        scores.append(j)
    print(scores, ages)


# print(bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
# print(bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))