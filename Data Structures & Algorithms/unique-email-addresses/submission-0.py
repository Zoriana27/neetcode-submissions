class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            s = ""
            local, domain = email.split("@")
            for i, ch in enumerate(local):
                if ch != "+":
                    if ch != ".":
                        s += ch
                else:
                    break
            s += domain
            res.add(s)
        return len(res)
                    
        