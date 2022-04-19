#!/usr/bin/python -B
import argparse
import requests
import json
import sys


url="https://api.github.com"

def getOpts () :
	parser = argparse.ArgumentParser(description='github api caller')
        parser.add_argument('-t', '--tokenfile', help="github API token")
        parser.add_argument('-o', '--org', help="repo owner")
        parser.add_argument('-f', '--format', action='store_true', help="repo owner")
	args = parser.parse_args()
	return args

def listRepos (org, head):
    """ Returns github group id when provided a github group slug
        Requires org to search, github group slug, and the headers (with token embedded)"""

    # Determine how many pages of results we're looking at
    results = {}
    results['Page1'] = requests.get(url + "/orgs/" + org + "/repos?per_page=100", headers=head)
    pages = int(results['Page1'].headers['link'].split(',')[1].split(';')[0].split('=')[-1].strip('>')) + 1
    repos = []
    for x in range(1, pages):
        results['Page' + str(x)] = requests.get(url + "/orgs/" + org + "/repos?per_page=100&page=" + str(x), headers=head).json()
    for key in results.keys():
        for repo in results[key]:
            repos.append(repo.get('name'))
    return repos

def main () :
    args = getOpts()

    # Check token stuffs
    if not args.tokenfile: 
        print "No token provided"
        # INVOCATION ERROR
        sys.exit(1)
    token_file = open(args.tokenfile,"r")
    my_token = token_file.readlines()[0].rstrip()
    head={ 'Authorization': 'token ' + my_token, "content-type":"text" }

    # Group we've chosen to grant read write access to for the new org.
    if not args.org:
        print "no github org provided"
        # INVOCATION ERROR
        sys.exit(1)

    repos = listRepos(args.org, head)
    for repo in repos:
        print repo
#        print(json.dumps(repos, indent=4, sort_keys=True))
#            print repo.get('name')
#            print(json.dumps(repo,indent=4))
            

if __name__ == "__main__":
    main()
