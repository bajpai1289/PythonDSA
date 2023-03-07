def groupStrings(s: str):
    if not s:
        return ""
    
    compressed = ""
    current_char = s[0]
    current_count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            compressed += current_char + str(current_count)
            current_char = s[i]
            current_count = 1
    
    compressed += current_char + str(current_count)
    
    return compressed




print(groupStrings('aababbabbbbaa'))