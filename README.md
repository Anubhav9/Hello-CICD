# Hello-CICD

## Overview

Hello-CICD is a demonstration project showcasing Continuous Integration and Continuous Deployment (CI/CD) practices using Python, Docker, and GitHub Actions. The project includes examples of Python scripts, Docker configurations, and CI/CD workflows.

There are 2 major workflows here:

i) Lint and Tag -> This checks for linting in the main app.py and if the linting score is greater than the threshold value, the flow is diverted to generate the build tag. The build tag logic is generating version based on the current Date and Time. If the commit is on branch other than main/master, suffix SNAPSHOT is added to it, otherwise not.

ii) Deploy to EC2 -> As soon as the open PR is merged to main / master branch, the build is generated on the master commit and the same build is then pushed to the EC2 instance which means to production

## Installation

### Prerequisites

- Docker
- Python 3.x

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Anubhav9/Hello-CICD.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd Hello-CICD
   ```
3. Start the docker container
   ```bash
   docker compose up --build -d
   ```


## Contributing

Contributions are welcome! Please raise feature request PR and I'll get it checked.

## License

This project is licensed under the MIT License.


