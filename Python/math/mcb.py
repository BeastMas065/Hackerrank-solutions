from math import atan2,degrees
AB = int(input()) 
BC = int(input()) 
final1 = atan2(AB,BC) 
final2 = (round(degrees(final1))) 
print(str(final2) + chr(176))