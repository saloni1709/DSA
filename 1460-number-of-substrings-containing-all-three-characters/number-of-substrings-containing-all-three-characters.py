class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = 0
        l = 0
        for r in range(len(s)):
             # =========================
            # r = 0
            # l = 0
            # sub = s[0:1] = "a"
            # "a" mein a,b,c teeno nahi hain
            # → while nahi chalega
            #
            # =========================
            #
            # r = 1
            # l = 0
            # sub = s[0:2] = "ab"
            # "ab" mein c nahi hai
            # → while nahi chalega
            #
            # =========================
            #
            # r = 2
            # l = 0
            # sub = s[0:3] = "abc"
            # a,b,c teeno hain ✅
            #
            # while chalega:
            #
            # count += len(s) - r
            # count = 0 + (6 - 2)
            # count = 4
            #
            # Ye 4 substrings hain:
            # "abc"
            # "abca"
            # "abcab"
            # "abcabc"
            #
            # ab l += 1
            # l = 1
            #
            # new sub:
            # s[1:3] = "bc"
            #
            # "bc" mein a nahi hai ❌
            # while stop
            #
            # =========================
            #
            # r = 3
            # l = 1
            # sub = s[1:4] = "bca"
            # a,b,c teeno hain ✅
            #
            # count += 6 - 3
            # count = 4 + 3
            # count = 7
            #
            # Ye 3 substrings:
            # "bca"
            # "bcab"
            # "bcabc"
            #
            # l += 1
            # l = 2
            #
            # new sub:
            # s[2:4] = "ca"
            # b nahi hai ❌
            #
            # =========================
            #
            # r = 4
            # l = 2
            # sub = s[2:5] = "cab"
            # a,b,c teeno hain ✅
            #
            # count += 6 - 4
            # count = 7 + 2
            # count = 9
            #
            # Ye 2:
            # "cab"
            # "cabc"
            #
            # l += 1
            # l = 3
            #
            # new sub:
            # s[3:5] = "ab"
            # c nahi hai ❌
            #
            # =========================
            #
            # r = 5
            # l = 3
            # sub = s[3:6] = "abc"
            # a,b,c teeno hain ✅
            #
            # count += 6 - 5
            # count = 9 + 1
            # count = 10
            #
            # Ye 1:
            # "abc"
            #
            # l += 1
            # l = 4
            #
            # new sub:
            # s[4:6] = "bc"
            # a nahi hai ❌
            # while stop
            sub = s[l:r+1]
            while 'a' in sub and 'b' in sub and 'c' in sub:
                count += len(s) - r
                l += 1
                sub = s[l:r+1]
        return count