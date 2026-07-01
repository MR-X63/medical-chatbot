import csv

def get_hospitals(specialty, city=None):
    matches = []
    
    with open("hospitals.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if specialty.lower() in row["specialty"].lower():
                if city is None or city.lower() == row["city"].lower():
                    matches.append(row)
    
    return matches
