def pig_it(text):# problem derived from https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
    s = text.split(" ")"""Note that this solution is way below optimal space or time complexity; it is non pythonic and i'll have to revise it at some point. It is an easier implementataion to understand because of it's similarlity to other language's syntactical usage"""
    x = []
    b = ""
    specials = "[@_!#$%^&*()<>?/\|}{~:]" #list contaning all the special elements
    for i in range(len(s)):
        temp = ""
        if len(s[i]) ==1 and s[i] in specials: #since our code below on line 13 would not copy to temp if the range is just 1 
            x.append(s[i])
        elif len(s[i]) ==1 and s[i] not in specials:
            x.append(s[i])
            x.append("ay")
        for j in range((len(s[i]))-1):
                temp = s[i][0]
                x.append(s[i][j+1])
        x.append(temp)
        if temp not in specials:
            x.append("ay")
        if i < len(s)-1:
            x.append(" ")
        b = "".join(x)
    
    return b 


pig_it("Hello There")
