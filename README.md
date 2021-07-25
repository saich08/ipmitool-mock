# ipmitool-mock

[![Build Status](https://dev.azure.com/ssc1729/ipmitool-mock/_apis/build/status/ssc1729.ipmitool-mock.build?branchName=main)](https://dev.azure.com/ssc1729/ipmitool-mock/_build/latest?definitionId=7&branchName=main)

`ipmitool-mock` is utility to mock the functionality [ipmitool](https://github.com/ipmitool/ipmitool). 

# How to Install?

## From the Binary Releases (For Linux)

```
# download release file
>> wget https://github.com/ssc1729/ipmitool-mock/releases/download/<version>/ipmitool-linux.zip

# unzip release file
>> unzip ipmitool-linux.zip

# copy binary file to /use/local/bin, need sudo privileges
>> sudo cp ipmitool /usr/local/bin/

# run ipmitool-mock commands
>> ipmitool sdr
>> ipmitool sdr elist
```

## From Source code

```
# clone repository, alternativly download from latest release
>> git clone https://github.com/ssc1729/ipmitool-mock

# create python virtual environment
>> cd ipmitool-mock
>> python3 -m virtualenv venv

# activate virtualenv
# this command changes on different operating systems, check below link for more info
# https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
>> source venv/bin/activate

# install requirements
>> pip3 install -r requirements.txt

# generate binary file
>> cd src
>> pyinstaller --onefile --name ipmitool ipmitool-mock.py

# copy binary file to /use/local/bin, need sudo privileges
# for windows, add ipmitool binary file to environment path
>> cd dist
>> sudo cp ipmitool /usr/local/bin/

# run ipmitool-mock commands
>> ipmitool sdr
>> ipmitool sdr elist
```

*Note: For Windows use PowerShell*

## Sample output

```
>> ipmitool sdr
System Fan 1     | 9403 RPM          | ok
System Fan 2     | 9509 RPM          | ok
System Fan 3     | 9398 RPM          | ok
System Fan 4     | 9804 RPM          | ok
PS1 Input Power  | 113 Watts         | ok
PS2 Input Power  | 115 Watts         | ok
PS1 Temperature  | 21 degrees C      | ok
PS2 Temperature  | 21 degrees C      | ok
PS1 Status       | 0x00              | ok
PS2 Status       | 0x00              | ok

>> ipmitool sdr elist
System Fan 1     | 0Ah | ok | 10.1 | 9262 RPM
System Fan 2     | 0Bh | ok | 10.2 | 9971 RPM
System Fan 3     | 0Ch | ok | 10.3 | 9582 RPM
System Fan 4     | 0Dh | ok | 10.4 | 9990 RPM
PS1 Input Power  | 01h | ok | 11.1 | 104 Watts
PS2 Input Power  | 02h | ok | 11.2 | 118 Watts
PS1 Temperature  | 01h | ok | 11.1 | 28 degrees C
PS2 Temperature  | 02h | ok | 11.2 | 29 degrees C
PS1 Status       | 01h | ok | 11.1 | Presence detected 
PS2 Status       | 02h | ok | 11.2 | Presence detected
```
