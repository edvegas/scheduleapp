pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                script {
                    echo 'Build docker images'
                    sh "docker-compose build" 
                    sh 'docker images'
                }
            }
        }
    }
}
