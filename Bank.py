class bank:
    class employ:
        def __init__(s,n,sa,p):
            s.name=n
            s.sal=sa
            s.pos=p
            print(f"The name {n} i'm {p} and my salary is : {sa}")
    class customer:
        def __init__(self,n2,s2,l):
            self.name=n2
            self.sal=s2
            self.loan=l   
            print(f"I'm {n2} and my salary is : {s2} and loan : {l}")

p=bank.employ("Elsaraty",999999999,"Engineer")
h=bank.customer("Elsayad",16527586,0)


# class bank:
#     class employ:
#         def __init__(self,name,sal,pos):
#             self.name=name
#             self.sal=sal
#             self.pos=pos
#             print(f"i'm {pos} my name is {name} and my salary is :{sal}")
#     class customer:
#         def __init__(self,name,sal,loan):
#             self.name=name
#             self.sal=sal
#             self.loan=loan   
#             print(f"my name is {name} and my salary is : {sal} and loan : {loan}")

# c1=bank.employ("ahmed",10000,"developer")
# a1=bank.customer("saeed",12000,134567890)
