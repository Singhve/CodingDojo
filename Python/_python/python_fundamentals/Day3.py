def isPalindrome(arr):
    left = 0
    right = len(arr) - 1
    while left < right and arr[left] == arr[right]:
        left += 1
        right -= 1
    return left >= right
print(isPalindrome('potato'))
print(isPalindrome('racecar'))

def isPalindrome(stringInput):
    reversed = ""
    for i in range(len(stringInput) - 1, -1, -1):
        reversed += stringInput[i]
    return reversed == stringInput
print(isPalindrome('potato'))
print(isPalindrome('racecar'))

def isPal2(stringInput):
    for i in range(0, len(stringInput)//2, 1):
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True

print(isPal2("aabcbaa"))
print(isPal2('potato'))
print(isPal2('racecar'))