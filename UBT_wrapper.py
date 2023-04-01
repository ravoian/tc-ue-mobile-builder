#!/usr/local/bin/python3
# See bottom of file for command examples

# System Modules
import os
import sys
import argparse
import socket
import time

# Use simple std logging 
class log:
    scriptName = os.path.basename(sys.argv[0])
    def info(msg):
        print(f'{log.scriptName}: {msg}', file=sys.stdout)
    def error(msg):
        print(f'{log.scriptName}: {msg}', file=sys.stderr)

def _ParseArguments() -> (bool, argparse.Namespace):
    # Generate our parser
    parser = argparse.ArgumentParser()
    # Service configuration
    parser.add_argument('--port', dest="serverPort", required=True, action='store', help='What file share to use')
    # Parse what we got
    parsedArguments = parser.parse_args()
    return (True, parsedArguments)

def _EntryPointAsScript():
    '''
    # Parse the arguments
    operationSuccess, parsedArguments = _ParseArguments()
    if not operationSuccess:
        log.error('Failed to parse command line arguments')
        return -1
    '''

    # Run the command for UBT
    log.info('Starting server')
    os.system('setx JAVA_HOME "C:\Program Files\Android\Android Studio\jbr"')
    finalCommand = '"C:\\Program Files\\Epic Games\\UE_5.1\\Engine\\Build\\BatchFiles\\RunUAT.bat" BuildCookRun ^\
    -project="C:\\Users\\EVO\\Documents\\Unreal Projects\\MBuild\\MBuild.uproject" ^\
    -platform=Android -targetplatform=Android -clientconfig=Development -cookflavor=ASTC ^\
    -verbose -compressed -utf8output -prereqs -nop4 -build -cook -stage -pak -package -archive ^\
    -UbtArgs=""'
    print(finalCommand)
    os.system(f'cmd /k "{finalCommand}"')

# Since we are running as a script; go ahead and run the entry point
if __name__ == '__main__':
    if sys.version_info.major < 3:
        log.error(f'Script requires Python3') 
    exitCode = _EntryPointAsScript()
    
# Example usage
# python3 UBT_wrapper.py 