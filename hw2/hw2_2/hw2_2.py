

class Person:
    def __init__(self):
        right_arm = Arm('Dominant is right hand.')
        left_arm = Arm('Non-dominant is left hand.')
        self.arms = [right_arm, left_arm]


class Arm:
    def __init__(self, handedness):
        self.handedness = handedness


print(f'#2.a:')
vinson = Person()
for arm in vinson.arms:
    print(arm.handedness)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, matrix_type):
        self.matrix_type = matrix_type


if __name__ == "main":
    print(f'#2.b:')
    lcd_screen = Screen('Liquid Crystal Display')
    cellPhone = CellPhone(lcd_screen)
    print(cellPhone.screen.matrix_type)
