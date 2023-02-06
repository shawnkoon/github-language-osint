# github-language-osint

OSINT tool to find Programming Language(s) used by Target GitHub Org/User

**PURELY EDUCATIONAL PURPOSE**

```bash
λ python -m ghkoon

Please enter github base URL (github.com|<custom_domain>)
-> github.com

Enter GitHub PAT token
->

Authenticating with github.com...
Hello, shawnkoon!

Enter name of the target user/org
-> octocat

Scanning...

Name of the Target  : octocat
Total repos scanned : 8
Total lines found   : 225111
+----------------------+------------+---------------+
| Programming Language | # of Lines | % Utilization |
+----------------------+------------+---------------+
| Ruby                 |     204865 |      91.006 % |
| CSS                  |      14950 |       6.641 % |
| HTML                 |       4338 |       1.927 % |
| Shell                |        910 |       0.404 % |
| JavaScript           |         48 |       0.021 % |
+----------------------+------------+---------------+
```

## How to Run

1. Create Python Virtual Environment.

   ```bash
   python -m venv .venv && \
       source .venv/bin/activate
   ```

2. Install necessary dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Execute the script.
   ```bash
   python -m ghkoon
   ```
