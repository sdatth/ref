resource "digitalocean_droplet" "web1" {
  image = "ubuntu-20-04-x64"
  name = "web1"
  region = "fra1"
  size = "s-1vcpu-1gb"
  private_networking = true
  ssh_keys = [var.ssh_fingerprint]
}
