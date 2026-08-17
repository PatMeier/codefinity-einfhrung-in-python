people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Write your code here
def people_information(dictionary, key):
      print("Name:", key)
      print("Age:", dictionary[key][0], "y.o.")
      print("Height:", dictionary[key][1], "cm")

# Testing
people_information(people_d, "Alex")
people_information(people_d, "Michelle")