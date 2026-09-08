import re

text = """
My name is Rafi.
My email is rafi@gmail.com.
My phone number is 9876543210.
I have 25 books and 10 pens.
"""

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
phones = re.findall(r"\b[6-9]\d{9}\b", text)
numbers = re.findall(r"\b\d+\b", text)

print("Emails:", emails)
print("Phone Numbers:", phones)
print("Numbers:", numbers)