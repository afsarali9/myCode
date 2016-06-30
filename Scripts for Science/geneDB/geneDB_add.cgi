#!/usr/bin/perl

# Title: Gene Database - Add Script

# Author: Tyler Murphy
# Purpose: This will be a self-referent cgi/perl program that will both generate the data entry
        # form and process/validate the data from the form. It will check if the re1 ID already
        # exists in the database, and if not will add it.

use strict;
use warnings;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;
use DBI;
require '/home/bif724_161a16/.secret';
require 'tyler_a1_lib.pl';


my $password = get_passwd();

#Validation of parameters
if (param()) {
    # form must have been submitted, so validate data
    my $re1 = param("re1");
    my $score = param("score");
    my $targetGene = param("targetGene");
    my $position = param("position");
    my $strand = param("strand");
    my $geneDescription = param("geneDescription");
    
    my @errors;
    my %positionHash = (
        "3'" => "0",               
        "5'" => "1",                
        "exon" => "2",               
        "EXON" => "3",                
        "intron" => "4",
        "INTRON" => "5",
        "exon+" => "6",
        "EXON+" => "7",                
        "intron+" => "8",
        "INTRON+" => "9",
        );
    
    
    # Validate re1
    my @re1 = split(/_/, $re1);
	if ($re1[0] !~ /^rat|chicken|opossum|xenopus|human$/i){
		push @errors, "Please enter valid re1 id species name."; 
	} 
	if ($re1[1] !~ /^(42)$/){
		push @errors, "Please enter valid re1 id ensemlb database number."; 
	}
	if ($re1[2] !~ /^([0-9]{1,2}[a-z]|2)$/){
		push @errors, "Please enter valid re1 id version number.";
	}
	if ($re1[3] =~ /^scaffold$/){
		my $a = splice (@re1, 3, 1);
		my $b = splice (@re1, 3, 1);
		splice (@re1, 3, 0, "$a\_$b");
		if ($re1[3] !~ /^scaffold.[0-9]{2,3}$/){
			push @errors, "Please enter valid re1 id region name.";
		}
	} elsif ($re1[3] !~ /^([WXYZ]|[0-9]{1,2})$/){
		push @errors, "Please enter valid re1 id region name.";
	}
	if ($re1[4] !~ /^[0-9]{6,9}$/){
		push @errors, "Please enter valid re1 id region position.";
	}
	if ($re1[5] !~ /^[rf]$/){
		push @errors, "Please enter valid re1 id forward(f) or reverse(r) strand.";	
	}
    
    # Validate Score
    if (($score !~ /^\d+(\.\d{1,4})?$/) || $score < 0.9100 || $score > 1.0000) {
        push @errors, "Please enter a valid score";    
    }
    
    # Validate Target Gene
    if ($targetGene !~ /^ENS([A-Z]{3}G|G)[0-9]{11}$/) {
        push @errors, "Please enter a valid target gene id.";    
    }
    
    # Validate Position
    if (exists $positionHash{$position}){
    } else {
        push @errors, "Please enter valid position."; 
    }
    
    # Validate Strand
    if ($strand !~ /^[\-+]+$/) {
        push @errors, "Please indicate whether the strand is positive or negative.";    
    }
    
    # Gene Description
    if ($geneDescription) {
        if($geneDescription !~ /^[\^\/\\,'"]+$/){
            push @errors, "Invalid characters in gene description.";    
        }
    }
    
    
    
    
        #Check if present in database    
     if (scalar(@errors)==0) {
        # if NO errors are logged, connect to database to check if re1 already exists there. 
        # Verify re1 doesn't already exist in database
        my $dbh = DBI->connect("DBI:mysql:host=db-mysql;database=bif724_161a16", "bif724_161a16", $password) or die "problem connecting" . DBI->errstr;
        # formulate the query to be run
        my $sql = "SELECT re1_id FROM a1_data WHERE re1_id LIKE '$re1'";
        # use prepare function to prepare the query and get a statement handle and use or die in case of errors
        my $sth = $dbh->prepare($sql) or die "problem with prepare" . DBI->errstr;
        # execute the query and use or die in case of errors 
        my $success = $sth->execute() or  die "problem with execute" . DBI->errstr;
        $dbh->disconnect() or die "problem with disconnect" . DBI->errstr;
        # Check if search returned a results. If it did, push to errors and re-print form
        # If Re1 doesnt exist in database, push to database
        if ($success != 0) {
            push @errors, "Re1 ID:$re1 already exists in database. Did not enter into database.";
        }   
    }
    
    
    # Errors array
    if (@errors) {
        print "Content-type: text/html\n\n";
        print top_html("Re1 Target Gene Data");
        print myAddTitle();
        print myMenu();
        foreach (@errors) {
            print "<br>$_";
        }
        print myform();
    } else {
        # if no validation errors, proceed with program
        my $dbh = DBI->connect("DBI:mysql:host=db-mysql;database=bif724_161a16", "bif724_161a16", $password) or die "problem connecting" . DBI->errstr;
        my $sql = "insert into a1_data values (?,?,?,?,?,?)";
        my $sth = $dbh->prepare($sql) or die "problem with prepare" . DBI->errstr;
        my $rows = $sth->execute($re1, $score, $targetGene, $position, $strand, $geneDescription);
        $dbh->disconnect() or die "problem with disconnect" . DBI->errstr;
            if ($rows == 1) {
                    print "Location: tyler_a1_view.cgi\n\n";
            } else {
                    print "Content-type: text/html\n\n";
                    print "couldn't insert data.\n";
            }
         }
} else {
    # form not submitted, so display form
    print "Content-type: text/html\n\n";
    print top_html("Re1 Target Gene Data");
    print myAddTitle();
    print myMenu();
    print myform();
    print bottom_html();
}   

print "</table>";
print bottom_html();
