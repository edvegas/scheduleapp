pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                echo 'Build docker images'
                sh "docker-compose build" 
                sh 'docker images'
            }
        }
    }
}
