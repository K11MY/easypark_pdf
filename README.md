# Rename Easypark PDFs 

## What do?

Easypark uses random numbers to name their parking receipts e.g Parking_348483. This python script will rename your parking receipt to the date you purchased your parking and price (in cents) e.g Parking_20221101_1760.

## How do?
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
python3 -m venv venv
```
Activate the virtual environment
```sh
source venv/bin/activate
```
Install requirements
```sh
python3 -m pip install .
```

Now that you have the environment set up download all your easy park receipts and put them into the `easypark` directory. 

## Make work?

Once all parking receipts are in the directory run:
```sh
easypark-pdf
```

Optionally specify the directory
```sh
easypark-pdf [--dir/-d] /var/tmp/
```

## Now what?

After the file has been rename you can deactivate the virtual environment by typing
```sh
deactivate
```
