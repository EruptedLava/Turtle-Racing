# ============================================================
# intro
# ===========================================================
print("\n\n\tPoint to be noted:-\n\tDont use spaces in the text it will show error use underscore ( _ ) instead")

# ============================================================
# processing
# ============================================================
l = []
text  = input("\n\n\n\tEnter the text here : ")
for character in text:
    l.append(ord(character))


# ============================================================
# sub processing
# ============================================================
nl = []
for num in l:
    
    nl.append(bin(num))

final = " ".join(nl)
# ============================================================
# final output
# ============================================================
print(f"\n\n\n\tHere is your Binary code : {final} \n\n\n")
print("For Linux users:- To coppy the code just press ctrl + shift + c")
print("For Windows users:- To coppy the code just press ctrl + c")
print("\nMade By @Eruptedlava\n")
# ============================================================
# Extra Not Related to My Project
# ============================================================

'''
# a = ord("k")
# print(ord("k"))
# print(bin(a))

# print(int("1101011",2))
# print(chr(100))
'''
# ============================================================
