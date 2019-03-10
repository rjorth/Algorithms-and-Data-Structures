def isPalindrome(self, x: int) -> bool:
        if (x < 0): #negative cant be palindrome 
            return False
        s = str(x) #make x iterable by making it a string
        front = 0
        back = len(s) -1 #0 indexing, so if you do not subtract 1, then out of index
        
        if back == 0: #otherwise will loop endlessly in some case
            return True
        
        #create a loop to check that the front equals the back of the string
        #if they are not equal, then x is not a palindrome
        while s[front] == s[back] and front <= back:
            front += 1
            back -= 1 
            
        if front < back : 
            return False 
        
        return True