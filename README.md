# PR - AGENT

AI sends pull requests for features you request in natural language

## Usage

```bash
python pr.py -h                                                                                              
usage: pr.py [-h] -f FILE -i INSTRUCTION [-r REPO] [-d] [-pr]

Edit a section of code, PR with changes.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  location of a file
  -i INSTRUCTION, --instruction INSTRUCTION
                        instruction on how to edit the file
  -r REPO, --repo REPO  location to git repo
  -d, --diff            show diff
  -pr, --pull-request   add change, commit, push and raise a PR
```

## Example

```bash
OPENAI_KEY="<key>" GH_TOKEN="<token>" python pr.py -f examples/bug.py -i "Rewrite the given code and fix any bugs in the program." -d --pr
```

> Please replace the OPENAI key and GH_TOKEN with your own.

Here is a real PR opened by this above command: https://github.com/AvaterClasher/PR-agent/pull/1