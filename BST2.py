#it ia now Tues morning
class Node:
   def __init__(self, content=None, left=None, right=None):
      self.content = content
      self.left = left
      self.right = right

   def contents (self):
      return self.content

   def insert(self, data):
      if (self.content == None ):
         self.content == data
      elif (data < self.content) :
         if(self.left==None):
            self.left = Node(data)
         else:
            self.left.insert(data)
      else:
         if(self.right==None):
            self.right = Node(data)
         else:
            self.right.insert(data)
         
   def postPrint(self):
      if (self.content == None ):
         print("empty")
      if (self.left != None) :
         self.left.postPrint()
      if (self.right != None) :
         self.right.postPrint()
      print(self.content)

t=Node(6)
t.insert(3)
t.insert(5)
t.insert(7)
t.insert(4)
t.postPrint()


  
