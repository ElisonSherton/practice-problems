# https://leetcode.com/problems/simplify-path/

# Simpler solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        helper_stack = []
        path += "/"
        L, n = 0, len(path)
        cur = ""

        while L < n:
            this_element = path[L]

            if this_element == "/":
                if cur == "..":
                    if helper_stack: helper_stack.pop()
                elif cur != "." and cur:
                    helper_stack.append(cur)
                cur = ""
            else:
                cur += this_element
            
            L += 1
        
        return "/" + "/".join(helper_stack)

# Working solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        L, n = 1, len(path)
        
        components = []
        part = ""
        # Parse once to get all the parts
        while L < n:
            this_element = path[L]
            
            # Get rid of all the forward slashes
            if this_element == "/":
                while L < n and this_element == "/":
                    L += 1
                    this_element = path[L] if L < n else ""
                L -= 1
                if part: components.append(part)
                part = ""
            else:
                part += this_element
            
            L += 1

        # If the final part is non empty and you did not encounter a slash, add that to our parts 
        if len(part):
            components.append(part)

        # Use a stack to resolve the components (i.e. if there are any dots or double dots)
        final_path = []
        for element in components:
            if element == "..":
                if len(final_path): final_path.pop()
            elif element == ".":
                pass
            else:
                final_path.append(element)
        
        # Form the final path using the list above
        result = "/"
        for idx, element in enumerate(final_path):
            appender = "/" if idx != len(final_path) - 1 else ""
            result += element + appender
        
        return result            