def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals=sorted(intervals, key=lambda x:x[1])
    prev_s, prev_e=intervals[0]
    count=1
    for s,e in intervals:
        if s<prev_e:
            pass
        else:
            prev_s, prev_e=s,e
            count+=1
    return len(intervals)-count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))