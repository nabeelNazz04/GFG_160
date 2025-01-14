'''
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.
'''
def findMajority(arr):

  #using hash maps
  n=len(arr)
  res=[]
  freq={}
  for ele in arr:
    freq[ele]=freq.get(ele,0)+1#if the number already present in hash map then element+1 or create a new key 0+1  
  for ele, cnt in freq.items():#The function iterates over each key-value pair (ele and cnt) in freq.
    if cnt>n//3:
      res.append(ele)
  if len(res)==2 and res[0]>res[1]:
    res[0],res[1]=res[1],res[0]
  return res