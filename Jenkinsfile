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
        stage("INIT"){
            steps{
                deleteDir()
                checkout scm
            }
        }   

        // stage ("AWS login"){
        //     steps{
        //         script{
        //             sh """
        //             apt update
        //             apt install -y awscli
        //             aws configure set aws_access_key_id AKIAZMC2XWDGO6KFC6FA
        //             aws configure set aws_secret_access_key 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
        //             aws configure set default.region eu-west-3
        //             aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
        //             """
        //         }
        //     }
        // }


        // stage("Build Portfolio") {
        //     steps {
        //         sh "docker build -t ${IMAGE_REPO_NAME} ."
        //     }
        // }

        // stage("Test App container") {
        //        steps {
        //            sh """
        //             docker-compose build --no-cache
        //             docker-compose up -d
        //             docker cp ./nginx/nginx.conf   bat_s_advice_main_nginx_1:/etc/nginx/conf.d
        //             docker cp ./templates     bat_s_advice_main_nginx_1:/usr/share/nginx/html
        //             docker cp ./db/setup.sql  bat_s_advice_main_batdb_1:/docker-entrypoint-initdb.d/    
        //             sleep 10
        //             curl 13.36.241.69:80
        //         """
        //    }
        // }

        // stage("E2E Test") {
        //     steps{
        //         sh """
        //         chmod 777 test/test.sh
        //         ./test/test.sh
        //         docker-compose down 
        //         """
        //     }
        // }

        // stage("Push App Image") {
        //     steps {
        //         sh 'docker tag ${IMAGE_REPO_NAME}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:latest'
        //         sh 'docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:latest'
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