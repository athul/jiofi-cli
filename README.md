# Jiofi CLI

Jiofi-CLI is a Command Line Interface to check your Jiofi Network from your terminal than using the web interface. It only shows very specific details like battery details, data usage and devices connected.


## Using it

- Clone this Repo
- Install the Dependencies with `pip install -r requirements.txt`
- Run the program `python main.py` . You'll be welcomed by the help section

```text
NAME
    main.py

SYNOPSIS
    main.py COMMAND

COMMANDS
    COMMAND is one of the following:

     devices
       Prints a tabular view of all the connected devices in the network

     speed
       Prints the Current upload and download speed

     basic
       Get basic Details like Battery charge and state, no of connected devices and data used in <time>

     usage
       Get Data usage in Upload and Download data in <time>

     device
       Get Details of the device, Battery Charge, Battery State, Phone number or MSISDN
```

You can exit the help screen by pressing `q`(Vim Space)

## Contributing

This is under [MIT License](/LICENSE). All Pull Requests are welcome. If you find a bug feel free to open an [Issue](https://github.com/athul/jiofi-cli/issues)

### Made with

- Python
  - `requests` for HTTP requests
  - `fire` for CLI interface

#### Tested on

- Jiofi4
