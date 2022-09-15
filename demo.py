
relevant_skills= [ 'power bi', 'bi', 'sql', 'tableau', 'r', 'r programming', 'python',
 'statistics', 'statistical analysis', 'oracle', 'sas', 'alteryx', 'sap', 'vba', 'vba macros', 'macros']


skills_scraped_text = 'algorithms, python, oracle, information technology, bi, sql, java, business objects, mysql, big data'
s_text = 'macros , visualization , bi , data analyst , vba'

skills_scraped_list = s_text.split(' ,')
#print(skills_scraped_list)


def get_refined(list):
    refined_skills_scraped = []
    for skill in skills_scraped_list:
        skill = skill.lstrip()
        if skill in relevant_skills:
            refined_skills_scraped.append(skill)
        else:
            continue
    return refined_skills_scraped

#print(get_refined(skills_scraped_list))
new_text = 'Data Analyst\nFresher\nInternational Backend\nScience\nUK Shift\nPhysics\nProcess Associate\nAnalyst'
new_text = new_text.lower()
new_list = new_text.split('\n')
print(new_list)


def get_text(row_text):
    refined_skills_scraped = []
    row_text = row_text.lower()
    if '_x000d_' in row_text:
        new_list = row_text.split('_x000d_\n')
    else:
        new_list = row_text.split('\n')
    for skill in new_list:
        if skill in relevant_skills:
            refined_skills_scraped.append(skill)
        else:
            continue
    return refined_skills_scraped

text_2 = 'Business Analysis_x000D_\nIT Skills_x000D_\nOracle_x000D_\nTableau_x000D_\nPower BI_x000D_\nProject Management_x000D_\nRequirement Gathering'


print(text_2.lower().split('_x000d_\n'))



list_2 = text_2.split('\n')
#print(list_2)

#Skill Query shows 3 plots
#  1. Technology proportions: such as python, sql, r, sas, sass, matlab, etc (mainly languages & interfaces such as shell)
#  2. Package proportions: such as pandas, matplotlib, numpy etc (so far I don't have much data for packages)
#  3. Operations tool proportions: such as Tableau, Power BI, aws, azure etc

#My projects plots
#  1. Plot for region %age on a map (similar to skill query)
#  2. Plot for visualization tools

#what i want to do with below lists?
# 1. I want to replace all synonyms with one label
# 2. Make diff columns for excel, databases, languages, visualization tools etc..

# Steps
#  1. First I will have to give single label for all synonyms
#  2. Then, use that single label to make columns or create dummy variables
#  3. will have to add a step to get unique skills in every row,because can have same skill 2 times or more

relevant_skills= [ 'power bi', 'sql', 'tableau', 'r', 'r programming', 'python', 'oracle', 'sas', 'alteryx', 'sap', 'vba', 
                  'vba macros', 'macros', 'hive', 'hadoop', 'spss', 'scala', 'sql queries','nosql', 'crm', 'excel','sql server', 
                  'google analytics', 'google studio', 'google data studio', 'adobe analytics', 'advanced excel', 'mysql', 'mongodb', 
                 'snowflake', 'azure', 'aws', 'qlikview', 'pyspark', 'qliksense', 'qlik sense', 'ms sql', 'qucksight', 'amazon quicksight', 'quick sight'
                 'google sheets', 'r language', 'microsoft sql server', 'php', 'oracle database', 'plsql', 'oracle plsql',
                 'data extraction', 'microsoft office excel', 'sas sql', 'azure sql server', 'microsoft azure sql server', 'azure data explorer',
                 'amazon dynamodb', 'dynamodb', 'sas visual analytics', 'postgresql','ibm db2', 'redis', 'sqlite', 'cassandra', 'sap hana', 'java', 'c', 'c++']

# for labelling
# done excel_syn = ['excel', 'advanced excel', 'microsoft excel', 'ms excel', 'vba', 'macros', 'vba macros', 'microsoft office excel', 'pivot table', 'spreadsheet']
# done azure_syn = ['azure', 'azure data explorer']
# done aws_syn   = ['aws', 'qucksight', 'amazon quicksight', 'quick sight']

syn_dict = {
    'ms sql server'   : ['microsoft sql server', 'ms server'],
    'mysql'           : ['mysql server'],
    'ms access'       : ['microsoft access'],
    'azure'           : ['azure data explorer'],
    'oracle'          : ['oracle database'],
    'sap'             : ['sap hana'],
    'amazon dynamodb' : ['dynamodb'],
    'azure sql server': ['microsoft azure sql server', 'microsoft azure sql'],
    'aws'             : ['qucksight', 'amazon quicksight', 'quick sight'],
    'sas'             : ['sas visual analytics'],
    'r'               : ['r programming', 'r language'],
    'spark'           : ['pyspark'],
    'sql'             : ['sql queries', 'sas sql', 'plsql', 'oracle plsql'],
    'excel'           : ['advanced excel', 'microsoft excel', 'ms excel', 'vba', 'macros', 'vba macros', 'microsoft office excel', 'pivot table', 'spreadsheet']

}

# for making columns
#  What columns? 1. Databases popularity 2. programming Languages (separate column for sql) 3.Visualization tool or service 4. Packages if possible (if no data, then drop)
# make a separate def func for each col, to scan all skills in skill list, then add it to the respective column

#TIP - for skills where 2 languages or 2 tools are used, use random func to randomly select one of them

# done spreadsheet_list = ['excel', 'google sheets']
databases_list = ['oracle', 'mysql', 'ms sql server', 'postgresql', 'mongodb', 'ibm db2', 'redis', 'ms access', 'sqlite', 'cassandra', 'hive', 'sap', 'amazon dynamodb', 'nosql']

languages = ['python', 'r', 'sql','spark', 'scala','java', 'c', 'c++']
#keywords = ['bi', 'business intelligence', 'dashboard', 'dashboards', 'report'] #I don't think I need this list


bi_tools_list = ['sas', 'spss', 'power bi', 'tableau', 'qlikview', 'qliksense', 'azure', 'aws', 'google analytics', 'google data studio', 'adobe analytics', 'snowflake', 'hadoop', 'alteryx']

#---------------------------------------------------------------------------------------------------------------
#           Date Engineer data preparation

relevant_skills_de = ['python', 'r', 'sql','java', 'scala', 'tensorflow', 'apache nifi', 'nifi', 'aws', 'azure', 'microsoft azure', 'oracle', 'pyspark',
'rest api', 'rest api development', 'teradata', 'spark', 'presto', 'jenkins', 'ssrs', 'ssis', 't-sql', 'pl/sql', 'oracle pl/sql', 'ms sql server', 'microsoft sql server',
'azure data factory', 'sql server', 'machine learning', 'pytorch', 'scipy', 'linux', 'nosql', 'dynamodb', 'snowflake', 'spark sql', 'redshift', 'amazon redshift', 'bigquery', 'google bigquery', 'big query',
'google big query', 'gcp cloud', 'google cloud', 'gcp', 'power bi', 'tableau', 'qlik sense', 'django', 'kafka', 'apache kafka', 'devops', 'spark analytics', 's3', 'flask', 'pandas', 'aws redshift', 'aws data analytics',
'python development', 'databricks', 'azure databricks', 'logstash', 'kibana', 'data bricks', 'azure data bricks', 'sql dw', 'aws cloud', 'adls2', 'adf', 'azure hdinsights', 'cloudcomposer', 'cloud composer', 'java script', 'js', 'jscript', 'javascript',
'amazonredshift', 'hadoop', 'google dataflow', 'google data flow', 'azure data lake', 'azure synapse', 'sap', 'gcp data engineer', 'azure data engineer', 'bricks', 'azure devops', 'snowflake sql', 'snowflake procedures', 'google cloud platform',
'azure synapse analytics', 'azure sql', 'sql queries', 'snowflake / redshift', 'mysql', 'hive', 'ssas', 'matlab', 'cassandra', 'gcs', 'mongodb', 'sqoop', 'cloudera', 'spss', 'sap pm', 'qliksense', 'qlikview', 'qlik view', 'qlik', 'talend', 'postgresql',
'sql dwh', 'cloud aws', 'alteryx', 'sql/nosql', 'hadoop development', 'cosmos', 'cosmos db', 'azure cosmos', 'azure cosmos db', 'cosmosdb', 'azure cosmosdb', 'jira', 'atlassian suite', 'atlassian', 'google cloud platforms', 'plsql', 'aws glue', 'numpy', 'ms-sql',
'hive sql', 'spark sql', 'rpython', 'kubernetes', 'r programming', 'r language', 'aws lambda', 'lambda', 'oracle dw']


syn_dict_de = {
    'apache'       : ['apache nifi', 'nifi', 'apache kafka', 'kafka', 'hadoop', 'apache hadoop', 'sqoop', 'hadoop architecture', 'hadoop development'],
    'rest api'     : ['rest api development'],
    'aws'          : ['s3', 'redshift', 'amazon redshift','amazonredshift', 'aws redshift', 'aws data analytics', 'aws cloud', 'cloud aws', 'aws glue', 'aws lambda', 'lambda'],
    'azure'        : ['microsoft azure', 'azure data factory', 'data bricks', 'databricks', 'azure data bricks', 'azure databricks', 'adls2', 'adf', 'azure hdinsights', 'azure data lake',
                      'azure synapse', 'azure data engineer', 'bricks', 'devops', 'azure devops', 'azure synapse analytics', 'azure sql', 'cosmos', 'cosmos db', 'azure cosmos', 'azure cosmos db', 'cosmosdb', 'azure cosmosdb'],
    'sql'          : ['sql development','t-sql', 'sql dw', 'sql queries', 'sql scripting', 'sql dwh', 'sql/nosql', 'hive sql', 'spark sql'],
    'ms sql server': ['ssis', 'microsoft sql server', 'ssas', 'ms-sql'],
    'sql server'   : ['ssrs'],
    'oracle'       : ['pl/sql', 'oracle pl/sql', 'plsql', 'oracle dw'],
    'spark'        : ['spark sql', 'spark analytics', 'apache spark'],
    'bigquery'     : ['google bigquery', 'big query','google big query'],
    'gcp'          : ['gcp cloud', 'google cloud', 'cloudcomposer', 'cloud composer', 'google dataflow', 'google data flow', 'gcp data engineer', 'google cloud platform', 'gcs', 'google cloud platforms'],
    'python'       : ['python development', 'rpython'],
    'javascript'   : ['java script', 'js', 'jscript'],
    'snowflake'    : ['snowflake sql', 'snowflake procedures', 'snowflake / redshift'],
    'sap'          : ['sap pm'],
    'qlikview'     : ['qlik sense', 'qliksense', 'qlikview', 'qlik view', 'qlik'],
    'atlassian'    : ['jira', 'atlassian suite'],
    'r'            : ['r programming', 'r language']

}

#programming language
list_1 = ['python', 'java', 'scala', 'r', 'sql', 'linux', 'javascript', 'matlab']

#databases
list_2 = ['oracle', 'spark', 'presto', 'ms sql server', 'sql server', 'nosql', 'dynamodb', 'sap', 'mysql', 'hive', 'cassandra', 'mongodb', 'postgresql', 'kubernetes']

#programming libraries/packages
list_3 = ['tensorflow', 'pyspark', 'pytorch', 'scipy', 'flask', 'pandas', 'numpy']

#any new tools for data engineering
list_4 = ['apache', 'aws', 'azure', 'teradata', 'rest api','jenkins', 'snowflake', 'bigquery', 'gcp', 'power bi', 'tableau', 'qlikview', 'django',
'logstash', 'kibana', 'spss', 'cloudera', 'talend', 'alteryx', 'atlassian']

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                       Data Science Data Preparation

relevant_skills_ds = ['deep learning', 'dl', 'dl models','deep learning models', 'machine learning', 'ml', 'ml models', 'machine learning models']

syn_dict_ds = {
    'DL': ['deep learning', 'dl', 'dl models', 'deep learning models'],
    'ML': ['machine learning', 'ml', 'ml models', 'machine learning models'],
}

#programming language
list_01 = []

#packages and model libraries
list_02 = []


list_03 = []
list_04 = []

