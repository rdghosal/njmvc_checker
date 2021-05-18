

class TemplateAdapter:
    """
    Class to format templates based on provided parameters
    """
    @staticmethod
    def get_formatted_strs(template: str, params: list):
        for p in params:
            yield template.format(p)


    