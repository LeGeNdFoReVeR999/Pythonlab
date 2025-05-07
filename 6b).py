class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self.normalize()

    def normalize(self):
        if self.seconds>=60:
            self.minutes+=self.seconds//60
            self.seconds%=60
        if self.minutes>=60:
            self.hours+=self.minutes//60
            self.minutes%=60
            self.hours%=24

    def __str__ (self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def __add__(self,other):
        new_time=Time(self.hours+other.hours,self.minutes+other.minutes,self.seconds+other.seconds)
        new_time.normalize()
        return new_time
    def get__time__input():
        hours=int(input("Enter hours"))
        minutes=int(input("Enter minutes"))
        seconds=int(input("Enter seconds"))
        return Time(hours,minutes,seconds)

print("\nEnter the first time:")
t1=Time.get__time__input()
print("Time t1:",t1)

print("\nEnter the second time:")
t2=Time.get__time__input()
print("Time t2:",t2)

t3=t1+t2
print("\nAdding the two times")
print("sum of time:",t3)


