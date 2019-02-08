# Logs Analysis Project

### by Ho Ting Chu

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The Logs Analysis Project is part of the Udacity Full Stack Web Developer Nanodegree's project 1.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.5.2
psycopg2 2.7.3.2
PostgreSQL 9.5.10
```
### Project Contents

This project consists of the following files:

``loganalysisfinal.py`` - The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.<br>
``newsdata.zip`` - A zip file containing a file that populates the news PostgreSQL database.<br>
``README.md`` - This read me file.

### Getting Started

Download the project zip file to your computer and unzip the file.

Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows) and navigate to the project directory.

### Bringing the VM up

```
vagrant up
```
The first time you run this command, it will take awhile, as Vagrant needs to download the VM image.

You can then log into the VM with the following command:
```
vagrant ssh
```
Once connected, be sure to navigate over to the directory containing the project.
```
cd /vagrant
```
We will then run the following command to log up the database.
```
unzip newsdata.zip
psql -d news -f newsdata.sql
```
### Running the queries

The ``loganalysisfinal.py`` contains everything needed to execute the 3 queries required in the project. To run it, simply execute the following command in the terminal.
```
python3 loganalysisfinal.py
```
The answers to the 3 queries will be printed onto the terminal.
### Shutting down

When you are finished with the VM, press ``Ctrl-D`` to log out of it and shut it down with this command:

```
vagrant halt
```
