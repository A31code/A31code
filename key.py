import keyword

print("Python keywords are:")
for kw in keyword.kwlist:
    print(kw)

print(f"\nTotal number of keywords: {len(keyword.kwlist)}")
# The above code imports the keyword module and prints all the keywords in Python.
# It also prints the total number of keywords.
# The keyword module provides a list of all the keywords in Python.
# The keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names).