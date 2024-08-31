-#merge sortt
def merge(arr,left,mid,right):
  n1=mid-left+1
  n2=right-mid
  l=[0]*n1
  r=[0]*n2
  for i in range(n1):
    l[i]=arr[left+i]
  for i in range(n2):
    r[i]=arr[mid+1+i]

  i=0
  j=0
  k=left
  while i<n1 and j<n2:
      if l[i]<=r[j]:
          arr[k]=l[i]
          k+=1
          i+=1
      elif l[i]>r[j]:
          arr[k]=r[j]
          k+=1
          j+=1

  while i<n1:
     arr[k]=l[i]
     k+=1
     i+=1
  while j<n2:
     arr[k]=r[j]
     k+=1
     j+=1


  

def merge_sort(arr,left,right):
  if left<right:
    
    mid=left+(right-left)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    merge(arr,left,mid,right)


arr=[5,4,3,2,1,66,75,101]
merge_sort(arr,0,len(arr)-1)
print(arr)
  
