# escMsg_StreamlabsParameter

A message-sanitizing parameter for streamlabs chatbot

## Requirements

You need python scripting set up for Streamlabs Chatbot.  This means you must
have Python 2.7.13 installed.  There are tutorials available online for
installing Python and configuring Streamlabs Chatbot to use it.

## Installation

You can download the .ZIP file for this script from the repository page at
https://github.com/madelsberger/escMsg_StreamlabsParameter

(Near the top right of the page, click the **Clone or Download** button; in the
pop-up, click **Download ZIP**.)

Then on the Scripts tab in Streamlabs Chatbot, click the import button (an
"arrow-pointing-into-a-box" icon near the upper right of the screen) and select
the downloaded zip file.

The script list should now include *escMsg*; check the **Enabled** box for this
script, and it will be ready to use in commands.

## Usage

This parameter is useful when you want to use the $msg value in a context
where the raw value might not be "safe".  For example, if you want to use the
$msg value in the conditional expression of the $if parameter
(https://github.com/madelsberger/if_StreamlabsParameter) you might try 
something like

    $if("$msg" == "test", "success", "failure")

This is supposed to respond "success" if the $msg is "test", and "failure" if
$msg is anything else; but if $msg contains a ", then the above expression
will not parse correctly.  For example, if $msg has a value like

    "now" what?

then, with $msg expanded, $if sees an expression of

    ""now" what?" == "test"

and this expression will not parse correctly, so you will get an unexpected
result.

So instead you can use

    $if("$escMsg" == "test", "success", "failure")

This will apply the default escape rule - which replaces " with \", among
other tings - to the $msg value, so in the above example the expanded
expression becomes

    "\"now\" what?" == "test"

which is parsed correctly and returns "failure", as expected.

You can apply other escape rules to make the $msg value "safe" for other
contexts, such as embedding in a URL or an HTML page.

Once you import this script, you can use the $escMsg parameter in your
commands.  The parameter syntax is

    $escMsg[(<escape-type>)]

where <escape-type>, if provided, indicates what type of escaping should be
applied to the message.

Examples:

    $escMsg

returns the $msg value modified so it can be embedded in a Python expression
(as is done by the $if parameter).  It does this by placing \ before characters
that could otherwise cause problems, such as ", ', and \ itself.

    $escMsg(html)

returns the $msg value modified for use in an HTML page.  (This is done by
replacing certain characters, such as &lt;, with quivalent HTML entities, such
as &amp;lt;.)

    $escMsg(url)

URL-encodes $msg and returns the result
