from enum import Enum
import pyparsing

class TemplateComponentType(Enum):
    RawText = 0
    Variable = 1
    Subtemplate = 2
    OrExpression = 3


class TemplateComponent:
    # Type, args, isOptional
    # Raw text & Variable: args is just the string
    # Subtemplate: first arg is the name, rest are the vars passed in
    # OrExpression: args are all the other TemplateComponents

    def __init__(self, type: TemplateComponentType, optional: bool, args):
        self.type = type
        self.optional = optional
        self.args = args

class Template:
    def __init__(self, components: list[TemplateComponent]):
        self.__components = components
        self.__expression = self.__convert_to_pyparse()
    
    def __convert_to_pyparse(self):
        '''todo'''
        

    def can_parse(self, input: str) -> bool:
        try:
            self.__expression.parse(input)
            return True
        except:
            return False
        
    def parse(self, input: str) -> list[str]:
        return self.__expression.parse(input)
        
