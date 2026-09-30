variable "github_repository" {
  description = "GitHub repository allowed to assume the OIDC role."
  type        = string
}

variable "github_branch" {
  description = "GitHub branch allowed to assume the OIDC role."
  type        = string
  default     = "main"
}
