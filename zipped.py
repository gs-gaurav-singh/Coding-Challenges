def average(n,x):
    
    students = []
    
    for i in range(x):
        # name = f"stu{i}"
        marks = list(map(float, input().split()))
        students.append(marks)
        
    map_students = list(zip(*students))
    for subject_marks in map_students:
        print(sum(subject_marks) / x)

if __name__ == "__main__":
    
    n, x = map(int, input().split())
    
average(n,x)
