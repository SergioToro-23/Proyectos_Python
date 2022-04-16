def arithmetic_arranger(problems,bool=False):

  
    #asing the problems in the variable but without the true statement
    #Real_problem  = [val for sublist in problems[0:-1] for val in sublist]
  Real_problem=problems
  ranges=range(0,len(problems))    
    
  #variables
  Error=None
  up=""
  middle=""
  down=""
  result=""
 
  if ranges[-1]<5:

    for i in ranges:
      list1=Real_problem[i].split()

      try:
        a=int(list1[0])
        b=int(list1[2])
      except:
        Error="Error: Numbers must only contain digits."
        break
      if len(list1[0])>4 or len(list1[2])>4:
        Error="Error: Numbers cannot be more than four digits."

      #calls function that adds spaces appropriately
      
      if len(list1[0])==1 or len(list1[2])==1:
        spUP=spaces(len(list1[0])+1,False)#space line on top
        spMid=spaces(len(list1[2])+1,False)#space line on mid
        dashes=spaces(len(list1[2])+1+len(list1[0]),True)#in this one it adds dashes
      elif len(list1[0])==len(list1[2]):
        spUP=spaces(2,False)#space line on top
        spMid=spaces(2,False)#space line on mid
        dashes=spaces(len(list1[2])+2,True)#in this one it adds dashes 
      else:
        spUP=spaces(len(list1[0]),False)#space line on top
        spMid=spaces(len(list1[2]),False)#space line on mid
        dashes=spaces(len(list1[2])+len(list1[0]),True)#in this one it adds dashes
      
      if list1[1]==('+'):
        #if is addition then it makes the operation and adds it to the string variable that returns
        c=a+b
        if i==ranges[-1]:
          #si es la ultima
          up=up+spMid+str(a)
          middle=middle+"+"+spUP[1:]+str(b)
          down=down+dashes
          if bool==True:
            result=result+(spaces(len(dashes)-len(str(c)),False))+str(c)#to acomodate it with the operators above
        else:
          up=up+spMid+str(a)+"    "
          middle=middle+"+"+spUP[1:]+str(b)+"    "
          down=down+dashes+"    "
          if bool==True:
            result=result+(spaces(len(dashes)-len(str(c)),False))+str(c)+"    "#to acomodate it with the operators above

      elif list1[1]==('-'):
        c=a-b
        if i==ranges[-1]:
          #si es la ultima
          up=up+spMid+str(a)
          middle=middle+"-"+spUP[1:]+str(b)
          down=down+dashes
          if bool==True:
            result=result+(spaces(len(dashes)-len(str(c)),False))+str(c)#to acomodate it with the operators above
        else:
          up=up+spMid+str(a)+"    "
          middle=middle+"-"+spUP[1:]+str(b)+"    "
          down=down+dashes+"    "
          if bool==True:
            result=result+(spaces(len(dashes)-len(str(c)),False))+str(c)+"    "#to acomodate it with the operators above
      
      else:
        Error="Error: Operator must be '+' or '-'."
        break
  else:
    Error="Error: Too many problems."
    print(['3801 - 2', '123 + 49'])
      #checks if there was any errors
      
  if Error is None:
    if bool==True:
      arranged_problems= up + "\n" + middle + "\n" + down + "\n" + result 
    else:
      arranged_problems=(up+'\n'+middle+'\n'+down)
      
  else:
    arranged_problems=Error
    
  return arranged_problems



def spaces(var,flag):
  space=""
  for i in range(0,var):
    #if its to arrange spaces or if its to arrange dashes
    if flag:
      space=space+"-"
    else:
      space=space+" "    
  return space



#a= "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
#b=arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
#print(a)
#print(b)


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(['3801 - 2', '123 + 49']))
#print(arithmetic_arranger(['3801 - 2', '123 + 49']))
