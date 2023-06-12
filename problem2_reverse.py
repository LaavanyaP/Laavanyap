#Ques 1: Write a Fibonnaci sequence
print("Fibonacci sequence")
i, j = 0, 1
x = 1
while x <= 10:
    print(i)
    sum = i + j
    i = j
    j = sum
    x += 1

#Ques 2: Send the words to mirror dimension

text = "Edyoda Classroom"
new_text = text[::-1]
print("Mirror dimension of text is:", new_text)

# #Ques3: Count the num of even and odd form a series
   
even_count = 0
odd_count = 0
for i in range(0,13):
    if i%2 == 0:
        even_count +=1
    else:
        odd_count +=1
print("number of even is", even_count)
print("number of odd is", odd_count)

