'''
Created on Sep 9, 2014
@author: tanmaymehrotra
'''

from sets import Set

#mydict = Set(["looked","just","like","her","brother"])
mydict = Set(["it", "hi"]) 

def unconcatenate(text, unmatched_chars):
    print text
    #break condition
    if len(text)==1 :
        if text not in mydict:
            return unmatched_chars + 1
        else:
            return unmatched_chars
         
    if len(text)==0:
        return unmatched_chars
    
    lstr_with_break = text[:1]
    lstr_without_break = text[:2]
    rstr_with_break = text[1:]
    rstr_without_break = text[2:]
    
    unmatched_chars_with_break = unmatched_chars
    unmatched_chars_without_break = unmatched_chars
    
    if lstr_with_break not in mydict:
        unmatched_chars_with_break += len(lstr_with_break)
    if lstr_without_break not in mydict:
        unmatched_chars_without_break += len(lstr_without_break)
    
    return min (unconcatenate(rstr_with_break, unmatched_chars_with_break),
                unconcatenate(rstr_without_break, unmatched_chars_without_break))
        
if __name__ == '__main__':
    #print unconcatenate("jesslookedjustlikeherbrother",0)
    print unconcatenate("thit", 0);