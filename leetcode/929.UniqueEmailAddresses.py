class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            local = local.split('+')[0]
            new_email = '{local_name}@{domain_name}'.format(local_name=local, domain_name=domain)
            email_set.add(new_email)
        return len(email_set)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    a = Solution()
    print(a.numUniqueEmails(emails))
