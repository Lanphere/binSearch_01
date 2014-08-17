
import re

def readList():
  '''read a sorted txt into memory'''
  f = open('jargonStripped.txt')
  lines = f.readlines()
  jList = []
  for line in lines[:2100]:
    match = re.search(r'(\w+)', line)
    jList.append(match.group(0))
  return jList

def binSearch(word):
  '''do a binary search'''
  myList = readList()
  mid = (len(myList))//2
  low = myList.index(myList[0])
  high = myList.index(myList[-1])
  print ('init low value is {}, init mid value is {}, init high value is {}'.format(low, mid, high)) #test print
  print ('word index is {}'.format(myList.index(word))) #test print
  while high - low > 1:
    if myList[mid] == word:
      print ('found the word ' + word + ' in here!')
    elif myList[mid] > word:
      high = mid
      mid = (high+low)//2
      print ('low value is {}, mid value is {}, high value is {}'.format(low, mid, high)) #test print
    elif myList[mid] < word:
      low = mid
      mid = (high+low)//2
      print ('low value is {}, mid value is {}, high value is {}'.format(low, mid, high)) #test print
    else:
      print ('hmmm, something is terribly wrong here.')

def main():
  binSearch('alt')



if __name__=="__main__":
  main()
