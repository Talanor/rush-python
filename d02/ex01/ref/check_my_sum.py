#!/bin/python3

import sys
import argparse
import requests
import hashlib
import base64
import urllib.parse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Output the content of a "
                                     "file in base 64")
    parser.add_argument("url", help="Valid url")
    parser.add_argument("hash_md5", help="The md5 hash of the file you want to"
                        "get.")
    return parser.parse_args()


def get_page_content(session, url):
    try:
        response = session.get(url)
    except requests.ConnectionError:
        print('ERROR: Unable to access the given URL.', file=sys.stderr)
        sys.exit(1)
    return response.json()


def get_correct_file_content(session, url, hash_md5, file_infos):
    for file_inf in file_infos:
        valid_url = urllib.parse.urljoin(url, file_inf['Local Url'])
        resp = session.get(valid_url)
        if resp.status_code != 200:
            continue
        md5 = hashlib.md5(resp.content).hexdigest()
        if md5 == hash_md5:
            return resp.content
    return None


def main():
    args = parse_arguments()
    session = requests.session()
    file_infos = get_page_content(session, args.url)
    file_content = get_correct_file_content(session, args.url, args.hash_md5,
                                            file_infos)
    if not file_content:
        print('ERROR: Unable to find the file corresponding to the given '
              'md5sum ("%s").' % (args.hash_md5), file=sys.stderr)
    else:
        print(base64.b64encode(file_content).decode())
    session.close()


if __name__ == "__main__":
    main()
