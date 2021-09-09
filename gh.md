# gh

execute this command to create an alias to delete repo 
'''gh alias set repo-delete 'api -X DELETE "repos/$1"''''

### commands
```bash
# create a repo
gh repo create <repo-name>

# delete repo
gh repo-delete username/repo-name

# publish file 'hello.py' as a public gist
gh gist create --public hello.py

# create a gist with a description
gh gist create hello.py -d "my Hello-World program in Python"

# create a gist containing several files
gh gist create hello.py world.py cool.txt

# read from standard input to create a gist
gh gist create -

# create a gist from output piped from another command
cat cool.txt | gh gist create
```
