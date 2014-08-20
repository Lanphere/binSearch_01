
import re

def readList():
  '''read a sorted txt into memory, eliminate some extra chars in txt'''
  f = open('jargonStrippedLower.txt', 'r')
  lines = f.readlines()
  jList = []
  for line in lines:
    match = re.search(r'(\w+)', line)
    jList.append(match.group(0))
  return jList
  f.close()

def binSearch(word):
  '''do a binary search'''
  myList = readList()
  mid = (len(myList))//2
  low = 0
  high = len(myList)
  print ('init low value is {}, init mid value is {}, init high value is {}'.format(low, mid, high)) #test print
  print ('word index is {}'.format(myList.index(word))) #test print
  while high - low > 1:
    if myList[mid] == word:
      print ('found the word ' + word + '!')
      break
    elif myList[mid] > word:
      high = mid
      mid = (high+low)//2
      print ('low value is {}, mid value is {}, high value is {}'.format(low, mid, high)) #test print
    elif myList[mid] < word:
      low = mid
      mid = (high+low)//2
      print ('low value is {}, mid value is {}, high value is {}'.format(low, mid, high)) #test print
    else:
      print ('something is terribly wrong here.')

def main():
  binSearch('lasherism')


if __name__=="__main__":
  main()
