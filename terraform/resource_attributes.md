# Use resource attributes to prevent complex strings

When using resources in Terraform, you can reference their attributes to pass elements between other resources. 

An example I encounter often is the email of a service account. 

You can use the `google_service_account.default.email` [attribute](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account#email)
instead of the complex string, which would be something like `myserviceaccount@${var.project-id}.gserviceaccount.com`. 

If you're not declaring the service account as part of ther Terraform, you may be able to use the [data resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/service_account#email) instead. 
