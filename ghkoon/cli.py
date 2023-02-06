from github import Github
import getpass
from prettytable import PrettyTable

def run():
    hostname = ""
    g: Github = None

    while hostname == "":
        hostname = input("\nPlease enter github base URL (github.com|<custom_domain>)\n-> ")

    if hostname.__contains__('github.com'):
        gh_pat = getpass.getpass('\nEnter GitHub PAT token\n-> ')
        g = Github(login_or_token=gh_pat)
    else:
        gh_pat = getpass.getpass(f'\nEnter GitHub PAT token from {hostname}\n-> ')
        g = Github(base_url="https://{hostname}/api/v3", login_or_token=gh_pat)

    print()
    print(f"Authenticating with {hostname}...")
    print(f"Hello, {g.get_user().name}!")

    target = input("\nEnter name of the target user/org\n-> ")
    print("\nScanning...\n")
    repos = g.get_user(target).get_repos()

    breakdown = {}
    total = 0

    for repo in repos:
        for lang, bytes in repo.get_languages().items():
            if lang in breakdown:
                breakdown[lang] += bytes
            else:
                breakdown[lang] = bytes
            total += bytes
    
    print(f"Name of the Target  : {target}")
    print(f"Total Repos Scanned : {repos.totalCount}")
    print(f"Total Bytes Found   : {total}")

    res = PrettyTable(field_names=["Programming Language", "# of Bytes", "% Utilization"])
    
    for lang, bytes in breakdown.items():
        res.add_row([lang, bytes, f"{round((bytes/total)*100,3)} %"])
    
    res.sortby = "# of Bytes"
    res.reversesort = True
    res.align["Programming Language"] = 'l'
    res.align["# of Bytes"] = 'r'
    res.align["% Utilization"] = 'r'

    print(res)
