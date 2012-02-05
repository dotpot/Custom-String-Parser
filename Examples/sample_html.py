from CustomStringParser import PrintResults, ParsingNode, CustomStringParserCore

__author__ = 'Lukas Salkauskas'

def test():
    string_data = """
    	<..>
	<div class="section-item">
		<div class="section-title">
			title1
		</div> <!-- end section-title -->
		<div class="section-comments">
			15
		</div> <!-- end section-comments -->
	</div> <!--end section-item-->
	<div class="section-item">
		<div class="section-title">
			title2
		</div> <!-- end section-title -->
		<div class="section-comments">
			16
		</div> <!-- end section-comments -->
	</div> <!--end section-item-->
	<div class="section-item">
		<div class="section-title">
				title3
		</div> <!-- end section-title -->
		<div class="section-comments">
			17
		</div> <!-- end section-comments -->
	</div> <!--end section-item-->
        """
    parser = CustomStringParserCore(string_data)
    itemParser = ParsingNode('item', '<div class="section-item">', '</div> <!--end section-item-->')

    titleParser = ParsingNode('title', '<div class="section-title">', '</div> <!-- end section-title -->')
    commentsParser = ParsingNode('comments', '<div class="section-comments">', '</div> <!-- end section-comments -->')
    # note: our item result will have title and comments inside of it, so we can do this:
    itemParser.addParser(titleParser)
    itemParser.addParser(commentsParser)

    parser.addParsingNode(itemParser)

    # call the parse
    parser.parse()

    PrintResults(itemParser.results)

if __name__ == '__main__':
    test()