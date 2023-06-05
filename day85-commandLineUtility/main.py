import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

# add cmd line arguments
parser.add_argument("url", help="url of the file you want to download")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# pars the arguments
args = parser.parse_args()

print(args.url)
print(args.output, type(args.output))

download_file(args.url, args.output)


