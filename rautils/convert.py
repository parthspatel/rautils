import os


def html2PDF(file_paths=None):
    try:
        if file_paths:
            for path in file_paths:
                _html2PDF(str(os.path.abspath(path)))
        else:
            cwd = os.getcwd()
            _html2PDF(f'{cwd}\\reports')
    except Exception as ex:
        raise ex


def _html2PDF(location):
    if os.path.isdir(location):
        cwd = os.getcwd()
        os.chdir(location)

        for file in os.listdir(location):
            if file.endswith(".html"):
                file = os.path.join(location,
                                    file).split('.html')[0]
                os.chdir(r'''C:\Program Files\wkhtmltopdf\bin''')
                os.system(f'''.\wkhtmltopdf.exe "{file}.html" "{file}.pdf" ''')

        os.chdir(cwd)
    elif os.path.isfile(location):
        cwd = os.getcwd()
        location = os.path.abspath(location)
        path = location.split('.html')[0]

        os.chdir(r'''C:\Program Files\wkhtmltopdf\bin''')
        os.system(f'''.\wkhtmltopdf.exe "{path}.html" "{path}.pdf" ''')

        os.chdir(cwd)
    else:
        raise ValueError(
            'html2PDF: location must be a dir or path')
