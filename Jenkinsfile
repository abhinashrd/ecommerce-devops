pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "abhinashrd/ecommerce"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/abhinashrd/ecommerce-devops.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                            docker.image("${DOCKER_IMAGE}").push()
                        }
                    }
                }
            }
        }
    }
}

