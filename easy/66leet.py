# def plusOne(self, digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     digits = "".join([str(x) for x in digits])
#     digits = int(digits)
#     digits+=1
    
#     ans = []
#     for k in str(digits):
#         ans.append(int(k))
#     return ans



def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    flag = 0
    if len(digits)==1:
        if digits[-1] + 1>9:
            digits = [1,0]
        else:
            digits[-1]+=1
        print(digits)

    for i in range(len(digits)-1,-1,-1):
        if digits[i] + 1 > 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,0)
                i = 1
            digits[i-1]+= 1
            flag = 1
        else:
            if not flag:
                digits[i]+=1
            break
    print(digits)

plusOne([9])



