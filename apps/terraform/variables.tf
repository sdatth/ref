variable "do_token" {
  type        = string
  description = "Your DigitalOcean API token"
  default     = "access-token-here"
}

variable "ssh_fingerprint" {
  type        = string
  description = "Your SSH key fingerprint"
  default     = "ssh-finger-print-here"
}

variable "pub_key" {
  type        = string
  description = "The path to your public SSH key"
  default     = "/path/to/pub/key"
}

variable "pvt_key" {
  type        = string
  description = "The path to your private SSH key"
  default     = "/path/to/privatey/key"
}

