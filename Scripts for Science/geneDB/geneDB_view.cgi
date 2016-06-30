#!/usr/bin/perl

# Title: Gene Database - View Script

# Author: Tyler Murphy
# Purpose: This script will connect to the database, form a query, and execute the query.
    # The query will get the appropriate data from the tables, and display it in an html table, 
    # by using a while loop to put one rowset in each row of the table. 


use strict;
use warnings;
use DBI;
require '/home/bif724_161a16/.secret';
require 'tyler_a1_lib.pl';

print "Content-type: text/html\n\n";
# store db password in a var for easy access
my $password = get_passwd();

# retrieve data from db
# get a database handle, using the connection string for your system and use or die in case of errors
my $dbh = DBI->connect("DBI:mysql:host=db-mysql;database=bif724_161a16", "bif724_161a16", $password) or die "problem connecting" . DBI->errstr;

# formulate the query to be run
my $sql = "select * from a1_data order by ?";
my $myURL = param('sort');

# use prepare function to prepare the query and get a statement handle and use or die in case of errors
my $sth = $dbh->prepare($sql) or die "problem with prepare" . DBI->errstr;
# execute the query and use or die in case of errors 
my $success = $sth->execute($myURL) or  die "problem with execute" . DBI->errstr;



print top_html("RE1 Target Gene Data");
print myViewTitle();
print myMenu();
print <<USE;
<!DOCTYPE html>
<html>
    <head>This is the database in its present state!<br>
    Click any of the above buttons to navigate to another page.<br>
    Click some of the column headings to reorder the column in ascending order.<br>
    OR! Click any of the Target Gene IDs to navigate to the respective website.
    </head>
</html>
USE
print <<T_TOP;
    <table border="1" cellspacing="0" width="50%">
    <tr><th><a href="http://zenit.senecac.on.ca/~bif724_161a16/assignment1/tyler_a1_view.cgi?sort=re1_id">Re1 Gene ID</a></th>
        <th><a href="http://zenit.senecac.on.ca/~bif724_161a16/assignment1/tyler_a1_view.cgi?sort=score">Score</a></th>
        <th><a href="http://zenit.senecac.on.ca/~bif724_161a16/assignment1/tyler_a1_view.cgi?sort=gene_id">Target Gene ID</a></th>
        <th>Position</th>
        <th>Strand Direction</th>
        <th>Gene Description</th>
    </tr>
T_TOP
if ($success != 0) {
    
      # loop through resultset if data found
    while (my @row = $sth->fetchrow_array) {
        print "<tr>
        <td>$row[0]</td>
        <td>$row[1]</td>
        <td><a href='http://uswest.ensembl.org/Gene/Summary?db=core;g=$row[2]' target='_blank'>$row[2]</td>
        <td>$row[3]</td>
        <td>$row[4]</td>
        <td>$row[5]</td>
        </tr>";
      
    }
} else {
      # print a message if no data found
    print "<tr colspan='3'><td>no records found</td></tr>";   
}
# release db connection and use or die in case of errors
$dbh->disconnect() or die "problem with disconnect" . DBI->errstr;
print "</table>";
print bottom_html();