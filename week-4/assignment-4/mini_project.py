#Using loops and data structure operations, your script must:
#Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
#Calculate the class average — accumulate the total score in a loop, then divide.
#List all unique subjects — use a set to collect subjects as you loop, then print them.
#List high scorers — use a loop and .append() to get the names of all students who scored above 75.

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_scorer_index=0
class_score=0
subject_set=set()
high_score_list=[]
bottom_line_score=75

for i, student in enumerate(students):
  if students [i]["score"] >= students [top_scorer_index]["score"]:
    top_scorer_index=i
  class_score += student ["score"]
  subject_set.add (student["subject"])
  
  if student["score"] > bottom_line_score:
    high_score_list.append(student["name"])


print (f"Top scorer: {students[top_scorer_index]["name"]} ({students[top_scorer_index]["score"]})")

average_class_score =  class_score/len(students)
print (f"Class average: {average_class_score:.2f}")

print (subject_set)
print (high_score_list)