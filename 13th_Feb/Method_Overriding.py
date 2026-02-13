# METHOD OVERRIDING
# SAME METHOD NAME, SAME PARAMETER, DIFFERENT PARAMETERS

# class Exam:
#     def marks(self):
#         print("Total Marks: 100")

# class Math(Exam):
#     def marks(self):
#         print("Total Marks: 200")

# m = Math()
# m.marks()

class Exam:
    def total_marks(self):
        print("Total Marks : 100")
class Math(Exam):
    def total_marks(self):
        super().total_marks()
        print("Total Marks : 200")
m = Math()
m.total_marks()