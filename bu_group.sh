# This is pretty specific for the ASF
openssl s_client -connect ldap-master.apache.org:636 </dev/null | sed -n '/-----BEGIN CERT/,/-----END CERT/p' > ./.cert.pem
LDAPTLS_CACERT=.cert.pem ldapsearch -xLLL -H ldaps://ldap-master.apache.org -b ou=project,ou=groups,dc=apache,dc=org "(cn=$1)"

