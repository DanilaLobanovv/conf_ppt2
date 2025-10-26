import sys
import json
import yaml
import urllib.request
from urllib.parse import urlparse


try:
    with open(sys.argv[1], 'r') as file:
        data = yaml.safe_load(file)
except FileNotFoundError:
    print("File not found")
    exit()

if not isinstance(data["URL"], str):
    print("URL is incorrect")
    exit()

try:
    result = urlparse(data["URL"])
    if not all([result.scheme, result.netloc]):
        print("URL incorrect")
        exit()
except:
    exit()

if not isinstance(data["package-name"], str):
    print("package-name is incorrect")
    exit()

if not isinstance(data["mode"], int):
    print("mode is incorrect")
    exit()

if not isinstance(data["package-version"], str):
    print("package-version is incorrect")
    exit()

if not isinstance(data["ASCII-mode"], int):
    print("ASCII-mode is incorrect")
    exit()

if not isinstance(data["depth"], int):
    print("depth is incorrect")
    exit()

if not isinstance(data["package-filter-str"], str):
    print("package-filter-str is incorrect")
    exit()

url = data["URL"]
package_name = data["package-name"]
version = data["package-version"]
full_url = f"{url}/{package_name}/{version}"

with urllib.request.urlopen(full_url) as response:
    data2 = json.loads(response.read().decode())
    dependencies = data2.get('dependencies', {})

for dep_name, dep_version in dependencies.items():
        print(f"{dep_name}: {dep_version}")