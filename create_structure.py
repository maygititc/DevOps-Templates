import os
from pathlib import Path

# Define the directory structure
structure = {
    "DevOps-Templates": {
        "Jenkins": ["Jenkinsfile", "jenkins-pipeline-example.groovy", "README.md"],
        "Terraform": ["main.tf", "variables.tf", "outputs.tf", "terraform.tfvars", "README.md"],
        "Ansible": {
            "playbook.yml": None,
            "inventory": None,
            "roles": {},
            "README.md": None,
        },
        "Kubernetes": ["deployment.yaml", "service.yaml", "ingress.yaml", "README.md"],
        "Helm": {
            "Chart.yaml": None,
            "values.yaml": None,
            "templates": {},
            "README.md": None,
        },
        "CI-CD": ["azure-pipelines.yml", "github-actions.yml", "gitlab-ci.yml", "README.md"],
        "ArgoCD": ["application.yaml", "app-of-apps.yaml", "README.md"],
        "Git": {
            "git-commands-cheatsheet.md": None,
            "git-hooks": {},
            "README.md": None,
        },
        "Azure-DevOps": ["azure-pipelines.yml", "terraform-azure-pipeline.yml", "README.md"],
        "Shell-Script": ["deploy.sh", "backup.sh", "README.md"],
        "PowerShell": ["deploy.ps1", "backup.ps1", "README.md"],
        "README.md": None,
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = Path(base_path) / name
        if isinstance(content, dict):  # It's a directory
            print(f"Creating directory: {path}")
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):  # It's a directory with files
            print(f"Creating directory: {path}")
            os.makedirs(path, exist_ok=True)
            for file in content:
                file_path = path / file
                print(f"Creating file: {file_path}")
                file_path.touch()
        else:  # It's a file
            print(f"Creating file: {path}")
            path.touch()

# Base directory where the structure will be created
base_directory = "DevOps-Templates"

# Create the structure
create_structure(base_directory, structure)

print("Directory structure and files created successfully!")