heading = input("Heading : ")
object = input("Object : ")
verb1 = input("Verb : ")
word1 = input("Word1 : ")
word2 = input("Word2 : ")

print(f"About {heading}")
madlib = f"{object} programming is the process " \
         f"of telling a {object.lower()} to do things a certain way. " \
         f"A person who {verb1} writes {word1} is called a {object.lower()} {word2}"

print(madlib)
