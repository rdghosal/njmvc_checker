

class XPathAdapter:
    """
    Class to format templates based on provided parameters
    """
    @staticmethod
    def generate_xpaths(template: str, params: list):
        """Uses list of params to format a provided template"""
        for p in params:
            yield template.format(p)


    