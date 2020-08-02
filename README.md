# 2ulb
Easy shortcut to make scripts executable and link them from /usr/local/bin

#Installation
```
git clone https://github.com/Zarcolio/2ulb
sudo python3 2ulb 2ulb.py
```

# Use 2ulb.py
`sudo python 2ulb.py <inputfile> [-f]`

Or after using 2ulb on 2ulb:

`sudo 2ulb <inputfile> [-f]`

Use -f to force an overwrite of the link in /usr/local/bin.

# Use 2ulb-curdir.sh
Install a symbolic link with 2ulb:

`sudo 2ulb 2ulb-curdir.sh`

Then use 2ulb-curdir:

`2ulb-curdir <filelist>`

For example:

`2ulb-curdir *.py`
