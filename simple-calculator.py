from tkinter import *
from tkinter import ttk

class Calculator(ttk.Frame):

    def createBtn(self, parent, txt, c, r, w, com):
        aBtn = ttk.Button(parent, text = txt, width = w, command = lambda: self.entryInp(com))
        aBtn.grid(column = c, row = r)
        return aBtn

    def entryInp(self, btnPressed):
        if btnPressed == 'inDot':
            self.dotPressed = True
        if btnPressed in ['in0', 'in1', 'in2', 'in3', 'in4', 'in5', 'in6', 'in7', 'in8', 'in9']:
            value = self.answer.get()
            if self.opJustPressed == True:
                value = '0'
                self.opJustPressed = False
            if self.dotPressed == True:
                if self.addedDot == False:
                    value += '.'
                    self.addedDot = True
                
            if value in ['0', 'Not a number']:
                self.answer.set(btnPressed[-1])
            else:
                self.answer.set(value + btnPressed[-1])

        elif btnPressed == 'ac':
            self.answer.set('0')
            self.addedDot = False
            self.dotPressed = False
        elif btnPressed == 'sqRoot':
            self.answer.set(str(float(self.answer.get()) ** 0.5))
        elif btnPressed == 'neg':
            self.answer.set(str(eval(self.answer.get()) * -1))
        elif btnPressed == 'frac':
            value = self.answer.get()
            if eval(value) == 0:
                self.answer.set('Not a number')
            else:
                self.answer.set(str(1 / float(self.answer.get())))
        elif btnPressed in ['in+', 'in-', 'in*', 'in/']:
            self.opJustPressed = True
            self.op.set(btnPressed[-1])
            self.number2 = self.answer.get()
            self.dotPressed = False
            self.addedDot = False
        elif btnPressed == 'in=':
            strValue = self.answer.get()
            if self.op.get() == '+':
                self.answer.set(str(eval(strValue) + eval(self.number2)))
            elif self.op.get() == '-':
                self.answer.set(str(eval(self.number2) - eval(strValue)))
            elif self.op.get() == '*':
                self.answer.set(str(eval(strValue) * eval(self.number2)))
            elif self.op.get() == '/':
                self.answer.set(str(eval(self.number2) / eval(strValue)))
            else:
                print(self.op.get())
        else:
            pass
            
    def __init__(self, frame):
        super(Calculator, self).__init__(frame)

        self.bFrame = ttk.Frame(frame)
        frame.grid(row = 0, column = 0)
        self.bFrame.grid(row = 1, column = 0, columnspan = 5)
        self.answer = StringVar(value = '0')
        self.number2 = ''
        self.firstNum = 0
        self.secondNum = 0
        self.op = StringVar('')
        self.opJustPressed = False
        self.dotPressed = False
        self.addedDot = False

        self.btn07 = self.createBtn(frame, '7', 0, 2, 6, 'in7')
        self.btn08 = self.createBtn(frame, '8', 1, 2, 6, 'in8')
        self.btn09 = self.createBtn(frame, '9', 2, 2, 6, 'in9')
        self.btn04 = self.createBtn(frame, '4', 0, 3, 6, 'in4')
        self.btn05 = self.createBtn(frame, '5', 1, 3, 6, 'in5')
        self.btn06 = self.createBtn(frame, '6', 2, 3, 6, 'in6')
        self.btn01 = self.createBtn(frame, '1', 0, 4, 6, 'in1')
        self.btn02 = self.createBtn(frame, '2', 1, 4, 6, 'in2')
        self.btn03 = self.createBtn(frame, '3', 2, 4, 6, 'in3')
        self.btn00 = self.createBtn(frame, '0', 0, 5, 6, 'in0')
        self.negate = self.createBtn(frame, '+/-', 1, 5, 6, 'neg')
        self.dot = self.createBtn(frame, '.', 2, 5, 6, 'inDot') 
        self.divide = self.createBtn(frame, '/', 3, 2, 6, 'in/')
        self.times = self.createBtn(frame, '*', 3, 3, 6, 'in*')
        self.minus = self.createBtn(frame, '-', 3, 4, 6, 'in-')
        self.add = self.createBtn(frame, '+', 3, 5, 6, 'in+')
        self.sqrt = self.createBtn(frame, 'sqrt', 4, 2, 6, 'sqRoot')
        self.percent = self.createBtn(frame, '%', 4, 3, 6, 'percentage')
        self.fraction = self.createBtn(frame, '1/x', 4, 4, 6, 'frac')
        self.equals = self.createBtn(frame, '=', 4, 5, 6, 'in=')

        self.backspace = self.createBtn(self.bFrame, 'Backspace', 0, 0, 13, 'bs')
        self.clear = self.createBtn(self.bFrame, 'C', 1, 0, 13, 'c')
        self.clearAll = self.createBtn(self.bFrame, 'AC', 2, 0, 13, 'ac')

        textentry = ttk.Entry(frame, textvariable = self.answer, width = 50, justify = 'right')
        textentry.grid(column = 0, row = 0, columnspan = 5)

def main():
    root = Tk()
    root.title('Calculator')
    frame = ttk.Frame(root)
    cal = Calculator(frame)
    cal.mainloop()

main()
