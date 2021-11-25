def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    positives = 0
    negatives = 0
    # Dictionary for Allocating each roman numeral
    dict={"I":1,"V":5, "X": 10, "L" : 50,"C" : 100, "D" : 500,"M" : 1000}
    #processing if there is only one element
    if len(roman) ==1:
        return dict[roman[0]]
    #loops till the end of the string
    #Note that this converter does NOT detect if the certain numeral is not valid, 
    for i in range(len(roman)-1):
        if dict[roman[i]] < dict[roman[i+1]] :#Comparing one element to the other and if it detects a negative it adds it to negatives
            negatives = negatives + dict[roman[i]]
        elif dict[roman[i]] >=dict[roman[i+1]]:  
            positives = positives + dict[roman[i]]
    positives = positives + dict[roman[len(roman)-1]]        
            
    return positives - negatives
print(solution("XV"))
print(solution("XIV"))