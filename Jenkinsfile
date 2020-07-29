node{
    def registryProjet = 'registry.gitlab.com/gauthiermagne1/jenkins'
    def IMAGE = "${registryProjet}:version-${env.BUILD_ID}"

    stage('Clone'){
        git 'https://github.com/GauthierMagne/runDocker.git'
    }
    
    def img = stage('Build') {
        docker.build("$IMAGE", '.')
    }
    
    stage("Run") {
        img.withRun("--name run-$BUILD_ID -p 4000:4000"){
        sh 'ps'
        }
    }
}
