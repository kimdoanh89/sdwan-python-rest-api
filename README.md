# sdwan-python-rest-api

## SD-WAN 20.3.1 in GNS3

This public repo contains python code that can be used to interact with the Cisco SD-WAN vManage REST API. The environment is pre-configured to access my local SD-WAN lab in GNS3. 

You can edit the variables in the `vmanage/constants.py` to point to your own vManage instance. 


### Topology

![Alt text](images/07_RG.png)

## Current functions
The code contains REST API calls to authenticate and interact with Cisco SD-WAN vManage 20.3.1. Currently, it supports the following functions:
```bash
-> % python sdwancli.py         
Usage: sdwancli.py [OPTIONS] COMMAND [ARGS]...

  Command line tool for deploying templates to CISCO SDWAN.

Options:
  --help  Show this message and exit.

Commands:
  bfd       Commands monitor bfd sessions: link --state, summary
  device    Commands to manage device: list, show, create
  template  Commands to manage template: create, delete, list, show
```

And for each command, it support some subcommands, for example:

```bash
-> % python sdwancli.py template
Usage: sdwancli.py template [OPTIONS] COMMAND [ARGS]...

  Commands to manage template: create, delete, list, show

Options:
  --help  Show this message and exit.

Commands:
  create  Create a feature template
  delete  Delete a feature template
  list    Get template list
  show    Show details of a feature template
```

## Requirements

To use this code you will need:

- Python 3.8+
- vManage user login details. (User should have privilege level to configure policies)

## Install and Setup
Clone the code to local machine.
```bash
git clone https://github.com/kimdoanh89/sdwan-python-rest-api
cd sdwan-python-rest-api
```

Setup Python Virtual Environment (requires Python 3.8+)
```bash
python3.8 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
A .py file with the Cisco SD-WAN credentials has been created in `vmanage/constants.py`. You can edit the variables in the file to point to your own vManage instance.

## Example 
- Device list

```bash
python sdwancli.py device list
```

![Alt text](images/01_device_list.png)

- Template list

```bash
python sdwancli.py template list
```
![Alt text](images/01_template_list.png)

- BFD sessions monitor

```bash
python sdwancli.py bfd link --state up
python sdwancli.py bfd link --state down
```
![Alt text](images/03_bfd_link_up_down.png)