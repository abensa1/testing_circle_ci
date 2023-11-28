import os

print("hello")
print(os.environ.get("CIRCLE_BRANCH"))
print(f'this is a form {os.environ.get("TEST_VARIABLE")}')
print('execution went well')