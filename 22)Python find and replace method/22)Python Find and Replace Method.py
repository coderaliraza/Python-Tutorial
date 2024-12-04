# replace() methode
string = "She is a beautiful and She is good dance"
print(string.replace(" ", "_"))
# replace any word
print(string.replace("is" , "still"))
# where position replace "is"
print(string.replace("is","was",1)) 
# where replace all is in your contact/ string
print(string.replace("is","was",2))




#find() methode
string = "She is a beautiful and she is good dance"
print(string.find("is")) # "is" started position in (4)
#e.g your insert "is" in first 
string = "is She is a beautiful and she is good dance"
print(string.find("is")) # "is" started position  zero(0)
#agar ap ko starting sy start ni karn hy to sap ek position dy sakty hy 
print(string.find("is",1))
#agar ap ko last waly is ki position ko find karn hy to ap kasy kary gy phly ap first waly is ki postion ko find kary gy
string = "She is a beautiful and she is good dance"
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)