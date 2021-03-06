<h1>Custom String Parser</h1>

<p>You can use this component if you need to parse any information from any string value which has some <a href="http://en.wikipedia.org/wiki/Syntax_(logic)">syntax logics.</a></p>

<blockquote><p>The easiest way to parse data from string in python.</p></blockquote>

<h2>Overview</h2>

<p><strong>CustomStringParser</strong>, the missing simple string parser for <em>python developers</em>.</p>

<h3>Usage</h3>

<h4>Parsing HTML</h4>

<p><strong>Note: for html based parsing you should consider using <a href="http://www.w3schools.com/xpath/">xpath</a>
</strong></p>

<p>Imagine you have this kind of content in your <code>string_data</code> with this content:</p>

<pre><code>&lt;div class="section-item"&gt;
    &lt;div class="section-title"&gt;
        title1
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        15
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
&lt;/div&gt; &lt;!--end section-item--&gt;
&lt;div class="section-item"&gt;
    &lt;div class="section-title"&gt;
        title2
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        16
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
&lt;/div&gt; &lt;!--end section-item--&gt;
&lt;div class="section-item"&gt;
    &lt;div class="section-title"&gt;
            title3
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        17
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
&lt;/div&gt; &lt;!--end section-item--&gt;
</code></pre>

<p>We need to parse these items:</p>

<ul>
<li>title</li>
<li>comments count</li>
</ul>


<p>Code to parse this looks like this:</p>

<pre><code>parser = CustomStringParserCore(string_data)
item_parser = ParsingNode('item', '&lt;div class="section-item"&gt;', '&lt;/div&gt; &lt;!--end section-item--&gt;')

title_parser = ParsingNode('title', '&lt;div class="section-title"&gt;', '&lt;/div&gt; &lt;!-- end section title --&gt;')
comments_parser = ParsingNode('comments', '&lt;div class="section-comments"&gt;', '&lt;/div&gt; &lt;!-- end section-comments --&gt;')
# note: our item result will have title and comments inside of it, so we can do this:
item_parser.add_parser(title_parser)
item_parser.add_parser(comments_parser)

# add main parser to the parsing core
parser.add_parser(item_parser)

# call the parse
parser.parse()

&lt;..&gt;
</code></pre>

<p><strong>output (print_results(item_parser.results)):</strong></p>

<p><em>item</em>:</p>

<pre><code>&lt;div class="section-title"&gt;
        title1
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        15
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
</code></pre>

<p><em>title</em>:</p>

<pre><code>title1
</code></pre>

<p><em>comments</em>:</p>

<pre><code>15
</code></pre>

<p><em>item</em>:</p>

<pre><code>&lt;div class="section-title"&gt;
        title2
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        16
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
</code></pre>

<p><em>title</em>:</p>

<pre><code>title2
</code></pre>

<p><em>comments</em>:</p>

<pre><code>16
</code></pre>

<p><em>item</em>:</p>

<pre><code>&lt;div class="section-title"&gt;
            title3
    &lt;/div&gt; &lt;!-- end section-title --&gt;
    &lt;div class="section-comments"&gt;
        17
    &lt;/div&gt; &lt;!-- end section-comments --&gt;
</code></pre>

<p><em>title</em>:</p>

<pre><code>title3
</code></pre>

<p><em>comments</em>:</p>

<pre><code>17
</code></pre>

<h4>This is very generic, so you can parse practically any structure.</h4>

<h3>Unit tests</h3>
This library suppose to be fully unit tested. So if you want to participate keep that in mind.

<h3>Feature ideas ( not yet implemented )</h3>
* Regex based parsers possibility.
* Grouped regex based parsers possibility.
* XPath based parsers possibility.
* Filtering out results by parser name.
