pipeline {
  agent any
  stages {
    stage('Build x64 Debug"') {
      steps {
        sh '''cd OpenCppCoverageDemo/cmake
chmod 777 build.sh
./build.sh'''
      }
    }
    stage('Perform Unit Tests') {
      steps {
        sh '''cd OpenCppCoverageDemo/cmake/x64/debug
make TestSource_coverage
cd ../../../../

gcovr -x -r . > OpenCppCoverageDemo/cmake/x64/debug/reports/gcovr_report.xml'''
      }
    }
    stage('Analyze Code') {
      steps {
        sh '''withSonarQubeEnv(\'SonarQubeLocal\') {
              sh \'sonar-scanner -Dsonar.projectVersion=$BRANCH_NAME-$BUILD_NUMBER\'
           }'''
        }
      }
      stage('Quality Gate') {
        steps {
          sh '''timeout(time: 1, unit: \'HOURS\') { // Just in case something goes wrong, pipeline will be killed after a timeout
              def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
              if (qg.status != \'OK\') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
              }'''
        }
      }
      stage('Package') {
        steps {
          sh 'echo "package my applications"'
        }
      }
    }
  }