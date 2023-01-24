pipeline{
    
    agent any

    options {
        timestamps() 
    }

    environment {
       AWS_ACCOUNT_ID= "644435390668"
       AWS_DEFAULT_REGION="eu-west-3"
       IMAGE_REPO_NAME= "roei"
       IMAGE_TAG= "latest"
    }

    stages{
        stage("Init"){
            steps{
                deleteDir()
                checkout scm

            }
        }   

        stage("Build APP") {
            steps {
                script{
                    sh "docker build -t ${IMAGE_REPO_NAME} ."
                }
            }
        }

        stage("Test App container") {
               steps {
                   sh """
                    docker compose up -d --build
                    sleep 10
                    curl 52.47.195.52:80
                """
           }
        }

        // stage("E2E Test") {
        //     steps{
        //         sh """
        //         chmod 777 test/test.sh
        //         ./test/test.sh
        //         docker-compose down 
        //         """
        //     }
        // }

        stage("Push to ECR") {
            steps {
                script{
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: "aws-jenkins",
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]]) {
                        sh "aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-3.amazonaws.com"
                        sh 'docker tag ${IMAGE_REPO_NAME}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:latest'
                        sh 'docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:latest'
                    }
                }
            }
        }

        //  stage("Deploy App") {
        //     steps {   
        //         //prod2 
        //         sh """
        //         scp db/setup.sql ubuntu@13.38.17.63:/home/ubuntu/myapp/db
        //         scp app.py ubuntu@13.38.17.63:/home/ubuntu/myapp
        //         scp deploy.sh ubuntu@13.38.17.63:/home/ubuntu/myapp
        //         scp docker-compose.yml ubuntu@13.38.17.63:/home/ubuntu/myapp
        //         scp Dockerfile  ubuntu@13.38.17.63:/home/ubuntu/myapp
        //         scp nginx/nginx.conf ubuntu@13.38.17.63:/home/ubuntu/myapp/nginx
        //         scp templates/index.html ubuntu@13.38.17.63:/home/ubuntu/myapp/templates
        //         scp requirements.txt ubuntu@13.38.17.63:/home/ubuntu/myapp
        //         ssh ubuntu@13.38.17.63 /home/ubuntu/myapp/deploy.sh

        //         scp db/setup.sql ubuntu@13.38.14.90:/home/ubuntu/myapp/db
        //         scp app.py ubuntu@13.38.14.90:/home/ubuntu/myapp
        //         scp deploy.sh ubuntu@13.38.14.90:/home/ubuntu/myapp
        //         scp docker-compose.yml ubuntu@13.38.14.90:/home/ubuntu/myapp
        //         scp Dockerfile  ubuntu@13.38.14.90:/home/ubuntu/myapp
        //         scp nginx/nginx.conf ubuntu@13.38.14.90:/home/ubuntu/myapp/nginx
        //         scp templates/index.html ubuntu@13.38.14.90:/home/ubuntu/myapp/templates
        //         scp requirements.txt ubuntu@13.38.14.90:/home/ubuntu/myapp
        //         ssh ubuntu@13.38.14.90 /home/ubuntu/myapp/deploy.sh
        //         """    
        //         //prod1
        //     }
        //  }
    }
}