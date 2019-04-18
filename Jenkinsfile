pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'deploy', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')])
                script {
                    echo 'Build docker images'
                    sh "docker-compose build" 
                    sh 'docker images'
                }
            }
        }
    }
}
