def course_grader(student_to_grades, course_prefix):
  accumScore = 0
  counter = 0

  avgScoreDict = {}

  for key in student_to_grades:
    for prefix in student_to_grades[key]:
      # if course prefix matches, store the scores for averaging in the later part
      if prefix == course_prefix:
        accumScore += student_to_grades[key][prefix]
        counter += 1 
    # if the student has the matching prefix, calculate average    
    if counter != 0:
      avgScoreDict[key] = accumScore / counter
      accumScore = 0
      counter = 0

  return avgScoreDict

print(course_grader({"1": {"MIS": 80, "MIS": 70}, "2": {"MIS": 60, "ISO": 80}, "3": {"ISO": 50}}, "MIS"))