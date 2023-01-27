remote_state {
    backend = "s3"

    generate = {
        path = "backend.tf"
        if_exists = "overwrite_terragrunt"
    }

    config = {
        bucket = "terraform-state-niraj"
        key = "us-east-1/${path_relative_to_include()}/terraform.tfvars"
        region = "us-east-1"
        dynamodb_table = "my_lock"
        encrypt = false
        profile = "niraj"

    }
}