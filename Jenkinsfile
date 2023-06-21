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
                sh 'docker build -t zappyhire-project:latest .'
                sh 'docker run -p 80:80 --name zappyhire-container -d zappyhire-project:latest'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker tag zappyhire-project sumeetcloudengineer/zappyhire-docker-image'
                sh 'docker push sumeetcloudengineer/zappyhire-docker-image'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}