from colorama import Fore, Style, init

init()  # Initialise Colorama

def main():
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open("log.txt", "r") as file:
        for line in file:
            for key in counts:
                if key in line:
                    counts[key] += 1
                    if key == "ERROR":
                        print(Fore.RED + line.strip() + Style.RESET_ALL)
                    elif key == "WARNING":
                        print(Fore.YELLOW + line.strip() + Style.RESET_ALL)
                    elif key == "INFO":
                        print(Fore.GREEN + line.strip() + Style.RESET_ALL)

    with open("rapport.txt", "w") as report:
        for key, value in counts.items():
            report.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()
