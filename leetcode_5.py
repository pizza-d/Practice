### Substring with Concatenation of All Words

### solution 1
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        w_len = len(words[0])
        ws_len = len(words)
        p = w_len * ws_len
        times = 0
        res = []
        while times < s_len - p + 1:
            clon = words.copy()
            tmp = s[times:p+times]
            for i in range(ws_len):
                st = i * w_len
                t = tmp[st:st+w_len]
                if t in clon:
                    if i == ws_len - 1:
                        res.append(times)
                        times += 1
                    else:
                        clon.remove(t)
                else:
                    times += 1
                    break
        return res
      
### solution 2
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        w_len = len(words[0])
        ws_len = len(words)
        p = w_len * ws_len
        times = 0
        res = []
        w_dic = {}
        for i in words:
            try:
                w_dic[i] += 1
            except:
                w_dic[i] = 1
        while times < s_len - p + 1:
            chk = {}
            tmp = s[times:p+times]
            for i in range(ws_len):
                st = i * w_len
                t = tmp[st:st+w_len]
                chk[t] = chk[t]+1 if t in chk else 1
                if t in w_dic and chk[t] <= w_dic[t]:
                    if i == ws_len-1:
                        res.append(times)
                        times += 1
                else:
                    times += 1
                    break
        return res
