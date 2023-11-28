import os

print("hello")
print(os.environ.get("CIRCLE_BRANCH"))
print(os.environ.get("TEST_VARIABLE"))
