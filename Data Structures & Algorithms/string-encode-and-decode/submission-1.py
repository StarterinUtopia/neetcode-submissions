class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=f"{len(s)}#{s}"    
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        resList=[]
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            start=j+1
            end=start+length      
            resList.append(s[start:end])
            i=end
        return resList
