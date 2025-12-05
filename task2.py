import math
#comparing two floating point numbers
print(math.isclose(0.1, 1))

print(math.ceil(2.3))

file_name = "file.yaml"

print(file_name.endswith(".yaml"))
print(file_name.startswith("file"))

path = "var/lib/bin"

splited_path = path.split("/")

print(f"splited path: {splited_path}")

print(f"joined path: {'/'.join(splited_path)}")

course = "  python_programming  "
print(course.rstrip())
print(course.lstrip())
print(course.strip())