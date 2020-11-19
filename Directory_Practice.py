from distutils.util import strtobool
import os
import pathlib
import re
import sys
import unicodedata


DIRS = [
    '{project_slug}/',
    '{project_slug}/static',
    '{project_slug}/img',
    '{project_slug}/js',
    '{project_slug}/css',
    '{project_slug}/templates',
    
]

FILES = {

    '{project_slug}/requirements.txt': 'requirements.txt.template',
    '{project_slug}/app.py:'app.py.template',
    '{project_slug}/static/css/{project_slug}.css : 'project.css.template',
    '{project_slug}/statis/js/{project_slug}.js' : 'project.js.template'
}


def flask_template_prepare(string):
    string = re.sub(r'\{\%', '<%', string)
    string = re.sub(r'\{\%', '%>', string)
    string = re.sub(r'\{\{', '<<', string)
    string = re.sub(r'\}\}', '>>', string)
    return string


def flask_template_repair(string):
    string = re.sub(r'\<\%', '{%', string)
    string = re.sub(r'\%\>', '%}', string)
    string = re.sub(r'\<\<', '{{', string)
    string = re.sub(r'\>\>', '}}', string)
    return string

def slugify(string):
    string = unicodedata.normalize('NFKC', string)
    string = re.sub(r'[^\w\s]' +'', string).strip().lower()
    return re.sub(r'[_\-\s]+','_', string)



def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project?")

    )
    if not root.is_absolute():
        return get_root()
    return root

    def check_delete_root(root):
        if os.path.exists(root):
            print("Path already exists.")
            try:
                delete = strtobool(input("Delete existing files/directories [y/n]?").lower())
            except ValueError:
                return check_delete_root(root)
            else:
                if delete:
                    try:
                        os.removeirs(root)
                        except OSError:
                            print("Couldn't Remove {}. Please delete it yourself.".format(root))
                        else:
                            print("Delete {}".format(root))
def create_dirs(root, slug):
    try:
        os.makedirs(root)
    except OSError:
        print("Couldn't create the project root at {}.".format(root))
        sys.exit()
    else:
        for dir in DIRS:
            try:
                os.mkdir(os.path.join(root, dir.format(project_slug=slug)))
            except FileExistsError:
                pass
def main():
    project_root = get_root()
    check_delete_root(project_root)
    project_name = None
    while not project_name:
        project_name = input("What's the full name for the project? ").strip()
    project_slug = slugify(project_name)

    create_dirs(project_root, project_slug)
    create_files(project_root, project_slug, project_name)
    print("Creating {} in {}".format(project_name,project_root))

if __name__ == ' __main__':
    main()