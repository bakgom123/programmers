def solution(s):
#     word = list(map(str, s))
#     countP = 0
#     countY = 0
#     for a in word:
#         if a == "p" or a == "P":
#             countP += 1
#         elif a == "y" or a == "Y":
#             countY += 1
#     if countP != countY:
#         return False

#     return True
    return s.lower().count('p') == s.lower().count('y')