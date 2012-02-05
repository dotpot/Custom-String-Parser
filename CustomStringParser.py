__author__ = 'Lukas Salkauskas'

class ParsingHelper():
    @staticmethod
    def extractTagFromString(stringValue, startTag, endTag):
        """
         Helper method will extract information between two tags.
         f.ex a string = "<a> hello lady <a>"
                startTag = "hello"
                endTag = "<a>"
                Result = "lady"
        """
        startIndex = stringValue.find(startTag)
        if startIndex != -1:
            # move starting index to the end of the tag.
            startIndex += len(startTag)

            # endIndex will be calculated in the string, starting from startIndex
            endIndex = stringValue.find(endTag, startIndex)
            if endIndex != -1:
                # slice string and return a result.
                return stringValue[startIndex:endIndex], startIndex, endIndex

        return None, -1, -1

class ParsingResult():
    """ This class represents result of the parsingNode and also subResutls if exits """
    def __init__(self, name, value, parsingNode):
        self.name = name
        self.value = value
        self.parsingNode = parsingNode
        self.subResults = None

    def addSubResult(self, subResult):
        """ adds provided subResult to existing subResults list """
        if self.subResults is None:
            self.subResults = list()

        self.subResults.append(subResult)

    def clearSubResults(self):
        """ clears the subResults """
        self.subResults = None

class ParsingNode():
    """ This class represents the parsing node with it's name, start and end tags, subParsers """
    def __init__(self, name, startTag, endTag):
        self.name = name
        self.startTag = startTag
        self.endTag = endTag

        self.parsers = None
        self.results = list()

    def parse(self, content):
        """ Method parses the given content and extracts all possible values """
        if content is not None:
            parsingResult, stIndex, enIndex = ParsingHelper.extractTagFromString(content, self.startTag, self.endTag)
            self.results = list()

            while parsingResult is not None:
                result = ParsingResult(self.name, parsingResult, self)
                self.results.append(result)

                # if there is sub parsers, parse them as well and add as sub result
                if self.parsers is not None:
                    for subParser in self.parsers:
                        subResults = subParser.parse(parsingResult)
                        if subResults is not None:
                            for res in subResults:
                                result.addSubResult(res)

                content = content[enIndex:]
                parsingResult, stIndex, enIndex = ParsingHelper.extractTagFromString(content, self.startTag, self.endTag)

        return self.results

    def addParser(self, parser):
        """ add sub parser """
        if self.parsers is None:
            self.parsers = list()

        self.parsers.append(parser)

class CustomStringParserCore():
    """ main parser class which holds the content we want to parse and the parsers we're going to use"""
    def __init__(self, content):
        self.content = content
        self.parsers = None

    def addParsingNode(self, parsingNode):
        """ adds parsing node to existing parsing nodes list """
        if self.parsers is None:
            self.parsers = list()

        self.parsers.append(parsingNode)

    def parse(self):
        """ iterates through all the parsers and calls parse method (which aggregates results)"""
        if self.parsers is not None:
            for parser in self.parsers:
                parser.parse(self.content)

# For temporary purposes.
def PrintResults(resultsList, sep=''):
    """ just prints out tree of results with subresults, provide someParsingNode.results"""
    sep += '\t'
    if resultsList is not None:
        for result in resultsList:
            print result.name + ':\n' + sep + result.value
            sr = result.subResults
            if sr is not None and len(sr) > 0:
                PrintResults(sr, '\t')
