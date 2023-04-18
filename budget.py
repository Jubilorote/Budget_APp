import math
class Category:
  def __init__(self, name, ledger=None):
      self._name= name
      if ledger is None:
          ledger=[]
          self.ledger= ledger
    

#On ajoute le nom de la catégorie dans la liste ledger
  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
      self.get_balance()

#Les retraits et les dépenses
  def withdraw(self, amount, description=""):
      if self.get_balance() >=0: #Si on peut faire le retrait
          self.ledger.append({"amount": amount*-1, "description": description})
          return True
      else: #Si on ne peut pas faire le retrait
          return False

  def get_balance(self):
      budget=0
      for i in self.ledger:
          budget= budget + i["amount"]
      return budget

  def transfer(self, amount, othername):
      try: 
          self.withdraw(amount, "Transfer to "+ str(othername._name))
          othername.deposit(amount, "Transfer from "+ str(self._name))
          return True
      except:
          return False

  def check_funds(self, amount):
      if amount > self.get_balance():
          return False
      else:
          return True


  def __repr__(self):
      total=self.get_balance() # L'argent qu'il reste
      temp= (30-len(str(self._name)))//2 #30-La longueur de la category divisé par 2 = le nombre de *
      ligne= temp*"*"+str(self._name)+(30-temp-len(str(self._name)))*"*"+"\n" #La première ligne
      for i in self.ledger:
          ligne= ligne +i["description"][:23]+(30-len(str(i["amount"]))-len(i["description"][:23]))*" "+ str(i["amount"])+"\n"
      ligne= ligne +"Total: "+ str(total)
      return ligne


      
def create_spend_chart(categories):
  ligne1="Percentage spent by category\n"
  pourcentage=[]
  longest_cat=0
  part=[]
  for j in categories: #dans toutes les categories
      temp=0
      if len(j._name) > longest_cat:
          longest_cat=len(j._name)
      for i in j.ledger: #dans tout les amount
          if i["amount"]<0:
              print(i["amount"])
              temp= temp +i["amount"]
      pourcentage.append(temp)
  tot=sum(pourcentage)
  for i in pourcentage:
      temp=round_down((i/tot)*100,-1)
      part.append(temp)
  #print(part)
  j=100
  ligne2=""
  
  while j>=0:
      listo=""
      for p in part:
          if p>=j:
              listo+=" "+"o"+" "
          else:
              listo+="   "
      if j==0:
          ligne2+="  "+str(j)+"|"+ listo+"\n"
      elif j==100:
          ligne2+=str(j)+"|"+ listo+"\n"
      else:
          ligne2+=" "+str(j)+"|"+ listo+"\n"
      j=j-10
  ligne3="    "+(3*(len(part)))*"-"+"-"+"\n"
  ligne4=""
  j=0
  while j<longest_cat:
      ligne4+=3*' '
      for i in categories:
          try:
              ligne4+=2*" "+i._name[j]
          except:
              ligne4+=3*" "
      ligne4+= "\n"
              
      j=j+1
  return(ligne1+ligne2+ligne3+ligne4)
  
  #print( ligne1+ligne2+ligne3)


def round_down(n, decimals=0): 
  multiplier = 10 ** decimals 
  return math.floor(n * multiplier) / multiplier 
