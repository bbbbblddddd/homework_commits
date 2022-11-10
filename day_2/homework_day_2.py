empty_1 = []

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"] 
 
 
 #1. Add "Edinburgh Waverley" to the end of the list
stops.insert(6, "Edinburgh Waverley")

 #2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen Street")

 #3. Add "Polmont" at the appropriate pooint (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")

 #4. Print out the index position of "Linlithgow"
index = stops.index('Linlithgow')     
print(index)

 #5. Remove "Livingston" from the list using its name
 stops.remove("Livingstone")

 #6. Delete "Cumbernauld" from the list by index
removed_stops = stops.pop(2)
print(stops)

# ALSO len(stops)

 #7. Print the number of stops there are in the list
num_of_stops = len(stops)
print(num_of_stops)

# ALSO stops.sort()


 #8. Sort the list alphabetically
stops.sort()
print(stops)

 #9. Reverse the positions of the stops in the list
stops.reverse()
print(stops)

 #10 Print out all the stops using a for loop
for stop in stops:
    print(stop)

#  FOR EACH ITEM IN STOPS.... IT PRINTS EACH STOP

