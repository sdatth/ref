# rsync


<br>

## commands
```bash
# syncing folder src into dest:
rsync -avz ./src /dest
# syncing the content of src into dest:
rsync -avz ./src/ /dest


# Display Options

-q, --quiet
-v, --verbose
    --stats
-h, --human-readable
    --progress
-P                     # same as --partial --progress


# Archive Options

-a, --archive    # archive (-rlptgoD)

-r, --recursive
-l, --links      # copy symlinks as links
-p, --perms      # preserve permissions
-t, --times      # preserve times
-g, --group      # preserve group
-o, --owner      # preserve owner
-D               # same as --devices --specials

--delete         # Delete extra files


# Transfer Options 

-z, --compress
-n, --dry-run
    --partial   # allows resuming of aborted syncs
    --bwlimit=RATE    # limit socket I/O bandwidth


# Skipping Options

-u, --update     # skip files newer on dest
-c, --checksum   # skip based on checksum, not mod-time & size


# Exclude & Include Options

--exclude=PATTERN
--include=PATTERN
--exclude-from=FILE
--include-from=FILE
--files-from=FILE    # read list of filenames from FILE


# In the following example shows how exclude the node_modules and tmp directories:

rsync -a --exclude=node_modules --exclude=tmp /src_directory/ /dst_directory/

# The second option is to use the --exclude-from option and specify the files and directories you want to exclude in a file.

rsync -a --exclude-from='/exclude-file.txt' /src_directory/ /dst_directory/


```

<br>


