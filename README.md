# Custom String Parser

You can use this component if you need to parse any information from string value.

> The easiest way to parse data from string in python.

## Overview

**CustomStringParser**, the missing simple string parser for *python developers*.

### Usage


#### Parsing HTML
**Note: for html based parsing you should consider using [xpath](http://www.w3schools.com/xpath/)
**

Imagine you have this kind of content in your `string_data` with this content:
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
We need to parse these items:

* title
* comments count

Code to parse this looks like this:	
	parser = CustomStringParserCore(string_data)
	itemParser = ParsingNode('item', '<div class="section-item">', '</div> <!--end section-item-->')
	
	titleParser = ParsingNode('title', '<div class="section-title">', '</div> <!-- end section title -->')
	commentsParser = ParsingNode('comments', '<div class="section-comments">', '</div> <!-- end section-comments -->')
	# note: our item result will have title and comments inside of it, so we can do this:
	itemParser.addParser(titleParser)
	itemParser.addParser(commentsParser)

	# add main parser to the parsing core
	parser.addParsingNode(itemParser)

	# call the parse
	parser.parse()
	
	<..>
**output (PrintResults(itemParser.results)):**

*item*:
	<div class="section-title">
			title1
		</div> <!-- end section-title -->
		<div class="section-comments">
			15
		</div> <!-- end section-comments -->
	
*title*:
	title1
		
*comments*:
	15
		
*item*:
	<div class="section-title">
			title2
		</div> <!-- end section-title -->
		<div class="section-comments">
			16
		</div> <!-- end section-comments -->
	
*title*:
	title2
		
*comments*:
	16
		
*item*:
	<div class="section-title">
				title3
		</div> <!-- end section-title -->
		<div class="section-comments">
			17
		</div> <!-- end section-comments -->
	
*title*:
	title3
		
*comments*:
	17

### This is very generic, so you can parse practically any structure.
	
	