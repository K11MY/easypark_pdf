# Rename Easypark pdf 

Easypark uses random numbers to name their parking receipts e.g Parking_348483. This python script will rename your parking receipt to the date you purchased your parking and start/end time e.g Parking_20221101_0800_1700.

## Getting started 
Pre-reqs
* python3 

Clone the repo
```sh
git clone https://github.com/K11MY/easypark_pdf.git
```
Change into the project directory
```sh
cd easypark_pdf
```
Create a python virtual environment 
```sh
python3 -m venv venvName
```
Activate the virtual environment
```sh
source ./venvName/bin/activate
```
Install requirements
```sh
pip3 install -r requirements.txt
```
Now that you have the environment set up download all your easy park receipts and put them into the Easypark directory. 

Once all parking receipts are in the directory run:
```sh
python3 easypark.py
```
After the file has been rename you can deactivate the virtual environment by typing
```sh
deactivate
```
