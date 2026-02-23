"""
Today's Work Design System
combine logic like real s/w engineers 
Eg: Multiple rules => real application
    Multiple inputs => Decision depends on 
    o/p is not just a value=> decision + status 

Transportation Domain
    => Metro Fare Calculation system

Problem Statement:-
    Metro Ticketing System


    System Should:
    1. Accept no of stations travelled
    2. Base Price
    3. Check travel type (peak/ Non Peak)
    4. Calcualte Fare
    5. Apple Daily cap if Exceeded

    Rules:
    Base Price = 20/-
    Plus 5 per Station
    Peak hours  => 20% Extra
    maximum Daily Cap 100

"""

def calcualte_fare(stations,peak):

    base_fare = 20
    fare = base_fare + (stations *5)
    if peak == "yes":
        fare += fare * 0.20
    if fare > 100:
        fare = 100

    return fare

#user inputs 
stations = int(input("Enter no.of stations travelled:"))
peak = input("Is It peak hour?(yes/no):").lower()

# Function Call
final_fare = calcualte_fare(stations,peak)
print(final_fare)