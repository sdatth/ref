# Nix

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

# apply new configuration changes  
sudo nixos-rebuild switch --flake '.#zeta'

# upgrade nix packages
sudo nix flake update
sudo nixos-rebuild switch --upgrade --flake '.#zeta'

```
