stringg = "Learning_Python_is_easy"
substr1 = stringg[:]
print('Answer for [:] is ', substr1) #Output: Learning_Python_is_easy

substr2 = stringg[0:3]
print('Answer for [0:3] is ', substr2) #Output: Lea

substr3 = stringg[3:9]
print('Answer for [3:9] is ', substr3) #Output: rning_

substr4 = stringg[9:15]
print('Answer for [9:15] is ', substr4) #Output: Python

substr5 = stringg[-1:]
print('Answer for [-1:] is ', substr5) #Output: y

substr6 = stringg[::-1]
print('Answer for [::-1] is ', substr6) #Output: ysae_si_nohtyP_gninraeL

substr0 = stringg[0:14:2]
print('Answer for [0:14:2] is ', substr0) #Output: Lann_yh

substr7 = stringg[0:8].upper()
print('Answer for [0:8].upper() is ', substr7) #Output: LEARNING

print(stringg[-len(stringg):])  # Starts from -len(stringg) (first letter) to the end