import​ tabula 

def​ ​rank​(​path​): 
 ​    ​dict​=​ {} 
 	a​ ​=​ ​tabula​.​readfile​(​"PDF"​,​page​  ​=​ ​"1"​) 
 ​    ​a​=​ ​a​.​splitlines​() 
 ​    ​for​ ​i​ ​in​ ​range​(​0​,​len​(​a​)): 
 ​        ​dict​[​a​[​i​].​split​()[​0​]] ​=​ ​a​[​i​]​.split​()[​1​] ​#enollment number to marks 
  
  
  
  
 ​dict1​=​ ​rank​(​input​()) 
 ​path​ ​=​input​() 
 ​a​ ​=​ ​tabula​.​readfile​(​"PDF"​,​pages​ ​=​"all"​) 
 ​a​ ​=​ ​a​.​splitline​() 
 ​for​ ​i​ ​in​ ​range​(​0​,​len​(​a​)): 
 ​    ​enr​=​ ​a​[​i​].​split​[​1​] 
 ​    ​if​(​dict1​[​enr​]):​#logical t val xomparison 
 ​        ​dict1​[​enr​] ​=​ ​a​[​i​].​split​()[​6​]​##dictionary appendment 
 ​        ​print​(​dict1​[​enr​])