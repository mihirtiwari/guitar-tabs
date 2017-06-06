# Tab Downloader
This project is a way for people to get guitar tabs quickly downloaded to their computer using command line. The tabs are the top 3 results and are based by default on reviews, but there is also the option of basing it off of the number of stars.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need to have at least Python 2.7. It can be installed by going to https://www.python.org/downloads/ and following the instructions. This can also be installed using Homebrew on Mac (https://brew.sh/#install) with the command:
<br><br>
`brew install python`
<br><br>
You should also install *virtualenv* using:
<br><br>
`pip install virtualenv`
<br><br>
The virtual environment can be created using `virtualenv <name of env>`. Every time you want to activate the virtual environment, you run `source <name of virtualenv>/bin/activate` and every time you want to deactivate it you run `deactivate`

### Installation
Clone the repository using:
<br><br>
`git clone https://github.com/mihirtiwari/guitar-tabs.git`
<br><br>
You also need to install the supporting libraries. A *requirements.txt* file has been provided. You can install the libraries by running:
<br><br>
`pip install requirements.txt`
<br><br>
**NOTE:** Unless you want to install the packages globally, it is recommended to first activate your virtual environment and then install the packages.

### Running the script
Navigate to where you cloned the repository and activate your virtual environment. Then run:
<br><br>
`python scrape.py <Name of song and/or artist> </s if sorted by # of stars>`
<br><br>
The script will run and tell you if it was able to find the tab or not. By default, it will show the top 3 results based on number of reviews. If you add */s* to the end, it will rank it by the number of stars. It will also ask for the directory in which to download the tabs. By default, it will search for a place in your home directory.

## Author
**Mihir Tiwari** - Github: [@mihirtiwari](https://github.com/mihirtiwari/) or Email: mtiw999@gmail.com

## License
This project is licensed under the MIT License - see [LICENSE](./LICENSE) for details
