#
#
# class SwitchWeek:
#     def __init__(self):
#         self.rear = 0
#         self.front = 0
#         self.minor = 0
#         self.misc = 0
#         self.under = 0
#
#         self.switcher = {
#             "REAR END": self.rearEnd,
#             "FRONT END": self.frontEnd,
#             "MINOR": self.minor,
#             "UNDER": self.under
#         }
#
#
#     def rearEnd(self):
#         return 'rear end'
#         rear += 1
#     def frontEnd(self):
#         return 'front end'
#         front += 1
#     def minor(self):
#         return 'minor'
#         minor += 1
#     def under(self):
#         return 'under'
#         under += 1
#     def default(self):
#         return 'this is run if others dont work'
#
#
#     def switch(self, damage):
#         return self.switcher.get(damage, self.default)()

# newSwitch =  SwitchWeek()
# otherSwitch = SwitchWeek()
#
# print(newSwitch.switch('nothing'))
# print(newSwitch.switch('REAR END'))
# print(newSwitch.switch('FRONT END'))







class SwitchWeek:
    rear = 0
    front = 0
    minor = 0
    misc = 0


    def rearEnd(self):
        return 'rear end'
        rear += 1
    def frontEnd(self):
        return 'front end'
        front += 1
    def minor(self):
        return 'minor'
        minor += 1
    def under(self):
        return 'under'
        under += 1
    def default(self):
        return 'this is run if others dont work'


    def switch(self, damage):
        # return self.switcher.get(damage, self.default)()
        return self.switcher.get(self.damage, self.default)()


    switcher = {
        "REAR END": rearEnd
    }

other = SwitchWeek()
other.switch('REAR END')