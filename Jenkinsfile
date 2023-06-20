pipeline {
    environment {
		registry = "sumeetcloudengineer/zappyhire-fast-api"
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
                sh 'docker build -t zappyhire-fast-api-test:latest .'
                sh 'docker run -d --name zappyhire-fast-api-container -p 80:80 zappyhire-fast-api-test'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker tag zappyhire-fast-api-test sumeetcloudengineer/zappyhire-fast-api'
                sh 'docker push sumeetcloudengineer/zappyhire-fast-api'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}