terraform {
	backend "remote" {
		organization = akash-testing
		workspaces {
			name = git-actions
		}
	}
}

provider "aws" {
    region = "us-east-1"
    access_key = "AKIAYFV75SZQZ5FR5UVM"
    secret_key =  "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"
}

resource "aws_instance"
"aws_testing" {
	ami = ami-0cff7528ff583bf9a
	instance_type = t2.micro
	availability_zone = us-east-1
}
