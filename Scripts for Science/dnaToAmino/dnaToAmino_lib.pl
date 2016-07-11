#!/usr/bin/perl

# Title: Subroutine Library for dnaToAmino.cgi
# Author: Tyler Murphy

use strict;
use warnings;
use CGI qw/:standard/;


sub myform {
    my $j = param('dna');
    return<<FORM;
    <form action="dnaToAmino.cgi" method="post">
    <table border="0" width="40%" style="border-radius: 25px; background-color:#3385ff; color:#ffffff;">
    <tr><td height="10" colspan="2" align="center"></td></tr>
    <tr><td height="10" colspan="2" align="center">Enter the DNA strand you would like to convert to its corresponding amino acid sequence.</td></tr>
    <tr><td height="10" colspan="2" align="center"></td></tr>
    <tr><td align="center">DNA Strand [Input]</td><td><textarea name="dnaIN" rows="8" cols ="75" placeholder="Enter a DNA strand here!"></textarea></td></tr>
    <tr><td colspan="2" align="center"><input type="submit"></td></tr>
    <tr><td height="10" colspan="2" align="center"></td></tr>
    
    </table>
    </form>
FORM
}


sub myAddTitle {
    return<<TITLE;
<!DOCTYPE html>
    <html>
        <head>
            <font size="6">DNA to Amino Acid Conversion Tool</font>
        </head>
    </html>
TITLE
}



sub top_html {
	my $title = shift @_;
	return<<TOP; 
<!DOCTYPE html>
<html>
	<head>
		<title>$title</title>
	</head>
	<body>
TOP
}
1;