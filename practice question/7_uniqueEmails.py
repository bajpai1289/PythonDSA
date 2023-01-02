emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
local=[i.split('@') for i in emails]
for i in range(len(local)):
    local[i][0]=local[i][0].split('+')[0]

for i in range(len(local)):
    local[i][0]=local[i][0].replace(".", "")
print(local)
result = ["@".join(i) for i in local]
result = set(result)
print(result)
print(len(result))






