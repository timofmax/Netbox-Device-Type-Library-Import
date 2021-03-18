import os
from dotenv import load_dotenv
load_dotenv()

REPO_URL = str(os.getenv("REPO_URL")) if str(os.getenv("REPO_URL")) != None else input("Please provide source repo: ")
NETBOX_URL = str(os.getenv("NETBOX_URL")) if str(os.getenv("NETBOX_URL")) != None else input(
    "Please provide NETBOX_URL: ")
NETBOX_TOKEN = str(os.getenv("NETBOX_TOKEN")) if str(os.getenv("NETBOX_TOKEN")) != None else input(
    "Please provide NETBOX_TOKEN: ")

MANDATORY_ENV_VARS = ["REPO_URL", "NETBOX_URL", "NETBOX_TOKEN"]

for var in MANDATORY_ENV_VARS:
    if var not in os.environ:
        REPO_URL = str(os.getenv("REPO_URL")) if str(os.getenv("REPO_URL")) != None else input(
                                                                                        "Please provide source repo: ")
        NETBOX_URL = str(os.getenv("NETBOX_URL")) if str(os.getenv("NETBOX_URL")) != None else input(
                                                                                        "Please provide NETBOX_URL: ")
        NETBOX_TOKEN = str(os.getenv("NETBOX_TOKEN")) if str(os.getenv("NETBOX_TOKEN")) != None else input(
                                                                                        "Please provide NETBOX_TOKEN: ")
        

