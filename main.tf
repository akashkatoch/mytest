terraform {
	backend "remote" {
		organization = akash-testing
		workspaces {
			name = git-actions
		}
	}
}

resource "aws_instance"
"aws_testing" {
	ami = ami-0cff7528ff583bf9a
	instance_type = t2.micro
	availability_zone = us-east-1
}
