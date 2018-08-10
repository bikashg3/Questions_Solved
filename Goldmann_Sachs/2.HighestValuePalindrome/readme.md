#Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example 0110 is valid, 0011 is not.

Given a string representing the starting number and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string -1 if it's impossible to create a palindrome under the contstraints.

##Input Format

The first line contains two space-separated integers,  (the number of digits in the number) and  (the maximum number of changes allowed), respectively. 
The second line contains an -digit string of numbers that you are to attempt to make palindromic.

##Constraints 0<n<=10^5
            0<=k<=10^5

Each character i in the number is an integer where 0<=i<=9
##Output Format

Print a single line with the largest number that can be made by changing no more than  digits; if this is not possible, print -1.

##Sample Input 0

4 1
3943
##Sample Output 0

3993

##Sample Input 1

6 3
092282
##Sample Output 1

992299
##Sample Input 2

4 1
0011
##Sample Output 2

-1
