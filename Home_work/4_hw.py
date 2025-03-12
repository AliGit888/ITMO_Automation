class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2*(self.width + self.height)

k=Rectangle(7,3)
l= Rectangle(3,5)
m = Rectangle(2,2)

print(k.area())
print(k.perimetr())
print('\n')
print(l.area())
print(l.perimetr())
print('\n')
print(m.area())
print(m.perimetr())

print('\n')

class Math:
     def __init__(self,a,b):
         self.a = a
         self.b = b
     def addition(self):
         return self.a + self.b
     def multiplication(self):
         return self.a * self.b
     def divison(self):
         return self.a / self.b
     def substraction(self):
         return self.a - self.b

t = Math(5,8)

print(t.addition())
print(t.multiplication())
print(t.divison())
print(t.substraction())

print('\n')

class Button:
    type: str = 'Кнопка'
    def __init__(self,text,loc):
        self.text = text
        self.loc = loc
    def click (self):
        print (f'Клик по кнопке {self.text}')

TextBox = Button('Text Box','')
CheckBox = Button ('Check Box','')
RadioButton = Button ('Radio Button', '')
WebTables = Button ('Web Tables', '')
Buttons = Button ('Buttons', '')
Links = Button ('Links', '')
UploadAndDownload = Button ('Upload And Download', '')
DynamicProperties = Button ('Dynamic Properties', '')

print(TextBox.text, TextBox.type, TextBox.loc)
print(CheckBox.text, CheckBox.type, CheckBox.loc)
print(RadioButton.text, RadioButton.type,RadioButton.loc)
print(WebTables.text, WebTables.type, WebTables.loc)
print(Buttons.text, Buttons.type, Buttons.loc)
print(Links.text, Links.type, Links.loc)
print(UploadAndDownload.text, UploadAndDownload.type, UploadAndDownload.loc)
print(DynamicProperties.text, DynamicProperties.type, DynamicProperties.loc)

print('\n')

TextBox.click()
CheckBox.click()
RadioButton.click()
WebTables.click()
Buttons.click()
Links.click()
UploadAndDownload.click()
DynamicProperties.click()


