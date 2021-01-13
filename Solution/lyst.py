from datetime import datetime                # Import datetime module to handle time inputs
import argparse                              # Import argparse to handle CLI inputs

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


def solve_run_time(time: str, txtfile: str):                  # Declare method to interpret cron scheduler inputs
    """Interpret next run of scheduler
    Args:
        time => String containing time input to compare to scheduler time eg 12:00
        txtfile => File containing scheduler data
    Returns:
        output => List of analysis for each scheduler task and when next they will run
    """
    now = datetime.strptime(str(time), "%H:%M")             # Initiate the time to compare with scheduler time
    # dd/mm/YY H:M:S
    hour_now = now.strftime("%H")                           # Extract the hour from the time input
    minute_now = now.strftime("%M")                         # Extract the minute from the time input
    mylines = open_files(txtfile)                            # Read input file using open_files method
    output = []                                             # Declare empty list for the output file
    for i in range(0, len(mylines)):                        # For each line in input file
        new_line = mylines[i].split()                       # Initiate newline to store contents of loop
        if new_line[0] == "*" and new_line[1]== "*":        # First logic to check if both schduler times are *
            output.append('{} today - {}'.format(now.strftime("%H:%M"), new_line[2]))
        elif new_line[0] == "*" and new_line[1] != "*":                        # Second logic to check only if schduler minute is *
            if new_line[0] == "*" and int(new_line[1]) > int(hour_now):
                output.append('{}:00 today - {}'.format(new_line[1], new_line[2]))
            elif new_line[0] == "*" and int(new_line[1]) == int(hour_now):
                output.append('{}:{} today - {}'.format(new_line[1], minute_now, new_line[2]))
            else:
                output.append('{}:00 tomorrow - {}'.format(new_line[1], new_line[2]))
        elif new_line[1] == "*" and new_line[0] != "*":                     # Third logic to check only if scheduler hour is *
            if new_line[1] == "*" and int(new_line[0]) < int(minute_now) and int(hour_now) == 23: # Logic to accommodate where time switches to midnight
                output.append('00:{} tomorrow - {}'.format(new_line[0], new_line[2]))
            elif new_line[1] == "*" and int(new_line[0]) >= int(minute_now):
                output.append('{}:{} today - {}'.format(hour_now, new_line[0], new_line[2]))
            elif new_line[1] == "*" and int(new_line[0]) < int(minute_now):
                output.append('{}:{} today - {}'.format(int(hour_now)+1, new_line[0], new_line[2]))
            else:
                output.append('{}:{} tomorrow - {}'.format(int(hour_now)+1, new_line[0], new_line[2]))
        else:                                                  # Fourth logic for other entries where both hour and minute of scheduler is *
            if new_line[0] != "*" and new_line[1] != "*" and int(new_line[1]) < int(hour_now):
                output.append('{}:{} tomorrow - {}'.format(new_line[1], new_line[0], new_line[2]))
            elif new_line[0] != "*" and new_line[1] != "*" and int(new_line[1]) == int(hour_now) and int(new_line[0]) < int(minute_now):
                output.append('{}:{} tomorrow - {}'.format(new_line[1], new_line[0], new_line[2]))
            else:
                output.append('{}:{} today - {}'.format(new_line[1], new_line[0], new_line[2]))
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

    parser = argparse.ArgumentParser(description='LystChallenge')                           # Initiate parser
    parser.add_argument('time', type= str)              # Create time cli argument with default time
    parser.add_argument('config_file',  metavar='path', type= str)           # Create config file cli argument with default config
    parser.add_argument('--save', required=False, default="./output_data/outputFile.txt", metavar='path', type= str)                  # Save
    args = vars(parser.parse_args())

    solved = solve_run_time(args['time'], args['config_file'])                    # Solve CLI inputs
    save_files(args['save'], solved)                                             # Save run results
    print("Output file can be found in {}".format(args['save']))                # Print some output to help user
    print('-----------------------------------')
    print('Sample output')
    print(solved[0])
