# tools
Warwalrux' tools for doing $things

### asf // Apache Multi-Tool
Warwalrux one-size-fits-all apache do-er.

asf does a lot of basic system-based apache.org oriented $stuff
run `asf help` for details

### checkip
check abuseipdb.com for the provided IP address.
The script returns the number of times it's been reported.

### dump
a python-based tool for examining / converting various object types with Jinja.

### evim + ecat // Apache Tool
hiera-eyaml wrapper evim (encrypted vim) and ecat (encrypted cat) 
*NB: which doesn't _actually_ specify vim, just the default system editor --*

evim & ecat interpret the path for git checkouts in $launchpad for the following repos:
	- github.com/apache/infrastructure-p6
	- github.com/apache/infrastrucure-puppet

this allows you to invoke eyaml-edit or eyaml-cat with all the fixins from anywhere in either repo
to edit eyaml files.

### merge
a python based ditty that can load files containing one of several different common
formats (ast, picl, yaml, json) and merge them using patented DEEP MERGE technology.

### nosleep
Generic Mouse wiggler using xdotool

### otp-md5 / donkeyrunner
Intercept the otp-md5 calls for OPIE implementations and return only the good
bits.

REQUIRES: ~/.$USER.cred with a valid OTP-MD5 password inside on a single line.

### ghquery
Query GitHub / return result object

requires a Personal Access Token in a file somewhere.

### ghrepo
Query github for a single repository object

requires a Personal Access Token in a file somewhere.

### ghutils

ghutils is a collection of useful GitHub actions.
it also holds GraphQL queries and stuff. (GraphQL is arcane AF) 

### rdns
Python script that resolves IP addresses in output that is piped to it

### repo
An Apt repository tool that allows you to manage repositories individually
list, update, and search for packages by repo, for the easy-making of life.

### pic-sort

pic-sort is a script that leverages exif utilities and and heic converter to rename and
organize jpg and heic files. for instructions: run the script with no arguments.

REQUIRES: exif, heif-gdk-pixbuf

### mkics

mkics is a ICS file creator with a prompt that will generate a potrable .ics file

### mkqr

mkqr generates QR codes.
