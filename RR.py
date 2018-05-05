import operator
tt=0
exe_p=0
idle_chk=False
class process:

   def _init_():
      self.at =0 
      self.bt =0
      self.ip=0
      self.rb=0
      self.rip=0
      self.io=False
      self.ipr
      self.qt=0
def initialinput(): 

    count=input("gow many proces you want to enter")
    list=[process() for index in range(count)]
    ready=[]
    wait=[]
    for index in range(count):
      
       list[index].at=input("enter the arrival time")
       list[index].bt=input("enter the burst time ")
       list[index].ip=input("enter the input time" )

    list.sort(key=operator.attrgetter('at')) 
def frominit():
    for index in range(count):
        if(list[index]['at']<=tt):
            ready[ready_p]=list[index]
            del list[index]
            idle_chk=True
    return True
def execute():
    for index in range(ready[exe_p][qt]):
        tt+=1


def fromwait():
    for index in range(wait_p):
         if(tt==wait[index][ipr]):
             ready[ready_p]=wait[index]
             ready_p+=1
             idle_chk=True
             
exe=[]
def main():
    for index in range(quantum):
        if(frominit()):
            print()
       
        if(tt==ready[0][ip]):
            exe[0]=ready[0]
            wait[wait_p]=ready[cur_p]
       
        if(ready[cur_p][at]):
            print()
        if(idle_chk==False):
            print("cpu idle")
        if(ready[0][bt]==0):

         
            i=0
    for ke in list:
        print (list[i].at)
        i+=1

