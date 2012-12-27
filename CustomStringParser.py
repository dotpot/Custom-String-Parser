__author__ = 'dotpot'

class ParsingHelper():
    @staticmethod
    def extract_tag(value, start_tag, end_tag):
        """
         Helper method will extract information between two tags.
         f.ex a string = "<a> hello lady <a>"
                start_tag = "hello"
                end_tag = "<a>"
                Result = "lady"
        """
        start_index = value.find(start_tag)
        if start_index != -1:
            # move starting index to the end of the tag.
            start_index += len(start_tag)

            # endIndex will be calculated in the string, starting from start_index
            endIndex = value.find(end_tag, start_index)
            if endIndex != -1:
                # slice string and return a result.
                return value[start_index:endIndex], start_index, endIndex

        return None, -1, -1

class ParsingResult():
    """ This class represents result of the parsing_node and also subResutls if exits """
    def __init__(self, name, value, parsing_node):
        self.name = name
        self.value = value
        self.parsing_node = parsing_node
        self.sub_results = None

    def add_sub_result(self, sub_result):
        """ adds provided sub_result to existing sub_results list """
        if self.sub_results is None:
            self.sub_results = list()

        self.sub_results.append(sub_result)

    def clear_sub_results(self):
        """ clears the sub_results """
        self.sub_results = None

class ParsingNode():
    """ This class represents the parsing node with it's name, start and end tags, subParsers """
    def __init__(self, name, start_tag, end_tag):
        self.name = name
        self.start_tag = start_tag
        self.end_tag = end_tag

        self.parsers = None
        self.results = list()

    def parse(self, content):
        """ Method parses the given content and extracts all possible values """
        if content is not None:
            parsing_result, start_index, end_index = ParsingHelper.extract_tag(content, self.start_tag, self.end_tag)
            self.results = list()

            while parsing_result is not None:
                result = ParsingResult(self.name, parsing_result, self)
                self.results.append(result)

                # if there is sub parsers, parse them as well and add as sub result
                if self.parsers is not None:
                    for sub_parser in self.parsers:
                        sub_results = sub_parser.parse(parsing_result)
                        if sub_results is not None:
                            for res in sub_results:
                                result.add_sub_result(res)

                content = content[end_index:]
                parsing_result, start_index, end_index = ParsingHelper.extract_tag(content, self.start_tag, self.end_tag)

        return self.results

    def add_parser(self, parser):
        """ add sub parser """
        if self.parsers is None:
            self.parsers = list()

        self.parsers.append(parser)

class CustomStringParserCore():
    """ main parser class which holds the content we want to parse and the parsers we're going to use"""
    def __init__(self, content):
        self.content = content
        self.parsers = None

    def add_parser(self, parser):
        """ adds parsing node to existing parsing nodes list """
        if self.parsers is None:
            self.parsers = list()

        # ToDo: Check if parser with same name exists or not ( maybe )
        self.parsers.append(parser)

    def parse(self):
        """ iterates through all the parsers and calls parse method (which aggregates results)"""
        if self.parsers is not None:
            for parser in self.parsers:
                parser.parse(self.content)

# For temporary purposes.
def print_results(resultsList, sep=''):
    """ just prints out tree of results with subresults, provide someParsingNode.results"""
    sep += '\t'
    if resultsList is not None:
        for result in resultsList:
            print result.name + ':\n' + sep + result.value
            sr = result.subResults
            if sr is not None and len(sr) > 0:
                print_results(sr, '\t')

