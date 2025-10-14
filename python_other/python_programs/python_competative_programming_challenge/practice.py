##############################################********PYTHON COMPETATIVE PROGRAMMING CHALLENGE*********#################################################
#####################################################Day1[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFJoYTAxcjV3Q2RnQWJQSTRHOGFFc01oenZMUXxBQ3Jtc0trYlF1LS1fM3hhTUJXeURPODhmbW93MjZhcld5bTZuTHFSb3Y1QWVKVzBCTG50QjVQM191b3F0VHdsdnR5RkpQdnpiUmV1NWlZcDIxNzk2QlZ1VGxRc0xJcVV6SmwzOE1BSDY3aXJ1RjdvNld0OFZORQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprint-alternate-elements-of-an-array%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DBasic%26sortBy%3Dsubmissions&v=rsubrskHQ4s# Problem Statement:You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0
class Solution:
    def getAlternates(self, arr):
        # Code Here
        output=[]
        for i in range(len(arr)): 
            if i%2==0:
                output.append(arr[i])
            else:
                continue

        return output


t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTJJNDJCYzlObnBTeUxreF8waGd0TUYwSU1jd3xBQ3Jtc0tsY2hoTzRrVTFiSnFUU1huVFRpSXU4TjI2WkJ0b3pmemprdXNXbndmWERIeGNwR0tGZHBQUjNFZ190MFRCMEEzbllMWXBuRHZmNHZoQVdibkdUY05ud2xad0pjU2ZNbGZudFRnRDhKc2p4c0RfRnpENA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-odd-even%2F0&v=rsubrskHQ4s
class Solution:
    def countOddEven(self, arr):
        odd = 0
        even = 0
        for number in arr:
            if number % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        return odd, even



if __name__ == "__main__":
    # Testcase input
    testcase = int(input())
    for i in range(testcase):
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countOddEven(arr)
        print(*res)
        print("~")
#####################################################Day2#######################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
class Solution:
    def convertFive(self, n):
        # Code here
        num_string = str(n)
        result_string=''
        for char in num_string:
            if char=='0':
                result_string=result_string+'5'
            else:
                result_string=result_string+char
        return result_string
        


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
#[Assignments1]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0hJTFNtR0Y3VW9YUkFwYzc5UjZsTUF1bHZqQXxBQ3Jtc0trTVlESHhGQThBSzNpWDNJODZETVY5M1FFVFVPNzBlLWVkUl91RlpvYmZUT1NlYk1ramRmRmMzMWw2ZlpfaUhSRjdlX1ZDWVNZZ1J3QXVSYXJUdXpSWUhnMXkwUktPeHU2RmZveWxRZzIyWlVDQ0ZuYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fchange-the-string3541%2F0&v=3b34ZOgT2A4
class Solution:
    def conCat(self,s1,s2):
        # code here
        concat_string = s1 + s2
        return concat_string


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        solObj = Solution()
        print(solObj.conCat(s1,s2))
#[Assignments2]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
class Solution:
    def modify(self, s):
        # code here
        if s[0].islower():
            return s.lower()
        else:
            return s.upper()
    
        

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
######################################################Day3######################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw//www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw##
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        for i in range(n+1):
            sum=sum+i
        return sum
        


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        obj = Solution()
        res = obj.seriesSum(n)
        print(res)
        print("~")
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazlMVXN4S1gxQW50bmZDMTlTMXZBNHpLMlI1UXxBQ3Jtc0tuQUVPcGN5blEzc1JjbG02czY2Z1pzczBFME5rWjlMTlJQdG1vOXpmUnVTV2JDVlJ5Qk9qSzM4T2RJU2pDSEx2VG5wTmZrZ2NINklsY1pEcDJzWjR4bzJQYXZOSFp2MWJQUGZwYjhkMWtjNDA3WDhDMA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-array2326%2F0&v=qC9FFshDvHw
class Solution:
    def arraySum(self, arr):
        # code here
        sum = 0
        for num in arr:
            sum = sum + num
        return sum
   		


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.arraySum(arr)
        print(ans)
        tc = tc - 1
        print("~")
######################################################Day4#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjNpUTZycGdUdGF3Y0ZROWhkeXlpdWxoZzlLd3xBQ3Jtc0trUzlVd3FQWEtZLUE2ZnMzYzlJZmVRbnZPMTZBemNzY2FXV2RqcXBuUllLekZJRlZMSjZZc25aWm1MWWNDS3dfN0JpZ0Q4NzZwbU5TZmdqczllcExjdU9UQWZpOWtTRzV5OHQwbEhUVHAtU0NpUUNUdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-camel3348%2F0&v=ac2x4QXg-48##
class Solution:
    def count (self,s):
        # your code here
        lower=0
        upper=0
        special=0
        numeric=0
        whitespace=0
        for char in s:
            if char.isupper():
                upper=upper+1
            elif char.islower():
                lower=lower+1
            elif char.isnumeric():
                numeric=numeric+1
            elif char.isspace():
                whitespace=whitespace+1
            else:
                special=special+1
        return upper,lower,numeric,special
    
    

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0tuN25IV2FsRmtmalNBT3BRdkN1ZDJ2cGd4d3xBQ3Jtc0tuREpLLUZyWlNMZnFjdV9wQlF5b3czZEExZjJUUEM1c3FWTm1FdjB0YVkyTGdGVVhSWE0ycTlWWTJDcE9CMjluTFlkTEFoR3lCeDBoWVlNUWtYd0kwSVpMTWFIQUp6Q0hKd2ZtSkNXeXJwNmRSRWp1SQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-type-of-characters3635%2F0&v=ac2x4QXg-48
class Solution:
    def countCamelCase (self,s):
        # your code here
        humps =0
        for char in s:
            if char.isupper():
                humps=humps+1
        return humps



t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))
    print("~")
######################################################Day5##########################################################################
#[Problem Statement]:https:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa21uYnVBdWI3LTZhU3VJakVJaEdsSHZKWGNMUXxBQ3Jtc0ttaWszVjhlYkdtd2NraWtkLTRSZ25JQzYtaWd1SHhsb3hFMWdzVG9LSXcxZjZOdHhfdHViaTBQNzVQRmJXXzljVnJEeFJEcTBjMVl6SlFOQVRlQnRsYmo0TUxhcl9jd3RhQlR0aW1CRWg0M290b2RMTQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Flargest-element-in-array4009%2F0&v=fwn9902r32s
from typing import List
class Solution:
    def largest(self, arr):
        # code here
        result=float('-inf')
        for num in arr:
            if num>result:
                result=num
            else:
                continue
        return result



t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
       
ob = Solution()
res = ob.largest(arr)
print(res)
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE5YTUFUOVFYdHVzeUdjV3BJc3N5eTdhWkpQUXxBQ3Jtc0ttbDF5ZnZvRExUcUtsSmxLT3VJZm9tUWp0V21NYnV0bFVHUGM2MU5UQjlWSHRvSXU4Nk9mTUg0NXRtVWlPcF96YlplR3A2U3cxNEM5UmF2WWJjSFVCeWt3Ul8yLVQzenRSTXd6TUhpbHBVVURXOUx1UQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsearching-a-number0324%2F0&v=fwn9902r32s
from typing import List
class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1  # 1-based indexing
                
        return -1



t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
######################################################Day6#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmNKU2p2YnBUbUNqdDc1cnpNTU1mWnFxcHAyUXxBQ3Jtc0tta0xFQVhJTFZIWklIWE9MaDNXZjNiVkYtcXBvRTJjdW9LQk1nWm9qYVFodnEyVGtIeUM0TkhUX3drQmJTU2JPU1VyX0FTOV9Sa2tKenVfU1dsNGVtYnR4ZnBGNk1YWmNETDlHZlBuemVPY3NoanY5aw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcheck-if-a-string-is-isogram-or-not-1587115620%2F0&v=lkyfIVevg3s
class Solution:
    #Your code here
    #Function to check if a string is Isogram or not.
    def isIsogram(self,s):
        value1=''
        for i in range(len(s)):
            value1=s[i]
            for j in range(i+1,len(s)):
                value2=s[j]
                if value1==value2:
                    return False
                else:
                    continue
        return True
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTV1RjNYdjNWeWZuQWZobS1lRFdpSGR6c29XZ3xBQ3Jtc0tuOHE4djFidUpwREVVZkNxYmdQRHRpbjBWVXZrSDNKQlljQ3FEb1lzQ0JwRldNRHJBM1RVRnlHbFFJRUpFYjZxRnhWLXRPZm5zMmRzUUpLQ0xLN3c3WWpqQlVPS2VoTFVEMVRBYWg0WjA3SmJaRGVhOA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fjava-delete-alternate-characters4036%2F0&v=lkyfIVevg3s
class Solution:
    def delAlternate (ob, S):
        # code here 
        S=S[::2]
        return S
        



######################################################Day7[Problem Statement]########################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lJMUNBNTNockJKcENZcWVPd0draHkwSkVOZ3xBQ3Jtc0trOWxNRmc2QjRfVzJaLVRZNkU1UFRjUWY4eV9JTDZKY2hzNU4tNWhMNUE3cFBzc2hoei0tQUdSSS1XSHBsSzVBd29PcDdHMmFhSFZ3SUVXVGhuc3dFVFU1blZqcS01MFRYV0NHQVE1c29Mb0xvRFVsUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprime-number2314%2F0&v=5mTsiek4uHk
class Solution:
    def isPrime(self, n):
        # code here
        start=2
        end=n//2
        for x in range(start,end):
            if n%x==0:
                return False
        return True
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUoxRm9sSkNQMGxYQ2JhMUpTNzl2Q1U0UzB5d3xBQ3Jtc0tsYU1maXVUMER6M2hCOG9JSzZrRUdpak5kQVNSSTROWk5kLUZJTkJlOFNNXzRsUUJ0MkpNeTMyanY1bmVPRGpBTjNSRzNJVHpwVlFfWVNKN0lTcUh0WnZDS3ZYbnI0LWU4Wk41R1pWTU4zeEVlMzlZUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fswap-kth-elements5500%2F0&v=5mTsiek4uHk
class Solution:
    def swapKth(self, arr, k):
        # Code Here
       for i in range(len(arr)):
           if i==k:
               temp= arr[k-1]
               arr[k-1]= arr[-k]
               arr[-k]=temp




#######################################################Day8#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGhXV3R3LUpuSDUwTGdhT045TWhOSEhsS3NYd3xBQ3Jtc0tuRW5sS2I4WDNfYU1FZnI3SUNsMVh4NHZLaXJ2Tkp5WGN2UTVzNXZJNVJuUlNRcXRRTzZ5Ym1BSlRDWjU5am82eXF6Z0J1SU1xYkMwR25oTnRuSFdvLUUtM0hURnVYaG9RQmVQT01IQzVhbkx2SG5sVQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fjava-reverse-a-string0416%2F0&v=dG5kLPxZVPA
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        rev_string=''
        for i in range(len(s)-1,-1,-1):
            rev_string=rev_string+s[i]
        return rev_string

#[Assignemnts]:#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVFRWGlaeVdOR1VCZU1fcWowN2otSFh1cWNrQXxBQ3Jtc0tsMDhhT1dxZ0lIWDBfU0I4VW0xR2lXUWViSzlpNVRaalJycGZlODJ4NThBQ3hwaDNpQWJWNnpvRm9seG41dXVMRnl6MUNQeXBrLUgtZGpBc19Sa3VTajR4Uy1LaVFqNXh2VGdMa0lvQXBpRTdob0xMZw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freverse-a-string%2F0&v=dG5kLPxZVPA
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        rev_string=''
        for i in range(len(s)-1,-1,-1):
            rev_string=rev_string+s[i]
        return rev_string
#######################################################Day9#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGJGMmNCcDc5ZHdLNm0yUnZDY2pBZ25NTV85Z3xBQ3Jtc0tucGdYM0dzZkRha0M4M2gtR2JoWjJKTFRPSWhWNXluTWhfZHIxVWlyRkItYmJCOGg4cHQ2dS1EVnI1SVhQdjZZaF9hZUUtQ1o5YkU0UkY3N1dxM3F1R3o5UFduZkl3ZTd0REtMTkllSmxmaTFVSXJpSQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fperfect-arrays4645%2F0&v=EQzdB1MuEs4


#[Assignemnts]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkhGbWZJRDJrd1VyN01vamJtU2VCdExiNnh1Z3xBQ3Jtc0trOVZnaGtuUWpLRDdCTWowX2NIZTBydmRGRHNXVmRyODRJWFhJeU0xQzBydElMRGNscjhBbDdjeTdkdmdaWm4zWHUzeVBrOFBoelR2eVZlZnFrejVvTUJjZ3lhcEVzbmdFbWdTblloejZUSmRxUTJfSQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsearch-an-element-in-an-array-1587115621%2F0&v=EQzdB1MuEs4

########################################################Day10#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2J3eTBON0JpQ3Y3VXhYVjU3SUhfWHVpU1g1d3xBQ3Jtc0tsaFItVGV5SW5lem5IczFEUDlpbG8weWRIS2VGOUZqZXRra3ZXeDBxWWhvZTdWZ0EtbjdzVWN1NjZ1VUxwd256XzRKMG5uYnp6RF9JUlNuVjF1RlpESE50WDZsOEhtRWFNQVdFbXRqblV1MkFkRlhFcw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Frepeated-character2058%2F0&v=2_iSqg0rZ70
class Solution:
    def firstRep(self, s):
        # code here
        out={}
        for char in s:
            if char in out:
                out[char]+=1
            else:
                out[char]=1
        for key,val in out.items():
            if val>1:
                return key
            else:
                continue
        return "#"
#[Assignemnts]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVd0dUJPS0VQZkVVX3U2TlJjOEljWHdxaWJTQXxBQ3Jtc0tuWWlVSXhaaTNEakZnMF9kZERjTExRNFZVYTVHLW9WSzdLWkRCb2ZZdHlsVWZhVkZSbS1wbG9oZGEwdDBDTkdyVXpJcDhPRTF0cGFzNGhJbEs3X2lvakpWSm1PWnI4SzB6RFo0cFJKY09mOHlXSzhscw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fnon-repeating-character-1587115620%2F1%3Fpage%3D1%26category%3DStrings%26difficulty%3DEasy%26status%3Dsolved%26sortBy%3Dsubmissions&v=2_iSqg0rZ70
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        out={}
        for char in s:
            if char in out:
                out[char]+=1
            else:
                out[char]=1
        for key,val in out.items():
            if val==1:
                return key
            else:
                continue
        return "$"
########################################################Day11#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDR2UTJ3eEVETlBwbGp1d3hoUGRTOWM0MlpZd3xBQ3Jtc0trQTdSVFdEM1AyQVBkaHFqbUFyRTNrYnFVRlVoUHczVkQ5bldsVHp1UzR6QVVCYVpGNTA4R2RRZVA4TXBrMFRucXpfZ3g2S3Qzb0xCN2pjdGp6MTl0NDNIdnJ6TWQ5T1lDSnl4V2FKRGVQSHgtMkdVRQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fpeak-element%2F0&v=PMvvy2_SJJs
class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] >= arr[1]:
            return 0
        if arr[n - 1] >= arr[n - 2]:
            return n - 1
        
        for i in range(1, n - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
#[Assignemnts]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDBUREhzc2VvU0F4eWVVYmhKNXhneV9lcnloUXxBQ3Jtc0trNkVQczJfZGgzb1paY0pvZXcwcWpCTTBGVmpZNFJ0V2Y3eHBKcGp3cmVFeHJzVHc5aXV4RUx0eFEzamhSN1FfY3UyY21Rb0xFdmlQeXlDdzFlOFFhdXY1Y1JoSnJfelpQWERjR3lsbHFWLUZxTkd3RQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-minimum-and-maximum-element-in-an-array4428%2F0&v=PMvvy2_SJJs
class Solution:
    def get_min_max(self, arr):
        if not arr:
            return None, None  # or raise an exception
        
        max_val = arr[0]
        min_val = arr[0]
        
        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        
        return min_val, max_val

########################################################Day12#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbG42Y0Z2bnVOaGZWbV85RFNPdjg4djVzb0V2Z3xBQ3Jtc0trQU5pdUVBcGRoNEtiNi1iNHRPdU93cHNLVTR4NlJKeGpPMV9laU1XdmVPa0VoVi1qdUFqX1FkRWdNaGE3ZkxwdEx4ZnBNVTJHeXFNRXlSY05Oamp6QXk5eTlwSmVIbHY4eVE2ZkdKNVNJa3dOR3ljbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fupper-case-conversion5419%2F0&v=V7S79qTqIMY
class Solution:
    def convert(self, s):
        new_list=s.split()
        ans=[]
        for i in range(len(new_list)):
            word=new_list[i]
            char_up=word[0].upper()
            new_word=char_up+word[1:]
            ans.append(new_word)
        return ' '.join(ans)


#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHp0TjdpYnlFandmNzd5VzhrU1c1Uy1IQnJHd3xBQ3Jtc0tuYkExbDVpOXB4YTU4MWRPalR6aFV1VnpnQlpURG52UnFkcktObXgtbDVKXzBVNTVwckZSanl5SExmaE5Sc2lDN1lzS2Jrc2gxU2lBQTZTdVhoRUNjdWFtVjBJOGt1TUZUWEpCVTBxaWJyVmxCOWw3UQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fconvert-a-list-of-characters-into-a-string5142%2F0&v=V7S79qTqIMY
class Solution:
    def chartostr(self, arr,N):
        # code here
        new_string=""
        for char in arr:
            new_string+=char
        return new_string
########################################################Day13#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbldGWnRiRHBJSTBqSVY2VmhQeXl2d1NTbjM4UXxBQ3Jtc0tuWHJoa2RkeHJpY1FDNGZIRFB0d3E3RG9XQkNWdE00NVNncGhOenhDSGowejJPWTZzdnZIUWdQbWM1WWRleWhVamFHdEFIZ2xYQ0FXRmgxMzEtcklOVFJWN0xwMGNiRzNlMVVGZkpNZzlxVVh0RmlYOA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-odd-occurence4820%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DBasic%26status%3Dunsolved%26sortBy%3Dsubmissions&v=BfXQL-IElBs
class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        dict={}
        for num in arr:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]=dict[num]+1
        for key,val in dict.items():
            if val%2!=0:
                return key
            else:
                continue
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkszTWFpQ1ZtZWd3YW9JME9MdG9sbWpIRGY5UXxBQ3Jtc0ttWjRqRnd6RG9mUFNBRkt3VkdUeXd0a3o0WktCSEN1azJURndHTnVCT29HN253TjRITkJJN2tFTzdYc1JXSnU0d3BpTTN5ZkxaZEpfbFM4aFktcE5xa1c1SVBvMmlPZGxGQndGdVYzRll6aUp2MDlmRQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Farray-insert-at-end%2F0&v=BfXQL-IElBs
def insertAtEnd(arr,sizeOfArray,element):
    ##Your code here
    for i in range(len(arr)+1):
        if i==sizeOfArray-1:
            arr.append(element)
        else:
            continue
    return arr
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2hwODlKYnUxWWZub2NoSU1FZ0xPOVZYWFljZ3xBQ3Jtc0tsd3pvaVB6YkVFNU9OUjVpVzRuODBIQjQzT0dHMEU3U3VGanN5NjI4NzdULXMwc1hPVkR2ZlRWR2tLOWZtMFZPMDRQZHRtRDltb2l2LVhtQ1UyVnpLLUZMdmZKb3BiNUhwV3dDQzRQZEcyb2RFTWVqTQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsearch-an-element-in-an-array-1587115621--133819%2F0&v=BfXQL-IElBs
class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i in range(len(arr)):
            if x==arr[i]:
                return i
            else:
                continue
        return -1
    
########################################################Day14#####################################################################
#[Problem Statement]:

#[Assignments]:

            
########################################################Day15#####################################################################
#[Problem Statement]:
class Solution:
    def printNos(self, n):
        # Convert numbers to strings, then join them with spaces
        output_string = ' '.join(map(str, range(1, n + 1)))
        
        # Print the string without a trailing newline
        print(output_string, end='')
#[Assignments]:
class Solution:
    def getAlternates(self, arr):
        # Code Here
        alternate_array=[]
        for i in range(0,len(arr),2):
            alternate_array.append(arr[i])
        return alternate_array
########################################################Day16#####################################################################
#[Problem Statement]:

#[Assignments]:

########################################################Day17#####################################################################
#[Problem Statement]:
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        index_array=[]
        for i in range(1,len(arr)+1):
            if arr[i-1]==i:
                index_array.append(arr[i-1])
            else:
                continue
        return index_array
#[Assignments]:
class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        count=0
        for i in range(len(arr)):
            if arr[i]<=x:
                count+=1
            else:
                continue
        return count 
########################################################Day18#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblFFUWVpb2p0UkFSYjBSb05yVWppa243UUYyZ3xBQ3Jtc0tsOURCaWpubGVBSGdJandkX005cnRpM2VTNzVOcU9rRlNYNGwzejY2c1liNFJyMmk0ajMwbXBDcWN3TUVVMkdTWThmbGdVcF9kcVJraTg2OGdNRzVuQm5yWHBYZ041WXdKakQxbTd0ZFRBMlNiUzRRcw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fremove-vowels-from-string1446%2F0&v=Mqt4jxhj3UY
class Solution:
    def removeVowels(self, s):
        # code here
        new_string=''
        vowels='aeiou'
        for char in s:
            if char in vowels:
                continue
            else:
                new_string+=char
        return new_string
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbS1XSzFhaGQ0cDFzMHFtb1RRSlBWTTVuVWR2Z3xBQ3Jtc0treVFIek5pc0xXVkMxdWJWSEVNMUM4cUktdUNvOFZFSDRUNTUyQThHUHR6V2JaMXpGSTFiMzhLTUFlejc3c1JMLUJFd21rUENqZWRBX2U1LWFCckVuQm5FNFNPNm5wOG5zeWNFVHJDZzJHeWNBZlIwcw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fremove-spaces0128%2F0&v=Mqt4jxhj3UY
class Solution:
    def modify(self, s):
        # code here
        new_string=''
        space=' '
        for char in s:
            if char in space:
                continue
            else:
                new_string+=char
        return new_string
########################################################Day19#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbU4xQ05TbU1QUkFnaTlhRW51VUNJeEhwWk1HZ3xBQ3Jtc0trT1ltSFV4bTd5RnhiSkhXZGVIcjQ2ekVVZklUN1ZMQ3NmVnl5N21uTmlzYVhmWTdoNDlhRDFfeFdKTmpIS3Q0akZwVmpEajNQaFljOTZSVGhQUXlCd2lxa2Z6ZUFpVHMyWHRzU1J1RUloZXpfTHg2MA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsecond-largest3735%2F1%3Fpage%3D1%26category%3DArrays%26sortBy%3Dsubmissions&v=7azowOMpqGo
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        j = 1
        lar = arr[0]
        selar = -1
        while j < len(arr):
            if arr[j] > lar:
                lar = arr[j]
            j += 1
        for i in arr:
            if i < lar and i > selar:
                selar = i
        return selar
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDhpSnQ0eTdyTVlIYjZNbU8yWUpyVUE0OXFYZ3xBQ3Jtc0trWGxjdG1NQlkxMlFQVTFEaHFlOThnSk5mRFBjMWg0V1FrY2w3N3FvUklyTkxGUnVvYzVVWEJoUlk2OHdzU0ZfOXoxaHRlXzJPZE1XNkF6V0xIRUNnYmY3Q3ZndEhraW5UOWRxeHhkalNyQjNQRTZuSQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fneed-some-change%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DEasy%26status%3Dsolved%26sortBy%3Dsubmissions&v=7azowOMpqGo
class Solution:
    def swapElements(self, arr):
        #Code here
        for i in range(len(arr)-2):
            arr[i],arr[i+2]=arr[i+2],arr[i]
        return arr	            
########################################################Day20#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnZzTHdCSTZzbkwxY1BVdV82a3o3Y0tYQUN5d3xBQ3Jtc0tuZ1BZN2tjLS1pNXhBZDAwWVdua0xzUWZfOTBGNlVrSkE1UG5jRWc4akZyV3Q4UkpmNmhBX0xxMEdBbFg4ZVdXZjJDbzc2VWpOR00wOHg3SkctVS1zU3NkeU5Xc2RsWXlWbXZfZDB3NDdwdGRRdjlKMA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fbinary-string-1587115620%2F0&v=26psHO1uXPE
class Solution:
    def binarySubstring(self,n,s):
        #code here
        count=0
        for i in s:
            if i=='1':
                count=count+1
        return count*(count-1)/2
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEFMR2NBR2hIVE4yVVFzNkJVUmtHWUY4MDRRd3xBQ3Jtc0tsU19WbmlOOGt0VVc4OVlnT05nQXdzQ3hjRnhtcUZuSEthRm84cnNDTzNvV2MtZ2dyNFpiWml6YXV4eXBfS3QyLUV6ZlAwV2lVUWpNelExd0ZueURySThaTVRZUlJmTkk0dmthYVBmc2pyeWVrdlhwYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Flower-case-to-upper-case3410%2F0&v=26psHO1uXPE
class Solution:
    def to_upper(self, str):
        # code here
        return str.swap
        
        
########################################################Day21#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHFkLXltZ0k3VFdET1ZsMFlBSVlKUVVrTDEwd3xBQ3Jtc0tsd2dIRGxVOEdzWnNuMHdNRk5EWFdvd2p5dnhkcXVRY0hCNEh4T0NzNVR5REJJQnViNWpIV212RXI5SnlzSjM5RjducF94ZnEtbExSbE93RnZsdHNtRXp1ZVZyaWVreFNodUQ1Mlh6NDRVWW8tU0xhcw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fmissing-number-in-array1416%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DEasy%26status%3Dsolved%26sortBy%3Dsubmissions&v=IjG7Kz0fCkk
class Solution:
    def missingNum(self, arr):
        # code here
        sum=0
        for i in range(len(arr)):
            sum=sum+arr[i]
        n=len(arr)+1
        exact_sum=(n*(n+1))//2
        result=exact_sum-sum
        return result
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFdGQ2o3LWFMNDFHOVRoTVBnbnM3ZkVVeW01d3xBQ3Jtc0ttX3BIeXYweUV5MHI5Z2JYd1BjbHZuVXFfR1d2RmRQWGVjT083UXp6c3MwUjFJTVo0MVVmUHN4NzJCcDNYR3lKNGFVaUxZUTBva3QydmhRREJkSFBUS20tRTBMZGw3TDVrT0RPa0VOX2htREc0Z1hxbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fwho-will-win-1587115621%2F0&v=IjG7Kz0fCkk
class Solution:
    def searchInSorted(self,arr, k):
        #Your code here
        return True if k in arr else False
########################################################Day22#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2F1eXJGRmNmWFJnWGZabGxJQy02d0lQUkxUd3xBQ3Jtc0trZUdlakQzTUN4MF9rVTRRdEkzNXQ2WjNWekVCN3FRMFU3UjVhMkxURXZ2Y1FBVFFhVWtUeDVoWU5hSHZ4M3ZZTmg3dDNkdDZNMFFER2pJOE5BNFNYcEdKNUtFTm9RZERhdkN3R3FHN1c0OHdCUGRYZw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fpangram-checking-1587115620%2F1&v=__GdlFh9MNI
class Solution:

    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        arr=[0]*26
        s=s.lower()
        for char in s:
            if char.isalpha():
                arr[ord(char)-97]+=1
        for num in arr:
            if num==0:
                return False
            else:
                continue
        return True

#[Assignments 1]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjRHRjlHQWtxNFpsSUI3Y2J5bENfRkxBekdQd3xBQ3Jtc0ttRFJIUjhfZm5LNTM1dEl2OFpoUDNkYTIwQnhzMTRhRi1zV2NHUWZyc2d3OHJXNlRBUVZCSnR6SkRuMjA5TFVVQWxBeHVZMU0zV3c2eVlqX09xbF82dVJzZG9pTkdjR2FEM1FpZnM0LW5pYWpfZTdoYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Funcommon-characters4932%2F0&v=__GdlFh9MNI
class Solution:
      def getMaxOccurringChar(self, s):
        #code here
        dicts={}
        count=0
        for char in s:
            if char in dicts:
                dicts[char]+=1
            else:
                dicts[char]=1
        max_val = max(dicts.values())
        max_keys = [k for k, v in dicts.items() if v == max_val]
        return min(max_keys)
#[Assignments 2]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnBlMnpKc3g3NzgzeGFvanZoeHN6MHZONnlnUXxBQ3Jtc0tteGFQOVAzdEdmVXFKa3FGaWhKWTJRdExRclc3aWs3TlRicWczLTVPbFdFZ2FTWnhMQlRsZTRuallQQjRHeHlfalBDQnpOYWFkang0QW00aDBvMl9kSFBYaENQUGc4STVyWnVxZ0VWY29sQkw5Y1pLbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fmaximum-occuring-character-1587115620%2F1%3Fpage%3D1%26category%3DStrings%26difficulty%3DBasic%26status%3Dsolved%26sortBy%3Dsubmissions&v=__GdlFh9MNI

########################################################Day23#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFppYVFTWUpRaXQ1NVAtb1JQSU5wUWw3c3dSUXxBQ3Jtc0tteGR3UkFHX1RjbjBSeEVmUGFJbGFyUFR6Q2ZqMXZWNVBhaDFBRUtUa21fVnduZ2dkUmF2bEZUN00tZVV5dk9PMTc5S3hmQV9lWlo4eVlUX0hJUHdqbWlwdERrbVVuQlZ6TF9vcmw2Z0J0VjFnSHBzdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-pairs-with-given-sum5022%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DEasy%26sortBy%3Dsubmissions&v=UBHCvUh1_2A


#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2JqNEdOZ3pXcWZ3MG1zSklSdGRZN2FsWlBKQXxBQ3Jtc0ttM29sUHFDd2ZnY2RMQ0Yzdm5pMDd0dVhObnJlZ21Od1c3aDdPYzdrOG5JUjJTLTFNNTJnMS1kMmJIdHdNbUEyWVFHS05PMldoSTFNNGhtY0VZb2hXQUZBYmN3SF9pOHlIdVBRR2NLUC1sRHd4RjNkUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-duplicates-in-an-array%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DEasy%26status%3Dsolved%26sortBy%3Dsubmissions&v=UBHCvUh1_2A


########################################################Day24#####################################################################
#[Problem Statement]:

#[Assignments]:


########################################################Day25#####################################################################
#[Problem Statement]:


#[Assignments]:



########################################################Day26#####################################################################
#[Problem Statement]:


#[Assignments]:



########################################################Day27#####################################################################
#[Problem Statement]:


#[Assignments]:



########################################################Day28#####################################################################
#[Problem Statement]:


#[Assignments]:



########################################################Day29#####################################################################
#[Problem Statement]:

#[Assignments]:




########################################################Day30#####################################################################
#[Problem Statement]:


#[Assignments]:























