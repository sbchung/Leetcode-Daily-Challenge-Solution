# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:41:42 2025

@author: kaich
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def generate_dic(s):
            dic = dict()
            for i, x in enumerate(s):
                if x in dic:
                    dic[x].append(i)
                else:
                    dic[x] = [i]
            return dic
        
                
        def find_longest(s, sd, d):
            tmp = [""]
            
            for i, c in enumerate(s):
                if c in d:
                    idx = d[c][0]
                    j = 0
                    t = i
                    while s[t] == sd[idx+j]:
                        t += 1
                        j += 1
                        if t==len(s) or idx+j==len(sd):
                            break
                    tmp[-1]=(sd[idx:idx+j])
                tmp.append("")
            
            tmp.sort(key=len, reverse=True)
            
            if tmp[0] == "":
                return []
            
            i = 1
            while len(tmp[i])==len(tmp[0]):
                i += 1
            
            return tmp[:i]
        
        
        
        def recursive( s1, s2 ):
            
            if len(s1)==0 or len(s2)==0:
                return s1 + s2
            else:
                dic1 = generate_dic(s1)
                dic2 = generate_dic(s2)
                
                tmp1 = find_longest(s1, s2, dic2)
                tmp2 = find_longest(s2, s1, dic1)
                if len(tmp1)>0 and len(tmp2)>0:
                    if len(tmp1[0]) == len(tmp2[0]):
                        longest_common = tmp1 + tmp2
                    elif len(tmp1[0]) > len(tmp2[0]):    
                        longest_common = tmp1
                    else:
                        longest_common = tmp2
                elif len(tmp1)==0 and len(tmp2)>0:
                    longest_common = tmp2
                elif len(tmp1)>0 and len(tmp2)==0:
                    longest_common = tmp1
                else:
                    # len(tmp1)==0 and len(tmp2)==0:
                    return s1 + s2  
                        
                tmp_ans = []
                for lc in longest_common:
                    s1_idx1 = [s1.index(lc)]
                    
                    while 1:
                        try:
                            t = s1.index(lc, s1_idx1[-1]+1)
                            s1_idx1.append(t)
                        except:
                            break
                    
                    
                    s2_idx1 = [s2.index(lc)]
                    
                    while 1:
                        try:
                            t = s2.index(lc, s2_idx1[-1]+1)
                            s2_idx1.append(t)
                        except:
                            break
    
    
                    
                    for s1_i in s1_idx1:
                        for s2_i in s2_idx1:
                            s1_idx2 = s1_i + len(lc)
                            s2_idx2 = s2_i + len(lc)
                            t = recursive( s1[:s1_i], s2[:s2_i] ) + lc  + recursive( s1[s1_idx2:], s2[s2_idx2:])
                            tmp_ans.append(t)
                        # print(tmp_ans)
                    return min(tmp_ans, key=len)
            
        return recursive(str1, str2)
  

s = Solution()
str1 = "kqpabce"
str2 = "cabccc"

str1 = "baabaaabb"
str2 = "bbabbbaab"

# str1 = "abckkk"
# str2 = "pppabc"

# str1 = "aaabb"
# str2 = "bbaab"

# str1 = "jbbssrclgezcstobodispruxoyclmtsfxdtlxzhqapuecirrdqcbcacwirdgfgnzccemfjmfwdzgswnpnzdezngghgzsfnkbchsevxloxbfzeasykplikbkwtqszszfcelqckpxbaxtlnztrvyrnwrrjhmgnyvlgtydxpbwaztevtoqkwwibggligvwchlpxrmkyuxtefytksfxsutewxkqtzaivfompioyqlqnlsrngjcrrbhalrujgpmgnzohckehxafncuzsaekhhlsefytvcxefjgwyuhkyqwdoeyrddibsnfqmvzupqfqlxpeidyzmrjnoydaiyrilyyldsegjngiqyypxjnululevibasrxnrdssbdxskncppwlrjnybmdxqpentauxlrkvniyxxowjqsvjnjmbexwqymfochmsfeicioppkbpodwsgzdxofowkyhvhncvpeyiaglvhfgvbdzfumzjzoskbupqbrfyymtkiodzhatwlxhulpuyqjxpdyofagtfznsprrvahbgmbwftbtmgpsawszvpmhkddxixtrtzphxuxfkglhzbnwewxydybwylcxqjnulbcnzbkwigokpfexgjrreotysnedyceluzqrhxvgrywdkctksyvdvrsawrcrviznqfdinbjrescdukbcpvkfalsluglmtfviwrlzhvbrrlersezohpaovnvwvhyerpuwqjgutjntikraytvqtcnnyuzjpkbuwdhslynaccocshyabkmjlwyirekphtparktbrsouvjnkwhqhvqugrimovvyhhpptqiykrvqbvtdwgdikwtmfzbuccbmfgonbookvxbvpknkbnhvhjfdyzrkecrvmcyqwlcnhtrbateldrpvkiabfsfyjhzrccfwujeeabndkezmvhkr"
# str2 = "jbbsgezcstoboispruxoyclmtsfxgodtlxzhqapuecirrsdqcbcacwirdgqvxlofgnzccemfjmfwdzgasyxvytkuwnpnzdezngghgzsfnkbchseloxbykplonikbkyxxowtjqszszfcelqckpxbaxtlnztrvyrjnwrrjhmgnyvlgtydxpbwaztevtoqkwwibggligvxwqymfochlpxrmkyuxtefytksfxsutewxkqtzaicivfomppkbpioyqlqnldwsrngjcrrbhalrujgpmgnzohckehdxaofncuzsaeowkyhvhlsncvpefytiaglvcxehfjgwyuhkyqwdoeyrddivbsndzfqumvzjzoskbupqbrfqlxpeidyyzmrjntkioydzhaiyrilytwhyldsegjngiqyypxjnululevibasrxnrdssbpdxskyofagtfzncpspwlrrjnyvahbgmdxqpentauxlrkvniykvbwlxhulpuyqfsrtbtksyvdvrmgpsawrcrvisznqfvpmhkddxinbjxtrescdukbctzpvkfalslhxuglmtxfviwrkglzhvbrrlersezohpaovbnvwvhyegutjntikrawxytvtcnndyuzjpkbuwdhslynaclcoxqjnulbcshyanzbkmjlwyiregokphpafexgjrreotbrysonedyceluvjhzqrhxvqugrimovvyhhpptqiykrvqbvtdwgdikwtmfzbuccbmfgonbookvxbvpkntkbnhvhjfdyzrkecrvmcyqpuwlcnhqjgqtrbacteldrpvkiabfsfyjhzrccfwujeeabktndkezmvwhqfkrl"
print(s.shortestCommonSupersequence(str1, str2))