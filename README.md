CRON SCHEDULER INTERPRETER PROJECT
------------------------------------
Specification

We have a set of tasks, each running at least daily, which are scheduled using some simple values in a text file. You might recognise this from writing a crontab configuration in the past.
Examples of the scheduler config:
* `30 1 /bin/run_me_daily`
* `45 * /bin/run_me_hourly`
* `* * /bin/run_me_every_minute`
* `* 19 /bin/run_me_sixty_times`
The first field is the minute past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means that it should run for all values of that field.
We want you to write a command line program that takes a single argument. This argument is the simulated 'current time' in the format HH:MM. The program should accept config lines in the form above to STDIN and output the soonest time at which each of the commands will fire and whether it is today or tomorrow. In the case when the task should fire at the simulated 'current time' then that is the time you should output, not the next one.

For example given the above examples as input and the simulated 'current time' command-line
argument 16:10 the output should be:

1:30 tomorrow - /bin/run_me_daily
16:45 today - /bin/run_me_hourly
16:10 today - /bin/run_me_every_minute
19:00 today - /bin/run_me_sixty_times

DO NOT USE THIRD PARTY LIBRARIES

We want to run your code on the command line using an input like
./<your app> HH:MM < config
For example: ./application.py 16:10 < config
Where ‘config’ is a file containing various cron style inputs like we described above.
Your code must be able to be run this way.


File Structure
----------------------
* `.circleci` Folder contains the below:
  * `config.yml` File contains the config for circleCI CI/CD pipelines

* `Input_data`: Folder contains the below:
  * `cron_config.txt` File contains the default input cron schedule data

* `output_data`: Folder contains the below:
  * `outputFile.txt` File contains the output of interpretation from schedule data

* `Solution` Folder contains the following:
  * `__init__.py` Initiate folder as a module
  * `lyst.py` File contains the solution to interpret cron schedule tasks

* `Tests` Folder contains the following:
  * `__init__.py` Initiate folder as a module
  * `cron_test.txt` File contains test data for unit tests
  * `test.py` File contains unit tests for solution

* `__init__.py` Initiate parent folder as a module

* `.gitignore` List of files to ignore in github

* `Makefile` File contains easy installation for Unix-based systems and Mac

* `Readme.MD` Contains the readme for the project

* `Requirements.txt` File contains a list of packages required to run project.

* It is recommended you run the solution in a virtual environment. Please see https://docs.python.org/3/library/venv.html


USAGE INSTRUCTIONS
----------------------
***Warning***
You may need python3 command python command depending on what your cli is mapped to python3. In this case my python3 interpreter is invoked using python3. The same applies for pip/pip3

* Clone this repo to your computer.
* For mac please ensure you have xcode or download it from the app store (probably not needed)
* From your CLI install homebrew using `/usr/bin/ruby -e "$(curl -fsSL https:/raw.githubusercontent.com/Homebrew/install/master/install)"`
* After installing homebrew successfully, install python3 using `brew install python3`
* Check python3 installed correctly using `python3 --version` and this should return python3 version
* Install the requirements using `pip3 install -r requirements.txt`.
    * Make sure you use Python 3
* `cd` to the location of the parent directory in CLI
* Navigate to parent directory in CLI
* Execute `python3 solution/lyst.py <**:**> config` where '<**:**>' should be replaced with an appropriate time and 'config' can be replaced with an appropriate file path to be interpreted. Eg `python3 solution/lyst.py 1:00 input_data/cron_config.txt`
* Check `output_data/outputFile.txt` for the interpretation of results from default input data

RUNNING TESTS
----------------------
To run the tests associated with this project, navigate to the parent directory in your command line and run the following command.

* `python3 tests/test.py`

USING MAKEFILE
----------------------
To make life easier on UNIX-based systems and MAC os, there is a makefile for this project and the following commands could be run:
*  `Make setup` Installs requirements for project (mainly pylint)
*  `Make lint` Lints python files using pylint
*  `Make test` Runs the unit tests for this PROJECT
*  `Make all` Runs all the 3 above commands at once

Extending this
-------------------------

If you want to extend this work, here are a few places to start:

* Improve implementation of importing solution into unit testing script
* Use a class for solution instead of just methods
* Modify application to run as a micro-service
* Improve error messages using try except principles
* Give variables and methods meaningful names



## Credits

Lead Developer - Deoga Kofi


## License

The MIT License (MIT)

Copyright (c) 2020 Deoga Kofi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
