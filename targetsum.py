# target sum using all numbers and arithmetic operators + or -
# find total number of ways
'''
given array of non-negative integers and a target integer, find the number
of ways you can make the target integer using all the integers from the
array and in the same sequence. you are only allowed to use + or -
operator between two elements . ( 1&lt;= n &lt;= 50,000 ) n is the size of array
'''

'''
Input:
Array: 1 2 1
Sum : 2
Output:
2
Explanation:
-1+2+1=2
+1+2-1=2
So, there are 2 ways to bring sum as 2 by adding/subtracting all
the elements from {1, 2, 1}

'''

def findtotalways(arr,i,k):
    if (i>=len(arr) and k!=0):
        return 0
    if (k==0 and i==len(arr)):
        return 1
    return (findtotalways(arr,i+1,k-arr[i]) + findtotalways(arr,i+1,k+arr[i]))


arr=[1,2,1]
k=2
print(findtotalways(arr,0,k))
