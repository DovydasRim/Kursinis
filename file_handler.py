import csv

def save_result(player1, player2, winner, filename="results.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player1, player2, winner])

def read_results(filename="results.csv"):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)
