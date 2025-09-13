# Function to record multiple 10 km run times and calculate the average
def run_timing():
    time_of_runs = []

    while True:
        run_time = input("Enter 10 km run time in minutes (press Enter to finish): ")
        if not run_time:
            break
        try:
            time_of_runs.append(float(run_time))
        except ValueError:
            print("Please enter a valid number.")

    runs_count = len(time_of_runs)

    if runs_count > 0:
        total_time = sum(time_of_runs)
        time_avg = total_time / runs_count
        print(f"Average of {time_avg:.1f} minutes over {runs_count} runs")
    else:
        print("No run times entered.")


run_timing()


# Function to extract a specific number of digits before and after the decimal point from a float
def truncate_float(number, before, after):
    number_str = str(number)
    whole_part_str, frac_part_str = number_str.split(".")

    # -before: = take the last before digits.
    # :before = take the first before digits.

    new_whole = whole_part_str[-before:]
    new_frac = frac_part_str[:after]

    new_number_str = new_whole + "." + new_frac
    return float(new_number_str)
