# tools
Warwalrux' tools for doing $things

### asf // Apache Tool
Warwalrux one-size-fits-all apache do-er.

asf does a lot of basic system-based apache.org oriented $stuff


### bu_groups // Apache Tool
This is an ASF specific script that allows a user to quickly back up
an LDAP group in the "ou=projects,ou=groups,dc=apache,dc=org" namespace
as an LDIF file, capable of being restored via ADS or ldapmodify.

./bu_groups $projectname >> $projectname.ldif


### checkip
check abuseipdb.com for the provided IP address.
The script returns the number of times it's been reported.


### dpkg-history
a yum-history type tool for dpkg based systemd

### evim  // Apache Tool
hiera-eyaml wrapper evim (encrypted vim) 
*NB: which doesn't _actually_ specify vim, just the default system editor --*

evim interprets the path for git checkouts in $launchpad for the following repos:
	- github.com/apache/infrastructure-p6
	- github.com/apache/infrastrucure-puppet

this allows you to invoke eyaml-edit with all the fixins from anywhere in either repo
to edit eyaml files.

### nosleep
Generic Mouse wiggler using xdotool

### otp-md5 / donkeyrunner
Intercept the otp-md5 calls for OPIE implementations and return only the good
bits.

REQUIRES: ~/.$USER.cred with a valid OTP-MD5 password inside on a single line.

### rdns
Python script that resolves IP addresses in output that is piped to it

### repo
An Apt repository tool that allows you to manage repositories individually
list, update, and search for packages by repo, for the easy-making of life.

