print (" CGPA CALULATOR")


a = str(input(" name of 1 subject :"))
b = str(input("  name of 2 subject   :"))
c = str(input(" name of 3 subject   :")) 
e = str(input(" name of 4 subject   :"))     
f = str(input(" name of 5 subject   :"))
  


print(" UNIT TEST AND SEMESTER MARKS ")
a1 = int(input(" total unit test and semester marks 1 subject /100 :"))
gp_a= int((a1/100)*100)
a3=print(" Gp of",a,gp_a)

b1 =int( input(" total unit test and semester marks 2 subject /100 :"))
gp_b = int((b1/100)*100)
a4 = print("Gp of ",b,gp_b)

c1 = int(input(" total unit test and semester marks 3 subject /100 :"))
gp_c = int((c1/100)*100)
a5 =print("Gp of ",c,gp_c)

e1 = int(input(" total unit test and semester marks 4 subject /100 :"))
gp_e = int((e1/100)*100)
a6 = print("Gp of ",e,gp_e)

f1 = int(input(" total unit test and semester marks 5 subject /100 :"))
gp_f = int((f1/100)*100)
a7 =print("Gp of ",f,gp_f)


g = input(" creadit = "+a)
print (g)
h = input(" creadit = " + b ) 
print(h)
i = input(" creadit = " + c  )
print(i)
j = input(" creadit =  " + e )
print(j)
k = input(" creadit of  = " + f )
print(k)



sum = int(gp_a+gp_b+gp_c+gp_e+gp_f) / int(int(g) + int(h) +int(i) +int(j) +int(k)) 
print ("CGPA ", sum)

if sum > 0.3 or sum < 0.3 :
    print(" Congrats !! but Next make more ")
elif 0.3 < 0.4:
    print(" Congratulations !!")