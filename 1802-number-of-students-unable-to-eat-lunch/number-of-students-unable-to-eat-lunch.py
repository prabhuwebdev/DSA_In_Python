import collections
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student=collections.deque(students)
        sandwich=collections.deque(sandwiches)
        rotations=0
        while student and rotations < len(student):
            if student[0] == sandwich[0]:
                student.popleft()
                sandwich.popleft()
                rotations=0
            else:
                student.append(student.popleft())
                rotations+=1
                
        return len(student)
        
        

            
        