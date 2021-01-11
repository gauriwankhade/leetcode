class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        Dict = {}
        for i in emails:
            string = i.split('@')
            local = string[0]
            domain = '@'+string[-1]

            if '.' in local:
                local = local.replace('.','')
            if '+' in local:
                local = local.split('+')[0]

            email = local+domain
            Dict[email] = True

        return len(Dict)


