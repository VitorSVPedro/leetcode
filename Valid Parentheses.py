import queue
class Solution:
    def isValid(self, s: str) -> bool:
        stk = queue.LifoQueue()
        i = 0
        if len(s) % 2 != 0:
            return False
            
        else:
            for c in s:
                if c == "(" or c == "[" or c == "{":
                    stk.put(c)
                else:
                    if stk.empty():
                        return False
                    elif c == ")" and stk.get() == "(":
                        continue
                    
                    elif c == "]" and stk.get() == "[":
                        continue
                    
                    elif c == "}" and stk.get() == "{":
                        continue
                    else:
                        return False
    
            if stk.empty():
                return True