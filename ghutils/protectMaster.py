#!/usr/bin/python -B
import argparse
import requests
import json
import sys

from listRepos import listRepos


url="https://api.github.com"

def getOpts () :
	parser = argparse.ArgumentParser(description='github api caller')
        parser.add_argument('-t', '--tokenfile', help="github API token")
        parser.add_argument('-o', '--org', help="repo owner")
	parser.add_argument('-r', '--repo', help='token file')
	parser.add_argument('-f', '--format', action='store_true', help='formatted output')
	args = parser.parse_args()
	return args

def repoInOrg (org, victim, head):
    """ Returns github group id when provided a github group slug
        Requires org to searh, victim repository and the headers (with token embedded)"""
    group_id = requests.get(url + "/repos/" + org + "/" + victim + "/branches", headers=head).json()
    return group_id

def main () :
    args = getOpts()

    # Check token stuffs
    if not args.tokenfile: 
        print "No token provided"
        # INVOCATION ERROR
        sys.exit(1)
    token_file = open(args.tokenfile,"r")
    my_token = token_file.readlines()[0].rstrip()
    head={ 'Authorization': 'token ' + my_token }

    # Group we've chosen to grant read write access to for the new org.
    if not args.repo:
        print "no github repo provided"
        # INVOCATION ERROR
        sys.exit(1)

    repo = repoInOrg(args.org, args.repo, head)
    if hasattr(repo, 'message'):
        print "no such repo exists in the provided org"
        # RESOURCE NOT FOUND ERROR
        sys.exit(2)
    else:
        if args.format:
            print(json.dumps(repo, indent=4, sort_keys=True))
        else:
            for branch in repo:
                    if branch['name'] == "master":

if __name__ == "__main__":
    main()
