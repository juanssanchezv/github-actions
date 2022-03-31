from actions_toolkit import core

language = core.get_input('language', required=True)
core.set_output('output_key', 'output_val')

languages = ['Python', 'JavaScript', 'Kotlin', 'PHP', 'Go', 
              'Shell', 'HCL', 'Swift', 'Typescript', 'C', 
              'Java', 'Vue', 'Ruby', 'Brightscript', 'SCSS', 
              'LookML', 'Groovy', 'CSS', 'HTML', 'PowerShell', 
              'C+', 'C++', 'C#']
def run(language):
    try:    
        for i in languages:
            if i==language:
                # select correct security_<language>.yaml file
                something = ''
    except Exception as e:
        core.error(f'Error {str(e)}')
    return something
run