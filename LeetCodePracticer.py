
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = s
        if len(s)%2 !=0:
            return False
        else:
            length = len(str1)
            i = 0
            while i <= length - 1:
                if str1 == '':
                    break
                elif self.matcher(str1[i]) == str1[i + 1]:
                    str1 =str1[:i]+ str1[i+2:]
                    length = len(str1)
                    continue
                elif self.matcher(str1[i]) == str1[length - 1]:
                    str1= str1[:length-1] + str1[length:]
                    str1 = str1[:i] + str1[i + 1:]
                    length = len(str1)
                    continue
                else:
                    return False
        return True

    def matcher(self, char):
        if char == '(':
            return ')'
        elif char== '[':
            return ']'
        elif char == '{':
            return '}'

if __name__ == "__main__":
    s = Solution()
    strs = "(([]){})"
    print(s.isValid(strs))

'''God Tier Code For This:
def isValid(self, s):
       """            
       :type s: str
       :rtype: bool
       """
       stack = []

       for c in s:
           if c == '(':
               stack.append(')')
           elif c == '{':
               stack.append('}')
           elif c == '[':
               stack.append(']')
           elif len(stack) == 0 or stack.pop() != c:
               return False
       return True if len(stack) == 0 else False
'''