def solution(s):
    o = s.lower()
    m = list(o) 
    m[0] = m[0].capitalize()
    for n in range(len(m)):
        if m[n] == " ": 
            if n + 1 < len(m): 
                m[n + 1] = m[n + 1].capitalize() 
    
    return ''.join(m)  
