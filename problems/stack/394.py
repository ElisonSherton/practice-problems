# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:

        # Create a set of lowercase characters to later help to check if the element to be added is a digit or not
        lower = set("abcdefghijklmnopqrstuvwxyz")
        decoded_stack = []

        for element in s:
            # If element is a digit, then do this
            if (element != "[") and (element not in lower) and (element != "]"):
                

                # Check if it is a multiple digit number by checking previously stacked numbers
                num = element
                if decoded_stack:
                    while decoded_stack and not isinstance(decoded_stack[-1], str):
                        num = str(decoded_stack.pop()) + num

                decoded_stack.append(int(num))

            # If element is a open bracket or an alphabet, just push it on the stack
            elif (element == "[") or (element in lower):
                decoded_stack.append(element)

            # If element is a closed bracket, then pop the elements from the stack and form the string until an integer element is encountered while popping back
            else:
                decoded_chars = ""
                while decoded_stack:
                    top = decoded_stack.pop()
                    # Stopping condition
                    if isinstance(top, int):
                        dc = decoded_chars
                        for i in range(top - 1):
                            decoded_chars = decoded_chars + dc
                        decoded_stack.append(decoded_chars)
                        break
                    else:
                        if top != "[":
                            decoded_chars = top + decoded_chars

        # Now our result is simply getting the elements of the stack back in reverse chronological order 
        result = ""
        for element in decoded_stack:
            result = result + element
        
        return result