def save_returns(books, log_file="returns.log", error_log_file="error.log"):
    """
    Saves returned books to the log file in append mode ('a') so previous days 
    are not overwritten, and uses a with statement for safe file handling.
    """
    try:
        with open(log_file, "a", encoding="utf-8") as log:
            for b in books:
                log.write(f"{b}\n")
    except Exception as e:
        # Save any unexpected writing errors to an error log instead of crashing silently
        with open(error_log_file, "a", encoding="utf-8") as err_log:
            err_log.write(f"Failed to write returns: {e}\n")

def process(day_file):
    """
    Reads a day's returned book file line by line and passes them to save_returns.
    """
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.read().splitlines()
        save_returns(books)
    except FileNotFoundError:
        print(f"Error: Day file '{day_file}' is missing.")