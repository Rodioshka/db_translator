from jinja2 import Environment, FileSystemLoader


class Reader:
    @staticmethod
    def read_file(filename):
        with open(fr'{filename}', 'r', encoding='utf-8') as file:
            return file.read()


class ReadTemplate(Reader):

    def __init__(self, template_path):
        self.template_dir = template_path
        self.template_env = Environment(loader=FileSystemLoader(template_path))

    def get_data_from_template(self, template_file_name: str):
        return self.template_env.get_template(template_file_name)
