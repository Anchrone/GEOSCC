import matplotlib.pyplot as plt 


#score plotting utility v0.1

msgOne = input("Welcome to score plotting utility!")



peopleLimit = int(input("How many people do you have in class? Please input digits: "))
names  =   []
scores =   []

#experimental functionality -begin


#experimental functionality -end
for a in range(0,peopleLimit):
    fName = str(input("Name of the student: "))
    names.append(fName)
    studentScore = int(input("Score of this student: "))
    scores.append(studentScore)

            
    
# experimental functionality

#script for listing names and scores


plt.scatter(names,scores)
plt.plot(names,scores)
plt.xlim(-1,peopleLimit)
plt.ylim(0,100)

plt.xlabel("student names")
plt.ylabel("%")
plt.title("Student score plotting utility")
plt.legend()
plt.show()
