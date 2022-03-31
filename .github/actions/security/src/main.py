import shutil
import os
from actions_toolkit import core

language = core.get_input('language', required=True)

languages = ['Python', 'JavaScript', 'Kotlin', 'PHP', 'Go', 
              'Shell', 'HCL', 'Swift', 'Typescript', 'C', 
              'Java', 'Vue', 'Ruby', 'Brightscript', 'SCSS', 
              'LookML', 'Groovy', 'CSS', 'HTML', 'PowerShell', 
              'C+', 'C++', 'C#']

dst = '~/.github/workflows/security.yaml'
# dst = core.get_input()

def run(language,src, dst):
    try:    
        for i in languages:
            if i==language:
                os.makedirs('~/.github/workflows/', exist_ok=True)
                src= str('../security_'+i+'.yaml')
                shutil.copy2(src, dst)

    except Exception as e:
        core.error(f'Error {str(e)}')

run