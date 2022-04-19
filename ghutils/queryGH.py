#!/usr/bin/python3 -B
import argparse
import requests
import json
import sys
import jinja2

url="https://api.github.com"

def getOpts():
    parser = argparse.ArgumentParser(description='github api caller')
    parser.add_argument('-t', '--tokenfile', help="github API token")
    parser.add_argument('-q', '--query', help="Query String")
    parser.add_argument('-j', '--j2', help="jinja2 formatting string")
    args = parser.parse_args()
    return args

def queryGH (query, head):
    """ Returns github group id when provided a github group slug
        Requires org to search, github group slug, and the headers (with token embedded)"""

    # Determine how many pages of results we're looking at
    results = {}
    t = requests.get(url + "/search/code?per_page=100&q=" + query, headers=head)
    if t.status_code != 200:
        print(t.json())
        sys.exit(1)

#    for k, v in t.json().items():
#        if k not in ["items"]:
#            print("%s: %s" %(k, v))

    if t.json()["incomplete_results"]:
        print("Incomplete result set delivered.")
    else:
        results = t.json()

    return results

def main () :
    args = getOpts()
    
    # Check token stuffs
    if not args.tokenfile: 
        print("No token provided")
        sys.exit(1)
    token_file = open(args.tokenfile,"r")
    my_token = token_file.readlines()[0].rstrip()
    head={ 'Authorization': 'token ' + my_token, "content-type":"text" }

    # Group we've chosen to grant read write access to for the new org.
    if not args.query:
        print("no github query string provided")
        # INVOCATION ERROR
        sys.exit(1)

    results = queryGH(args.query, head)

    for result in results["items"]:
        if args.j2:
            t = jinja2.Template(args.j2)
            print(t.render(result=result))
        else:
            print(result)

    print("Total Results: %s" % results["total_count"])
            

if __name__ == "__main__":
    main()
