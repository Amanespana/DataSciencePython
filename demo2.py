skills_scraped_text = 'algorithms, python, oracle, information technology, bi, sql, java, business objects, mysql, big data, vba macros'
s_text = 'macros , visualization , bi , data analyst , vba'

skills_scraped_list = skills_scraped_text.split(',')

syn_dict = {
    'ms sql server'   : ['microsoft sql server', 'ms server'],
    'mysql'           : ['mysql server'],
    'azure'           : ['azure data explorer'],
    'oracle'          : ['oracle database'],
    'sap'             : ['sap hana'],
    'amazon dynamodb' : ['dynamodb'],
    'azure sql server': ['microsoft azure sql server'],
    'aws'             : ['qucksight', 'amazon quicksight', 'quick sight'],
    'sas'             : ['sas visual analytics'],
    'r'               : ['r programming', 'r language'],
    'spark'           : ['pyspark'],
    'sql'             : ['sql queries', 'sas sql', 'plsql', 'oracle plsql'],
    'excel'           : ['advanced excel', 'microsoft excel', 'ms excel', 'vba', 'macros', 'vba macros', 'microsoft office excel', 'pivot table', 'spreadsheet']

}

def get_dict():
    for skill in skills_scraped_list:
        skill = skill.lstrip()
        if skill in syn_dict:
            print(syn_dict.keys())
        else:
            print('none')

    return None

nl = ['excel', 'python', 'mongodb', 'sql', 'sql']

def get_unique(row_list):
    unique_list = []
    for skill in row_list:
        if skill not in unique_list:
            unique_list.append(skill)
        else:
            continue

    return unique_list

print(get_unique(nl))

def label_for_syn(row_list):

    new_list = []
    for skill in row_list:
        skill = skill.lstrip()
        for label, syn in syn_dict.items():
            if skill in syn:
                l=label
                break
            else:
                l = skill
        new_list.append(l)
            
    return new_list


