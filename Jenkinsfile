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
                    sh "docker build -f Dockerfile.app -t ${IMAGE_REPO_NAME} ."
                }
            }
        }

        stage("Test App container") {
               steps {
                   sh """
                    docker-compose build --no-cache
                    docker-compose up -d 
                    sleep 10
                    curl 15.236.40.171:80
                """
           }
        }

        stage("E2E Test") {
            steps{
                sh """
                chmod 777 test/test.sh
                ./test/test.sh
                cat score.txt
                docker-compose down -v
                """
            }
        }

        stage("Tagging commit and tags"){
            when {
                branch 'main'
            }
            steps{
                script{
                    message = sh(script: "git log -1 --pretty=%B ${env.GIT_COMMIT}", returnStdout: true).trim()
                    if(message.contains("version")){
                        withCredentials([gitUsernamePassword(credentialsId: "94c3e575-d774-4321-8b7b-7f3544ee446e", gitToolName: 'Default')]){
                            Ver_Calc=sh (script: "bash tag_calc.sh ",returnStdout: true).trim()
                            echo "${Ver_Calc}"
                            sh  """
                                git tag --list
                                git switch main
                                git fetch origin --tags
                                git tag ${Ver_Calc}
                                git push origin ${Ver_Calc}
                                git fetch
                                """
                        }
                    }
                }
            }
        }

        // stage("Push to ECR") {
        //     steps {
        //         script{
        //             withCredentials([[
        //                 $class: 'AmazonWebServicesCredentialsBinding',
        //                 credentialsId: "aws-jenkins",
        //                 accessKeyVariable: 'AWS_ACCESS_KEY_ID',
        //                 secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        //             ]]) {
        //                 sh "aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-3.amazonaws.com"
        //                 sh 'docker tag ${IMAGE_REPO_NAME}:\${Ver_Calc} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:\${Ver_Calc}'
        //                 sh 'docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:\${Ver_Calc}'
        //             }
        //         }
        //     }
        // }


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