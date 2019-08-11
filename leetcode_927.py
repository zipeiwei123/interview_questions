class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #return the email index with assign of "+" and "@"
        unique_email = set()
        for email in emails:
            local, domain = email.split("@")
            #ignore all the local name after local
            if "+" in local:
                local = local[:local.index("+")]
            unique_email.add(local.replace('.', '') + "@" + domain)
        return len(unique_email)
        