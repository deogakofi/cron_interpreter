from datetime import datetime
import argparse

def openFiles(txtfile: str):
    mylines = []                             # Declare an empty list named mylines.
    with open (txtfile, 'rt') as myfile: # Open lorem.txt for reading text data.
        for myline in myfile:                # For each line, stored as myline,
            mylines.append(myline)           # add its contents to mylines.
    return mylines


def solveRunTime(time: str, txtfile: str):
    now = datetime.strptime(str(time), "%H:%M")
    # dd/mm/YY H:M:S
    hour_now = now.strftime("%H")
    minute_now = now.strftime("%M")
    start = datetime.now()
    mylines = openFiles(txtfile)
    output = []
    for i in range(0, len(mylines)):
        new_line = mylines[i].split()
        if new_line[0] == "*" and new_line[1]== "*":
            output.append('{} today - {}'.format(now.strftime("%H:%M"), new_line[2]))
        elif new_line[0] == "*" and new_line[1] != "*":
            if new_line[0] == "*" and int(new_line[1]) > int(hour_now):
                output.append('{}:00 today - {}'.format(new_line[1], new_line[2]))
            elif new_line[0] == "*" and int(new_line[1]) == int(hour_now):
                output.append('{}:{} today - {}'.format(new_line[1], minute_now, new_line[2]))
            else:
                output.append('{}:00 tomorrow - {}'.format(new_line[1], new_line[2]))
        elif new_line[1] == "*" and new_line[0] != "*":
            if new_line[1] == "*" and int(new_line[0]) < int(minute_now) and int(hour_now) == 23:
                output.append('00:{} tomorrow - {}'.format(new_line[0], new_line[2]))
            elif new_line[1] == "*" and int(new_line[0]) >= int(minute_now):
                output.append('{}:{} today - {}'.format(hour_now, new_line[0], new_line[2]))
            elif new_line[1] == "*" and int(new_line[0]) < int(minute_now):
                output.append('{}:{} today - {}'.format(int(hour_now)+1, new_line[0], new_line[2]))
            else:
                output.append('{}:{} tomorrow - {}'.format(int(hour_now)+1, new_line[0], new_line[2]))
        else:
            if new_line[0] != "*" and new_line[1] != "*" and int(new_line[1]) < int(hour_now):
                output.append('{}:{} tomorrow - {}'.format(new_line[1], new_line[0], new_line[2]))
            elif new_line[0] != "*" and new_line[1] != "*" and int(new_line[1]) == int(hour_now) and int(new_line[0]) < int(minute_now):
                output.append('{}:{} tomorrow - {}'.format(new_line[1], new_line[0], new_line[2]))
            else:
                output.append('{}:{} today - {}'.format(new_line[1], new_line[0], new_line[2]))
    end = datetime.now()
    return output

def saveFiles(fileName: str, file: str):
    with open(fileName, "w") as outfile:
        outfile.write("\n".join(file))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='LystChallenge')
    parser.add_argument('--time', required=False, default="16:10")
    parser.add_argument('--config_file', required=False, default="../input_data/cron_config.txt")
    parser.add_argument('--save', required=False, default="../output_data/outputFile.txt")
    args = vars(parser.parse_args())

    solved = solveRunTime(args['time'], args['config_file'])
    saveFiles(args['save'], solved)
