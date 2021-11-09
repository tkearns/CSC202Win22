def bin_search(target, low, high, list_val):
   if(high<low):
      print(str(target) + " not found")
      return None
   
   mid = (low+high)//2
   if (list_val[mid] == target):
      return mid
   elif (list_val[mid] < target):
      return bin_search(target, mid+1, high, list_val)
   else:
      return bin_search(target, low, mid-1, list_val)

# list_val =[0,1,2,3,4,7,8,9,10]
# low = 0
# high = len(list_val)-1

# print(bin_search(4, low, high, list_val))


      
# see the following link for animations
#   http://www.cs.usfca.edu/~galles/visualization/Algorithms.html
def max_list(tlist):
   """ finds the max of a list of numbers """
   if (len(tlist) == 1):
      return tlist[0]
   else:
      return max(maxlist(tlist[:len(tlist)-1]), tlist[len(tlist)-1])

def reverse(tempstr):   #returns max of a list of numbers
   if (len(tempstr) == 1):
      return tempstr[0]
   else:
      return tempstr[len(tempstr)-1]+reverse(tempstr[:len(tempstr)-1])
