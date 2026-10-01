variable "github_repository" {
  description = "GitHub repository allowed to assume the OIDC role."
  type        = string
}

variable "github_branch" {
  description = "GitHub branch allowed to assume the OIDC role."
  type        = string
  default     = "main"
}

variable "github_owner_id" {
  description = "Immutable GitHub owner ID used in the OIDC subject claim."
  type        = number
}

variable "github_repository_id" {
  description = "Immutable GitHub repository ID used in the OIDC subject claim."
  type        = number
}
