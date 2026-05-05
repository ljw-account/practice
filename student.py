class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def avg_score(self):
        total = 0
        for score in self.scores:
            total += score
        return total/len(self.scores)
    
    def is_passed(self):
        if self.avg_score() >= 60:
            return True
        else:
            return False
    
    def summary(self):
        return (f"姓名 : {self.name}\n平均分數 : {self.avg_score()}\n是否及格 : {self.is_passed()}")
    
student1 = Student("Sam", [20, 30, 50])
student2 = Student("Emily", [50, 70, 85])

student1_summary = student1.summary()
student2_summary = student2.summary()

print(student1_summary)
print(student2_summary)

class GraduateStudent(Student):
    def __init__(self, name, scores, thesis):
        super().__init__(name, scores)
        self.thesis = thesis
    
    def summary(self):
        return (f"姓名 : {self.name}\n平均分數 : {self.avg_score()}\n是否及格 : {self.is_passed()}\n論文題目 : {self.thesis}")

student3 = GraduateStudent("Sam", [20, 30, 50], "船運")
print(student3.summary())