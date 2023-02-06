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
        for lang, lines in repo.get_languages().items():
            if lang in breakdown:
                breakdown[lang] += lines
            else:
                breakdown[lang] = lines
            total += lines
    
    print(f"Name of the Target  : {target}")
    print(f"Total repos scanned : {repos.totalCount}")
    print(f"Total lines found   : {total}")

    res = PrettyTable(field_names=["Programming Language", "# of Lines", "% Utilization"])
    
    for lang, lines in breakdown.items():
        res.add_row([lang, lines, f"{round((lines/total)*100,3)} %"])
    
    res.sortby = "# of Lines"
    res.reversesort = True
    res.align["Programming Language"] = 'l'
    res.align["# of Lines"] = 'r'
    res.align["% Utilization"] = 'r'

    print(res)
