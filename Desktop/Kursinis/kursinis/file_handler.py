
import csv

def save_result(player1, player2, result):
    with open("results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([player1, player2, result])

def load_results():
    try:
        with open("results.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []
