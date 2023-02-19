#passwords[n] contains passwords
#dict_words[m]  contains m weak passwords
#password is weak if
'''
•password in dictionary
•substring of password is word in dictionary
•password is all numerical
•all characters is upper or lower
•password is shorted than 6 characters
input:
n=5
passwords = ['iliketoCoDe', "teaMAKEsmehappy", "abracaDabra", "password", "blackcoffeelsthebest"]
common_words = ["coffee", "coding", "happy"]
output-strong, weak, string, strong, weak
'''


def getPasswordStrength(passwords, common_words):
    res=[]
    for i in passwords:
        if i.islower() or i.isupper() or len(i)<6 or any(b in i for b in common_words):
            res.append('weak')
        else: 
            res.append('strong')
    return res

# print(getPasswordStrength(['iliketoCoDe', "teaMAKEsmehappy", "abracaDabra", "pasSword", "blackcoffeeISthebest"],
#                           ["coffee", "coding", "happy"]))

print(getPasswordStrength(passwords=['hello', 'chargoR', 'pass123'], common_words=['hello', '123','password', 'xyz', '999']))
# print(getPasswordStrength())
