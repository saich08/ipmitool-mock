# ipmitool-sdr-mock

[![Build Status](https://dev.azure.com/ssc1729/ipmitool-sdr-mock/_apis/build/status/ssc1729.ipmitool-sdr-mock.build?branchName=main)](https://dev.azure.com/ssc1729/ipmitool-sdr-mock/_build/latest?definitionId=5&branchName=main)

`ipmitool-sdr-mock` is utility to mock the functionality of sub-command `sdr` in [ipmitool](https://github.com/ipmitool/ipmitool). 

# How to Install?

## From the Binary Releases

```
# download release
wget https://github.com/ssc1729/ipmitool-sdr-mock/releases/download/<version>/ipmitool-linux.zip

# unzip release
unzip ipmitool-linux.zip

# copy binary to /use/local/bin, need sudo privileges
sudo cp ipmitool /usr/local/bin/

# run ipmitool-sdr-mock commands
ipmitool sdr
ipmitool sdr elist
```

## From Source code

```
# clone repository, alternativly download from latest release
git clone https://github.com/ssc1729/ipmitool-sdr-mock

# create python virtual environment
cd ipmitool-sdr-mock && python3 -m virtualenv venv

# activate virtualenv
# this command changes on different operating systems, check below link for more info
# https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
source venv/bin/activate

# install requirements
pip3 install -r requirements.txt

# generate binary
cd src && pyinstaller --onefile --name ipmitool ipmitool-sdr-mock.py

# copy binary to /use/local/bin, need sudo privileges
cd dist && sudo cp ipmitool /usr/local/bin/

# run ipmitool-sdr-mock commands
ipmitool sdr
ipmitool sdr elist
```
