def main():
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open("log.txt", "r") as file:
        for line in file:
            for key in counts:
                if key in line:
                    counts[key] += 1

    with open("rapport.txt", "w") as report:
        for key, value in counts.items():
            report.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()
