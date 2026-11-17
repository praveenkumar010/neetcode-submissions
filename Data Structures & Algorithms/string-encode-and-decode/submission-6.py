class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return str(strs)
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        return list(map(str,s.split(" ")))
