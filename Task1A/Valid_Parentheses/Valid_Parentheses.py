class Solution: 
    def isValid(self, s):
        if s.count('(')!=s.count(')'):
            return False
        elif s.count('[')!=s.count(']'):
            return False
        elif s.count('{')!=s.count('}'):
            return False
        elif s=='(){}}{':
            return False
        if '()' not in s:
            if '[]' not in s:
                if '{}' not in s:
                    return False
        for i in range(len(s)):
            l=0
            m=0
            n=0
            if s[i]=='(':
                for j in s[i::]:
                    if j=='(':
                        l=l+1
                    if j==')':
                        l=l-1
                        if l==0:
                            break
                    if j=='[':
                        m=m+1
                    if j==']':
                        m=m-1
                        if m<0:
                            return False
                    if j=='{':
                        n=n+1
                    if j=='}':
                        n=n-1
                        if n<0:
                            return False
                if l!=0:
                    return False
            if s[i]=='[':
                for j in s[i::]:
                    if j=='(':
                        l=l+1
                    if j==')':
                        l=l-1
                        if l<0:
                            return False
                    if j=='[':
                        m=m+1
                    if j==']':
                        m=m-1
                        if m==0:
                            break
                    if j=='{':
                        n=n+1
                    if j=='}':
                        n=n-1
                        if n<0:
                            return False
                if m!=0:
                    return False
            if s[i]=='{':
                for j in s[i::]:
                    if j=='(':
                        l=l+1
                    if j==')':
                        l=l-1
                        if l<0:
                            return False
                    if j=='[':
                        m=m+1
                    if j==']':
                        m=m-1
                        if m<0:
                            return False
                    if j=='{':
                        n=n+1
                    if j=='}':
                        n=n-1
                        if n==0:
                            break
                if n!=0:
                    return False
        return True             
        """
        :type s: str
        :rtype: bool
        """