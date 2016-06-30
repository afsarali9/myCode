#!/usr/bin/perl

# Title: Gene Database - Subroutine Library

# Author: Tyler Murphy
# Purpose: This program holds all subroutines used for programs the gene database add/view/upload scripts

use strict;
use warnings;
use CGI qw/:standard/;
require '../week3/webLib.pl';

# prints form for ?add.cgi and accepts param variables
sub myform {
    my $j = param('re1');
    my $k = param ('score');
    my $l = param ('targetGene');
    my $m = param ('position');
    my $strand = param ('strand');
        my $pos = $strand eq '+'?"checked":"";
        my $neg = $strand eq '-'?"checked":"";
    return<<FORM;
    <form action="tyler_a1_add.cgi" method="post">
    <table border="0" width="40%" style="border-radius: 25px; background-color:#009999; color:#ffffff;">
    <tr><td height="10" colspan="2" align="center"></td></tr>
		<tr><td align="center">Re1 ID:</td><td><input type="text" name="re1" value="$j"></td></tr>
		<tr><td align="center">Score:</td><td><input type="text" name="score" value = "$k"></td></tr>
        <tr><td align="center">Target Gene:</td><td><input type="text" name="targetGene" value="$l"></td></tr>
		<tr><td align="center">Position (Relative to Target Gene):</td><td><input type="text" name="position" value = "$m"></td></tr>
        <tr><td align="center">Strand:</td><td>
            Positive Strand:<input type=radio name="strand" value="+" $pos><br>
            Negative Strand:<input type=radio name="strand" value="-" $neg>
        </td></tr>
        <tr><td align="center">Gene Description:</td><td><textarea name="geneDescription" placeholder="Describe the gene..."></textarea></td></tr>
        <tr><td colspan="2" align="center"><input type="submit"></td></tr>
        <tr><td height="10" colspan="2" align="center"></td></tr>
        <tr><td height="10" colspan="2" align="center">With this form you are able to enter values into the appropriate fields in order to store them in the database. All fields except for description are required. Navigate to another page with the menu bar. </td></tr>
		</table>
        </form>
FORM
}


# This 
sub myUploadForm {
    return<<FORM;
    <form action="tyler_a1_upload.cgi" method="post" enctype="multipart/form-data">
    <table border="0" width="40%" style="border-radius: 25px; background-color:#009999; color:#ffffff;">
    <tr><td height="10" colspan="2" align="center"></td></tr>
    <tr><td colspan="2" align="center">File to be uploaded:<input type="file" name="filename"></td></tr>
    <tr><td colspan="2" align="center"><input type="submit"><input type="reset"></td></tr>
    <tr><td height="10" colspan="2" align="center"></td></tr>
    <tr><td height="10" colspan="2" align="center">Upload a file to be validated and stored in the gene database. Only .csv files are accepted. Use the menu bar to redirect to the database or data entry form.</td></tr>
	</table>
    </form>
    
FORM
}


sub myMenu {
    return<<TOP;
<!DOCTYPE html>
<html>
    <head>
        <style>
        ul {padding: 10;}

        ul li {display: inline;}

        ul li a {
        background-color: #009999;
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 4px 4px 0 0;
        }

        ul li a:hover {background-color: #c2c2f0;}
        </style>
    </head>
<body>

<ul id="menu">
  <li><a href="/~bif724_161a16/assignment1/tyler_a1_add.cgi">Add a Record</a></li>
  <li><a href="/~bif724_161a16/assignment1/tyler_a1_view.cgi">View All Records</a></li>
  <li><a href="/~bif724_161a16/assignment1/tyler_a1_upload.cgi">Upload a File</a></li>
</ul>  

</body>

</html>
TOP
}

sub myAddTitle {
    return<<TITLE;
<!DOCTYPE html>
    <html>
        <head>
            <font size="6">Re1 Target Gene Entry Form</font>
        </head>
    </html>
TITLE
}

sub myViewTitle {
    return<<TITLE;
<!DOCTYPE html>
<html>
    <head>
        <font size="6">Re1 Target Gene Database Entries</font>
    </head>
</html>
TITLE
}

sub myUploadTitle {
    return<<TITLE;
<!DOCTYPE html>
<html>
    <head>
        <font size="6">Import a File</font>
    </head>
</html>
TITLE
}


sub validate{
        my $new_re1 = shift;
        #DOES SOMETHING
        
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


sub bottom_html {
		return<<BOTTOM;
	</body>
</html>	
BOTTOM
} 
1;