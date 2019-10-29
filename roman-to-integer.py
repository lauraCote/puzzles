class Solution:
    romanDict = dict({ "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 })
    
    def getTwoRomanLettersInt(self, index: int, lastIndex: int, s: str) -> int:
      if index < lastIndex:
        twoLetters = s[index:(index+2)]
        return self.romanDict.get(twoLetters, 0)
      return 0
    
    def romanToInt(self, s: str) -> int:
      lastIndex = len(s) - 1
      total = 0
      index = 0
      while index <= lastIndex:
        oneLetterInt = self.romanDict.get(s[index], 0)
        if oneLetterInt == 0:
          return 0
        twoLetterInt = self.getTwoRomanLettersInt(index, lastIndex, s)
        if twoLetterInt > 0:
          total += twoLetterInt
          index += 2
        else:
          total += oneLetterInt
          index += 1
      return total

print(Solution().romanToInt("MCMXCIV"))
          
        