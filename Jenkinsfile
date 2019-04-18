pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            withCredentials([usernamePassword(credentialsId: 'deploy', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')])
            steps {
                echo 'Build docker images'
                sh "docker-compose build" 
                sh 'docker images'
            }
        }
    }
}
