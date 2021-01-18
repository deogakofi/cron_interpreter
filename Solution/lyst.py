from datetime import datetime
import argparse

def open_files(txtfile: str):
    """Open files with scheduler data input
    Args:
        txtfile => File containing scheduler data
    Returns:
        mylines => Scheduler data in list format for analysis
    """

    mylines = []                             # Declare an empty list named mylines.
    with open (txtfile, 'rt') as myfile: # Open inputfile for reading text data.
        for myline in myfile:                # For each line, stored as myline,
            mylines.append(myline)           # add its contents to mylines.
    return mylines


def solve_run_time(time: str, txtfile: str):
    """Interpret next run of scheduler
    Args:
        time => String containing time input to compare to scheduler time eg 12:00
        txtfile => File containing scheduler data
    Returns:
        output => List of analysis for each scheduler task and when next they will run
    """
    now = datetime.strptime(str(time), "%H:%M")             # Initiate the time to compare with scheduler time
    # dd/mm/YY H:M:S
    hour_now = int(now.strftime("%H"))                          # Extract the hour from the time input
    minute_now = now.strftime("%M")                       # Extract the minute from the time input
    mylines = open_files(txtfile)                            # Read input file using open_files method
    output = []                                             # Declare empty list for the output file
    for i in range(0, len(mylines)):                        # For each line in input file
        new_line = mylines[i].split()                       # Initiate newline to store contents of loop
        scheduler_minute = new_line[0]
        scheduler_hour = new_line[1]
        schedule = new_line[2]
        if scheduler_minute == "*" and scheduler_hour== "*" and hour_now == 0:        # First logic to check if both schduler times are *
            output.append('0{}:{} today - {}'.format(hour_now, minute_now, schedule))
        elif scheduler_minute == "*" and scheduler_hour== "*" and hour_now != 0:
            output.append('{}:{} today - {}'.format(hour_now, minute_now, schedule))
        elif scheduler_minute == "*" and scheduler_hour != "*":                        # Second logic to check only if schduler minute is *
            if scheduler_minute == "*" and int(scheduler_hour) > hour_now:
                output.append('{}:00 today - {}'.format(scheduler_hour, schedule))
            elif scheduler_minute == "*" and int(scheduler_hour) == hour_now:
                output.append('{}:{} today - {}'.format(scheduler_hour, minute_now, schedule))
            else:
                output.append('{}:00 tomorrow - {}'.format(scheduler_hour, schedule))
        elif scheduler_hour == "*" and scheduler_minute != "*":                     # Third logic to check only if scheduler hour is *
            if scheduler_hour == "*" and int(scheduler_minute) < int(minute_now) and hour_now == 23: # Logic to accommodate where time switches to midnight
                output.append('00:{} tomorrow - {}'.format(scheduler_minute, schedule))
            elif scheduler_hour == "*" and int(scheduler_minute) >= int(minute_now) and hour_now == 0:
                output.append('0{}:{} today - {}'.format(hour_now, scheduler_minute, schedule))
            elif scheduler_hour == "*" and int(scheduler_minute) >= int(minute_now) and hour_now != 0:
                output.append('{}:{} today - {}'.format(hour_now, scheduler_minute, schedule))
            elif scheduler_hour == "*" and int(scheduler_minute) < int(minute_now):
                output.append('{}:{} today - {}'.format(hour_now+1, scheduler_minute, schedule))
        else:                                                  # Fourth logic for other entries where both hour and minute of scheduler is *
            if scheduler_minute != "*" and scheduler_hour != "*" and int(scheduler_hour) < hour_now:
                output.append('{}:{} tomorrow - {}'.format(scheduler_hour, scheduler_minute, schedule))
            elif scheduler_minute != "*" and scheduler_hour != "*" and int(scheduler_hour) == hour_now and int(scheduler_minute) < int(minute_now):
                output.append('{}:{} tomorrow - {}'.format(scheduler_hour, scheduler_minute, schedule))
            else:
                output.append('{}:{} today - {}'.format(scheduler_hour, scheduler_minute, schedule))
    return output

def save_files(file_name: str, file: str):
    """Save files from interpreter
    Args:
        txtfile => File containing scheduler data
    Returns:
        mylines => Scheduler data in list format for analysis
    """
    with open(file_name, "w") as outfile:                # Open file to save outputs
        outfile.write("\n".join(file))                  # Write each line of the file with a break at the end to create new line

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='LystChallenge')
    parser.add_argument('time', type= str)
    parser.add_argument('config_file',  metavar='path', type= str)
    parser.add_argument('--save', required=False, default="./output_data/outputFile.txt", metavar='path', type= str)
    args = vars(parser.parse_args())

    solved = solve_run_time(args['time'], args['config_file'])
    save_files(args['save'], solved)
    print("Output file can be found in {}".format(args['save']))                # Print some output to help user
    print('-----------------------------------')
    print('Sample output')
    print(solved[0])
