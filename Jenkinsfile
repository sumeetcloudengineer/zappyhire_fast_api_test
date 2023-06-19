pipeline {
    environment {
		registry = "sumeetcloudengineer/zappyhire"
		registryCredentials = 'docker-credentials'
	}
    agent any

    stages {
        stage('Cloning the GIT Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sumeetcloudengineer/zappyhire_fast_api_test.git'
            }
        }
        stage('Setup Application') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {                
                sh 'sudo docker build -t zappyhire-fast-api-test:latest .'
                sh 'sudo docker run -d --name zappyhire-fast-api-container -p 80:80 zappyhire-fast-api-test'
            }
        }
    }
}