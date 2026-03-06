import re

# Match a string that has 'a' followed by zero or more 'b'
ptr = r"ab*"
txt = "abbb a ab aaaa"

matches = re.findall(ptr, txt)
print(matches)
# Match a string that has 'a' followed by two to three 'b'
ptr = r"ab{2,3}"
txt = "ab abb abbb abbbb"

matches = re.findall(ptr, txt)
print(matches)
# Find sequences of lowercase letters joined with an underscore
ptr = r"[a-z]+_[a-z]+"
txt = "hello_world test_example wrong_Example another_one"

matches = re.findall(ptr, txt)
print(matches)

# Find sequences of one uppercase letter followed by lowercase letters
ptr = r"[A-Z][a-z]+"
txt = "Hello world Python Is Great"

matches = re.findall(ptr, txt)
print(matches)

# Match a string that has 'a' followed by anything, ending in 'b'
ptr = r"a.*b"
txt = "acb a123b axxxb ab a_test_b"

matches = re.findall(ptr, txt)
print(matches)
# Replace all occurrences of space, comma, or dot with a colon
txt = "Hello, world. Python is fun"
result = re.sub(r"[ ,\.]", ":", txt)

print(result)
# Convert snake_case string to camelCase
def snake_to_camel(txt):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), txt)

txt = "hello_world_python"
print(snake_to_camel(txt))
# Split a string at uppercase letters
txt = "HelloWorldPythonIsCool"
result = re.split(r"(?=[A-Z])", txt)

print(result)
# Insert spaces between words starting with capital letters
txt = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", txt).strip()

print(result)
# Convert camelCase string to snake_case
def camel_to_snake(txt):
    return re.sub(r"([A-Z])", r"_\1", txt).lower()

txt = "helloWorldPython"
print(camel_to_snake(txt))