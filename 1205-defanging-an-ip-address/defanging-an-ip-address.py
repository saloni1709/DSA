class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        if "." in address:
            address = address.replace(".", "[.]")
        return address