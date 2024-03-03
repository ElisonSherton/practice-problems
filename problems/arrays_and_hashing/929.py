# https://leetcode.com/problems/unique-email-addresses/
from typing import List

class Solution:

    def get_components(self, mail):
        # Function to decompose the given mail into localname and domainname
        at_position = 0
        for element in mail:
            if element == "@":
                break
            else:
                at_position += 1
        local_name = mail[:at_position]
        domain_name = mail[(at_position + 1):]
        return local_name, domain_name

    def numUniqueEmails(self, emails: List[str]) -> int:
        # Maintain a set to accumulate the unique emails
        unique_emails = set()

        # Iterate over all emails
        for mail in emails:
            local_name, domain_name = mail.split("@")
            new_local_name = ""
            for element in local_name:
                # Ignore everything ahead of +
                if element == "+":
                    break
                # Skip the dots in local name
                elif element == ".":
                    continue
                else:
                    new_local_name += element
            unique_emails.add(f"{new_local_name}@{domain_name}")
        return len(unique_emails)