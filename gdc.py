from markdown2 import markdown
from jinja2 import Environment,PackageLoader
import os
from datetime import datetime
import logging
import http
import jinja2

#setup logging
logging.basicConfig(filename='gdc-parser.log',encoding='utf-8',level=logging.DEBUG)





       
with open('content/gdc.md','r') as file:
    base = markdown(file.read(),extras=['metadata'])


env = Environment(loader=PackageLoader('gdc', 'templates'))

base_template = env.get_template('base.html')
#home_template = env.get_template('homepage.html')


# page_metadata = [PAGES[md].metadata for md in PAGES]
base_metadata = base.metadata

base_html = base_template.render(page = base_metadata)
with open('output/base.html','w') as file:
    file.write(base_html)






#class to handle different pages and parse their markdown
class MarkdownParser:
    """
        This Class Handles Parsing of the markdown documents and converts the docs into Html files.
    """
    def __init__(self,page_name,md_file,directory):
        self.page_name = page_name
        self.page_path = os.path.join('content',md_file)
        self.page_metadata = {}
        self.page_html = ''
        self.page_template = ''
        self.page_output = ''
        self.page_content = ''
        self.md_file = md_file
        self.directory = directory
    
    def get_page_content(self):
        logging.info("Process Started! Getting Page Content...")
        try:
            with open(self.page_path,'r') as file:
                self.page_content = file.read()
        except FileNotFoundError:
            pass

    def parse_page_content(self):
        self.page_metadata = markdown(self.page_content,extras=['metadata'])

    def get_page_template(self):
        try:
            self.page_template = env.get_template(self.page_name+'.html')
        except jinja2.exceptions.TemplateNotFound:
            self.page_template = env.get_template('base.html')

    def render_page_template(self):
        logging.info("Process Started! Rendering Page Template...")
        self.page_html = self.page_template.render(page = self.page_metadata)

    def write_page_output(self):
        logging.info("Process Started! Writing Page Output...")
        self.page_output = os.path.join('output',self.directory,self.page_name+'.html')
        with open(self.page_output,'w') as file:
            file.write(self.page_html)

    # write function to get current page title for html templates
    def get_page_title(self):
        return self.page_metadata.metadata['title']
    
    #function to serve html templates with an http server
    def serve_page(self):
        http.server.test(self.page_output)

    def parse_page(self):
        self.get_page_content()
        self.parse_page_content()
        self.get_page_template()
        self.render_page_template()
        self.write_page_output()

    #function to move through the makdocs.yml file and builds html pages based on the values of the keys.
    def build_pages(self):
        mkdocs_config = os.path.join('mkdocs.yml')
        with open(mkdocs_config,'r') as file:
            mkdocs_config = yaml.load(file)
        for page in mkdocs_config['pages']:
            print(page)
            page_parser = MarkdownParser(page)
            page_parser.parse_page()
            page_parser.serve_page()




#class that receives the markdown file and converts it to html

