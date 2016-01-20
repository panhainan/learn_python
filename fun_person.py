#-*-coding:utf-8-*-
#def person(name,age,**kw):
#    print("name:",name,"age:",age,"other:",kw)
def person(name, age, *, city, job):
    print(name, age, city, job) 
   
