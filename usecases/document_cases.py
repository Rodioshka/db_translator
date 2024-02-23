from service.reader import ReadTemplate
from service.writer import writer


class CreateDocumentUseCase:
    @staticmethod
    def execute(template_name: str, template_path: str, file_format: str, file_name: str, data: dict) -> None:
        template = ReadTemplate(template_path=template_path)
        template_data = template.get_data_from_template(f'{template_name}')

        writer.save_data(
            file_name=file_name, file_format=file_format, data=template_data.render(**data), file_folder='results',
        )
