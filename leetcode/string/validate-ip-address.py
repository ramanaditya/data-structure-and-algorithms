"""
## Questions : Medium

### 468. [Validate IP Address](https://leetcode.com/problems/validate-ip-address/)

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each
ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups
are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also,
we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case
 ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::)
to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example,
the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Example 1:
Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Constraints:
IP consists only of English letters, digits and the characters "." and ":".
"""

## Solutions


class Solution:
    def checkIPv4(self, IP: list) -> bool:
        if len(IP) != 4:
            return False
        for ip in IP:
            if not ip:
                return False
            for char in ip:
                if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    return False
            if int(ip) < 0 or int(ip) > 255:
                return False
            if len(ip) > 1 and ip[0] == "0":
                return False
        return True

    def checkIPv6(self, IP: list) -> bool:
        if len(IP) != 8:
            return False
        for ip in IP:
            ip = ip.lower()
            if not ip:
                return False
            if len(ip) > 4 or (len(ip) > 4 and ip[0] == "0"):
                return False
            for char in ip:
                if char not in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                ]:
                    return False
        return True

    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            ret = self.checkIPv4(IP.split("."))
            return "IPv4" if ret else "Neither"
        elif ":" in IP:
            ret = self.checkIPv6(IP.split(":"))
            return "IPv6" if ret else "Neither"
        return "Neither"


# Runtime: 32 ms, faster than 34.98% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 47.14% of Python3 online submissions


import re


class Solution:
    chunk_IPv4 = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    patten_IPv4 = re.compile(r"^(" + chunk_IPv4 + r"\.){3}" + chunk_IPv4 + r"$")

    chunk_IPv6 = r"([0-9a-fA-F]{1,4})"
    patten_IPv6 = re.compile(r"^(" + chunk_IPv6 + r"\:){7}" + chunk_IPv6 + r"$")

    def validIPAddress(self, IP: str) -> str:
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither"


# Runtime: 28 ms, faster than 68.39% of Python3 online submissions
# Memory Usage: 14 MB, less than 24.10% of Python3 online submissions
