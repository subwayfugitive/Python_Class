#Project 1 #11 Male and female percentages
#Thomas Powell Horan 2/24/22

#First a description of the program then we requre input

print("This program will calculate the percentages of males and females in a classroom")
males = float(input('Please eneter the number of males in the class '))
females = float(input('Please enter the number of females in the class'))

#here we are going to calcuclate the percentages by dividing the number of males/females by the total number of students in the class
class_size = males + females
print(f'{(males/class_size)* 100}% of this class is male')
print(f'{(females/class_size)*100}% of this class is female')

#I multiplied the answers by 100 to make them look better
