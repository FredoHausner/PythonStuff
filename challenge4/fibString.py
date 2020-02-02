class NumberToString:

    def numToString(self, n):
        numberString = str(n)

        if(len(numberString)) == 9:
            return self.hundredMillionsPlace(n)
        elif(len(numberString)) == 8:
            return self.tenMillionsPlace(n)
        elif(len(numberString)) == 7:
            return self.millionsPlace(n)
        elif (len(numberString)) == 6:
            return self.hundredThousandsPlace(n)
        elif (len(numberString)) == 5:
            return self.tenThousandsPlace(n)
        elif (len(numberString)) == 4:
            return self.thousandsPlace(n)
        elif (len(numberString)) == 3:
            return self.hundredsPlace(n, 'yes')
        elif (len(numberString)) == 2:
            return self.tensPlace(n)
        elif (len(numberString)) == 1:
            return self.onesPlace(n)


    def onesPlace(self, n):
        if(n == 0):
            return ''
        if(n == 1):
            return 'one'
        if(n == 2):
            return 'two'
        if(n == 3):
            return 'three'
        if(n == 4):
            return 'four'
        if(n == 5):
            return 'five'
        if(n == 6):
            return 'six'
        if(n == 7):
            return 'seven'
        if(n == 8):
            return 'eight'
        if(n == 9):
            return 'nine'

    def tensPlace(self, n):
        if(n == 10):
            return 'ten'

        elif(n > 10 and n < 20):
            if(n == 11):
                return 'eleven'
            if(n == 12):
                return 'twelve'
            if(n == 13):
                return 'thirteen'
            if(n == 14):
                return 'fourteen'
            if(n == 15):
                return 'fifteen'
            if(n == 16):
                return 'sixteen'
            if(n == 17):
                return 'seventeen'
            if(n == 18):
                return 'eighteen'
            if(n == 19):
                return 'nineteen'
        elif(n == 20):
            return 'twenty'
        elif(n > 20 and n < 30):
            if(n == 21):
                return 'twenty one'
            if(n == 22):
                return 'twenty two'
            if(n == 23):
                return 'twenty three'
            if(n == 24):
                return 'twenty four'
            if (n == 25):
                return 'twenty five'
            if (n == 26):
                return 'twenty six'
            if (n == 27):
                return 'twenty seven'
            if (n == 28):
                return 'twenty eight'
            if (n == 29):
                return 'twenty nine'
        elif(n == 30):
            return 'thirty'
        elif(n > 30 and n < 40):
            if(n == 31):
                return 'thirty one'
            if(n == 32):
                return 'thirty two'
            if(n == 33):
                return 'thirty three'
            if(n == 34):
                return 'thirty four'
            if (n == 35):
                return 'thirty five'
            if (n == 36):
                return 'thirty six'
            if (n == 37):
                return 'thirty seven'
            if (n == 38):
                return 'thirty eight'
            if (n == 39):
                return 'thirty nine'

        elif(n == 40):
            return 'fourty'

        elif(n > 40 and n < 50):
            if(n == 41):
                return 'fourty one'
            if(n == 42):
                return 'fourty two'
            if(n == 43):
                return 'fourty three'
            if(n == 44):
                return 'fourty four'
            if (n == 45):
                return 'fourty five'
            if (n == 46):
                return 'fourty six'
            if (n == 47):
                return 'fourty seven'
            if (n == 48):
                return 'fourty eight'
            if (n == 49):
                return 'fourty nine'

        elif(n == 50):
            return 'fifty'

        elif(n > 50 and n < 60):
            if(n == 51):
                return 'fifty one'
            if(n == 52):
                return 'fifty two'
            if(n == 53):
                return 'fifty three'
            if(n == 54):
                return 'fifty four'
            if (n == 55):
                return 'fifty five'
            if (n == 56):
                return 'fifty six'
            if (n == 57):
                return 'fifty seven'
            if (n == 58):
                return 'fifty eight'
            if (n == 59):
                return 'fifty nine'

        elif(n == 60):
            return 'sixty'

        elif(n > 60 and n < 70):
            if (n == 61):
                return 'sixty one'
            if (n == 62):
                return 'sixty two'
            if (n == 63):
                return 'sixty three'
            if (n == 64):
                return 'sixty four'
            if (n == 65):
                return 'sixty five'
            if (n == 66):
                return 'sixty six'
            if (n == 67):
                return 'sixty seven'
            if (n == 68):
                return 'sixty eight'
            if (n == 69):
                return 'sixty nine'

        elif(n == 70):
            return 'seventy'

        elif (n > 70 and n < 80):
            if (n == 71):
                return 'seventy one'
            if (n == 72):
                return 'seventy two'
            if (n == 73):
                return 'seventy three'
            if (n == 74):
                return 'seventy four'
            if (n == 75):
                return 'seventy five'
            if (n == 76):
                return 'seventy six'
            if (n == 77):
                return 'seventy seven'
            if (n == 78):
                return 'seventy eight'
            if (n == 79):
                return 'seventy nine'

        elif(n == 80):
            return 'eighty'

        elif(n > 80 and n < 90):
            if (n == 81):
                return 'eighty one'
            if (n == 82):
                return 'eighty two'
            if (n == 83):
                return 'eighty three'
            if (n == 84):
                return 'eighty four'
            if (n == 85):
                return 'eighty five'
            if (n == 86):
                return 'eighty six'
            if (n == 87):
                return 'eighty seven'
            if (n == 88):
                return 'eighty eight'
            if (n == 89):
                return 'eighty nine'

        elif(n == 90):
            return 'ninety'

        elif(n > 90 and n < 100):
            if (n == 91):
                return 'ninety one'
            if (n == 92):
                return 'ninety two'
            if (n == 93):
                return 'ninety three'
            if (n == 94):
                return 'ninety four'
            if (n == 95):
                return 'ninety five'
            if (n == 96):
                return 'ninety six'
            if (n == 97):
                return 'ninety seven'
            if (n == 98):
                return 'ninety eight'
            if (n == 99):
                return 'ninety nine'


    def hundredsPlace(self, n, bool):

        if(len(str(n)) == 2):
            twentys = self.tensPlace(int(str(n)))
            return 'and ' + twentys
        else:
            hundreds = self.onesPlace(int(str(n)[0:1]))
            if(str(n)[1:2] == '0'):
                ones = self.onesPlace(int(str(n)[2:3]))
                if (bool == 'yes'):
                    return hundreds + ' hundred and ' + ones
                else:
                    return hundreds + ' hundred ' + ones
            else:
                twentys = self.tensPlace(int(str(n)[1:3]))
                if(bool == 'yes'):
                    return hundreds + ' hundred and ' + twentys
                else:
                    return hundreds + ' hundred ' + twentys


    def thousandsPlace(self, n):
        thousands = self.onesPlace(int(str(n)[0:1]))
        return thousands + ' thousand ' + self.hundredsPlace(int(str(n)[1:4]), 'yes')

    def tenThousandsPlace(self, n):
        tenThousands = self.tensPlace(int(str(n)[0:2]))
        return tenThousands + ' thousand ' + self.hundredsPlace(int(str(n)[2:5]), 'yes')

    def hundredThousandsPlace(self, n):
        hundredThousands = self.hundredsPlace(int(str(n)[0:3]), 'no')
        return hundredThousands + ' thousand ' + self.hundredsPlace(int(str(n)[3:6]), 'yes')

    def millionsPlace(self, n):
        millions = self.onesPlace(int(str(n)[0:1]))
        return millions + ' million ' + self.hundredThousandsPlace(int(str(n)[1:7]))

    def tenMillionsPlace(self, n):
        tenMillions = self.tensPlace(int(str(n)[0:2]))
        return tenMillions + ' million ' + self.hundredThousandsPlace(int(str(n)[2:8]))

    def hundredMillionsPlace(self, n):
        hundredMillion = self.hundredsPlace(int(str(n)[0:3]), 'no')
        return hundredMillion + ' million ' + self.hundredThousandsPlace(int(str(n)[3:9]))