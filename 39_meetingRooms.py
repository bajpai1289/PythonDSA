def meetingRooms(rooms: list[int]):
    data = []
    for s, e in rooms:
        data.append((s, +1))
        data.append((e, -1))
    data.sort()

    curr, ans=0,0
    for _, v in data:  #i dont care about the time any more, i care abut the change
        curr+=v
        ans=max(ans, curr)
    return ans



print(meetingRooms([[5,10],[15,20],[0,30]]))