pipeline {
    environment {
        registry = "sumeetcloudengineer/python-fast-api"
		registryCredentials = 'docker-credentials'
    }
    agent any

    triggers { pollSCM '* * * * *' }

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
                sh 'docker build -t python-fast-api:latest .'
                sh 'docker run -p 80:80 --name python-fast-api-container -d python-fast-api:latest'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker tag python-fast-api sumeetcloudengineer/python-fast-api'
                sh 'docker push sumeetcloudengineer/python-fast-api'
            }
        } 
    }
    post { 
        always { 
            cleanWs()
        }
    }
}