
node() {

        checkout scm

        stage("Build x64 Debug") {
		sh 'chmod u+x ./build.sh'
		sh './build.sh'
        }
        stage("Perform Unit Tests"){
                dir('OpenCppCoverageDemo/cmake/x64/debug'){
                   sh 'make TestSource_coverage'
                }
                
                sh 'gcovr -x -r . > OpenCppCoverageDemo/cmake/x64/debug/reports/gcovr_report.xml'

        }
        stage("Analyze Code"){
           withSonarQubeEnv('SonarQubeLocal') {
              sh 'sonar-scanner -Dsonar.projectVersion=$BRANCH_NAME-$BUILD_NUMBER' 
           }
        }
        stage("Quality Gate"){
              timeout(time: 1, unit: 'HOURS') { // Just in case something goes wrong, pipeline will be killed after a timeout
              def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
              if (qg.status != 'OK') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
              }
        }
        stage("Package"){
             echo "package my applications"
        }


}
