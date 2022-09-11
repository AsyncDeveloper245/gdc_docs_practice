from genericpath import exists
from turtle import title
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader,PackageLoader
import os
from datetime import datetime
import logging
import http
import jinja2
from ruamel.yaml import YAML


rootdir = './content'
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         #print(dirs)
#         if file.endswith('.md'):
#             #print(f" {subdir:10} {file:10}")
#             #print(os.path.join(subdir, file))
#             with open(os.path.join(subdir, file)) as markdown_file:
#                 file_name = file.split('.')[0]
#                 parsed_file= markdown(
#                     markdown_file.read(),
#                     extras=['fenced-code-blocks', 'code-friendly','metadata'])

#             #select pages based on the page tield in the markdown file
#             if parsed_file.metadata:
#                 # print(parsed_file.metadata)
#                 #print(parsed_file.metadata['page_title'])
#                 if 'page_title' in parsed_file.metadata:
#                     # print(parsed_file.metadata['page_title'])
#                     page_title = parsed_file.metadata['page_title']
#                     print(page_title)

#                     #write output files for different pages based on the page title in the markdown file
#                     if page_title == 'Home':
#                         #print(file.split('.')[0])
#                         with open('output/'+file_name + '.html','w') as output_file:
#                             output_file.write(

#                             template.render(
#                                     content = parsed_file,
#                                     page_title = parsed_file.metadata['page_title'],
#                                     description = parsed_file.metadata['page_description'],
#                             )
#                             )

#                     elif page_title == 'Encyclopedia':
#                         with open('output/'+file_name + '.html','w') as output_file:
#                             output_file.write(
#                                 template.render(
#                                     content = parsed_file,
#                                 ))




            
# def handle_md_to_html(directory):
#     for folders in os.listdir(directory):
#         if os.path.isdir(os.path.join(directory,folders)):
#             for root,dirs,files in os.walk(os.path.join(directory,folders)):
#                 for file in files:
#                     if 'Users_Guide' in root.split('/'):
#                         if file.endswith('.md'):
#                             print(os.path.join(root,file))
#                         #check if the file is in the Users_Guide directory
#                             with open(os.path.join(root,file),'r') as md_file:
#                                 md_file_content = md_file.read()
#                                 parsed = markdown(md_file_content,extras=['metadata'])
                                
#                                 env = Environment(loader=PackageLoader('script', 'templates'))

#                                 base_template = env.get_template('base.html')
#                                 base_metadata = parsed.metadata

#                                 if 'page_title' in parsed.metadata:
#                                     # print(parsed_file.metadata['page_title'])
#                                     page_title = parsed.metadata['page_title']
#                                     with open('mkdocs.yml') as f:
#                                        yaml = YAML(typ='safe')
#                                        mkdocs_config = yaml.load(f)
#                                     base_html = base_template.render(page = base_metadata,
#                                                                     page_title = parsed.metadata['page_title'],
#                                                                     config = mkdocs_config,
#                                                                     nav = mkdocs_config['pages'],
#                                                                     content = parsed
#                                                                     )


#                                     file_name = file.split('.')[0]
                                    
#                                     filename = str('output/'+root+'/'+file_name+'.html').lower()
#                                     #create an html file with the file_name
#                                     html_file = open(filename, 'w')
#                                     html_file.write(base_html)
                        
# handle_md_to_html(rootdir)
# #todo Write conditional blocks in the base.html template to display the content of the different pages

# #todo Write a function to handle the creation of the html files for the different pages
# #todo Include page_title to all markdown files


# for root,dirs,files in os.listdir(rootdir):
#     for file in files:
#         if "Users_Guide" in root.split('/'):
#             if file.endswith('.md'):
#                 print(file)

#         else:
#             if file.endswith('.md'):
#                 print(f" Home---- {file}")

# for folders in os.listdir(rootdir):
#     if os.path.isdir(os.path.join(rootdir,folders)):
#         for root,dirs,files in os.walk(os.path.join(rootdir,folders)):
#             for file in files:
#                 if 'Users_Guide' in root.split('/'):
#                     if file.endswith('.md'):
#                         print(file)
            #     else:
            #         print(file)
            # # for file in files:
            #     print(dirs)
            #     if 'Users_Guide' in dirs and file.endswith('.md'):
            #             print(f" {root} {file}")
            #     # else:
                #     if file.endswith('.md'):
                #         print(f"{file}")


all_pages = []
with open('mkdocs.yml','r') as yaml_file:
    yaml = YAML(typ='safe')
    mkdocs_config = yaml.load(yaml_file)
    for page in mkdocs_config['pages']:
        all_pages.append(page)


for page in all_pages:
    for k,v in page.items():
        if isinstance(v,list):
              for item in v:
                if isinstance(item,dict):
                     for k,v in item.items():
                        v = v.split('/')[:-1]
                        #merge list elements into paths
                        v = '/'.join(v)
                        os.makedirs(os.path.join('dist',v),exist_ok=True)
                        

        else:
            #print(v)
            continue