class Solution:
    def encode(self, strs: List[str]) -> str:
        new_ting = ""
        for ting in strs:
            new_ting += ting + "!@%"
        return new_ting

    def decode(self, s: str) -> List[str]:
        return s.split("!@%")[:-1]