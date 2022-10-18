# Nix

### NixOS
```bash
# list generations
sudo nix-env --list-generations --profile /nix/var/nix/profiles/system

# switch generation
sudo nix-env --profile /nix/var/nix/profiles/system --switch-generation 204

# delete generation
sudo nix-env --profile /nix/var/nix/profiles/system --delete-generations 1002 1001

# garbage collect
nix-collect-garbage
sudo nix-collect-garbage 

# delete old generations
nix-collect-garbage -d

# apply new configuration changes  
sudo nixos-rebuild switch --flake '.#zeta'

# upgrade nix packages
sudo nix flake update
sudo nixos-rebuild switch --upgrade --flake '.#zeta'

```

### Nix Package manager
```bash
# Searching for packages	
nix search nixpkgs packagename

# Installing a package	
nix-env -iA nixpkgs.packagename

# List installed packages	
nix-env -q

# Uninstall packages	
nix-env -e packagename

# Upgrade packages	
nix-env -u `*`

# Listing current channels	
nix-channel --list

# Adding other channels	
nix-channel --add https://some.channel/url my-alias

# Remove a channel	
nix-channel --remove channel-alias

# Updating a channel	
nix-channel --update channel-alias

# Updating all channels	
nix-channel --update

# List generations
nix-env --list-generations

# switch generation
nix-env --switch-generation 204

# delete generation
nix-env --delete-generations 1002 1001

# garbage collect
nix-collect-garbage
sudo nix-collect-garbage 

# delete old generations
nix-collect-garbage -d

```
