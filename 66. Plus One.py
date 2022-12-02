def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # faster method
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
                return digits           
        else:
            digits[i] += 1
            return digits
    # a = "".join(str(i) for i in digits)
    # a = str((int(a)+1))
    # return [int(i) for i in a]

print(plusOne([9,9]))
print(plusOne([1,9,0]))