marks = list(map(int, input("Enter marks separated by space: ").split()))

avg = sum(marks) / len(marks)  #here i get marks values 
highest = max(marks)
lowest = min(marks)

print("Average Marks:", avg)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)