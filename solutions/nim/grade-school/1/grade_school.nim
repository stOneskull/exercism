import std/algorithm


type
  Student* = object
    name*: string
    grade*: int

  School* = object
    students*: seq[Student]


proc roster*(school: School): seq[string] =
  ## Returns the names of every student in the `school`, sorted by grade then name.
  var sortedStudents = school.students

  sortedStudents.sort(proc(a, b: Student): int =
    if a.grade < b.grade:
      return -1
    if a.grade > b.grade:
      return 1
    # Grades are equal, so sort by name
    return cmp(a.name, b.name)
  )

  for student in sortedStudents:
    result.add(student.name)


proc addStudent*(school: var School, name: string, grade: int) =
  ## Adds a student with `name` and `grade` to the `school`.
  ##
  ## Raises a `ValueError` if `school` already contains a student named `name`.
  for student in school.students:
    if student.name == name:
      raise newException(ValueError, "Student name already exists")

  school.students.add(Student(name: name, grade: grade))


proc grade*(school: School, grade: int): seq[string] =
  ## Returns the names of the students in the given `school` and `grade`, in
  ## alphabetical order.
  for student in school.students:
    if student.grade == grade:
      result.add(student.name)

  result.sort()
