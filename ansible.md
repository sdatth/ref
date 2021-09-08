# Ansible

## commands

```bash
# test connection
ansible all -m ping

# test particular hosts connection
ansible nodes -m ping

# execute particular command 
ansible nodes -m shell -a "lsb_release -a"
ansible nodes -a "lsb_release -a"

# execute a playbook {-K flag is used to input superuser password}
ansible-playbook playbook.yml -K

# run a play book locally
ansible-playbook --connection=local --inventory 127.0.0.1, playbook.yml

# vault commands
ansible-vault {create,edit,view,encrypt,decrypt} file.yml
ansible-vault edit --vault-passworld-file /path/to/pass-file file.yml

# use vault
ansible-playbook file.yml --ask-vault-pass -K
ansible-playbook file.yml --vault-passworld-file /path/to/pass-file -K

# ansible-pull
ansible-pull -U https://url/to/fetch/from
# only pulls if there are any changes in the repo
ansible-pull -o -U https://url/to/fetch/from

# oneline command
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u <username> -i 'ip-address,' --private-key /path/to/file -e 'pub_key=/path/to/file' ansible_become_pass=<password> file.yml


```

<br>
