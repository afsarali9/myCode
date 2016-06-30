#!/usr/bin/perl

# Title: Gene Database - Upload Script

# Author: Tyler Murphy
# Purpose: This program will be a self-referent cgi program that will produce a form and process the data.
        # The form will allow one to upload a file. The uploaded file and filename will be validated. Each
        # line in file that passes will be uploaded to the database, and any errors with lines will be
        # displayed for the user.


use strict;
use warnings;
use DBI;
use CGI qw/:standard/;
require 'tyler_a1_lib.pl';
require '/home/bif724_161a16/.secret';
print "Content-type: text/html\n\n";
print top_html("Re1 Target Gene Database");
my $password= get_passwd();

# Steps for uploading a file.
# 1. User can enter text into the fields, or click a button to upload a file.
# 2. Selected file is saved into an array, with each array position containing a single line entry.
# 3. Each line in the array must then be saved to their own arrays, being split at the comma.

my @errorsU;

if (param()) {

    # stores uploaded file in variable
    my $filename = param("filename");
    
    if ($filename !~ /^[\w\d_-]+\.csv$/) {
        push @errorsU, "Invalid file name and/or type."
    }
    
    if (scalar(@errorsU)==0) {
        # get a filehandle to the file to be uploaded
        my $upload_fh = upload("filename");
        # file_upload array contains all lines, one line per entry. Ex- $file_upload[0] = line 1
        my @file_upload = <$upload_fh>;
        # split each lines into an array
        
        for (my $i=0; $i<scalar(@file_upload); $i++){            
            my @errorsUp;       
            @_ = split(/,/, $file_upload[$i]);
            my $re1 = $_[0];
            my $score = $_[1];
            my $targetGene = $_[2];
            my $position = $_[3];
            my $strand = $_[4];
            my $geneDescription = $_[5];
            
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
                push @errorsUp, "Error on line: $i"; 
            } 
            if ($re1[1] !~ /^(42)$/){
                push @errorsUp, "Error on line: $i"; 
            }
            if ($re1[2] !~ /^([0-9]{1,2}[a-z]|2)$/){
                push @errorsUp, "Error on line: $i";
            }
            if ($re1[3] =~ /^scaffold$/){
                my $a = splice (@re1, 3, 1);
                my $b = splice (@re1, 3, 1);
                splice (@re1, 3, 0, "$a\_$b");
                if ($re1[3] !~ /^scaffold.[0-9]{2,3}$/){
                    push @errorsUp, "Error on line: $i";
                }
            } elsif ($re1[3] !~ /^([WXYZ]|[0-9]{1,2})$/){
                push @errorsUp, "Error on line: $i";
            }
            if ($re1[4] !~ /^[0-9]{6,9}$/){
                push @errorsUp, "Error on line: $i";
            }
            if ($re1[5] !~ /^[rf]$/){
                push @errorsUp, "Error on line: $i";	
            }
            
            # Validate Score
            if (($score !~ /^\d+(\.\d{1,4})?$/) || $score < 0.9100 || $score > 1.0000) {
                push @errorsUp, "Error on line: $i";    
            }
            
            # Validate Target Gene
            if ($targetGene !~ /^ENS([A-Z]{3}G|G)[0-9]{11}$/) {
                push @errorsUp, "Error on line: $i";    
            }
            
            # Validate Position
            if (exists $positionHash{$position}){
            } else {
                push @errorsUp, "Error on line: $i"; 
            }
            
            # Validate Strand
            if ($strand !~ /^[\-+]+$/) {
                push @errorsUp, "Error on line: $i";    
            }
            
            # Gene Description
            if($geneDescription =~ /^[\^\/\\,'"]+$/){
                push @errorsUp, "Error on line: $i";    
            }
            
            # Errors array
          if (@errorsUp) {
            #print "Content-type: text/html\n\n";
            print top_html("Re1 Target Gene Data");
            print myUploadTitle();
            print myMenu();
                foreach (@errorsUp) {
                    print "<br>$_";
                }
            print myUploadForm();
            } else {
        
           # print "Content-type: text/html\n\n";
            
            
            my $dbh = DBI->connect("DBI:mysql:host=db-mysql;database=bif724_161a16", "bif724_161a16", $password) or die "problem connecting" . DBI->errstr;
            my $sql = "insert into a1_data values (?,?,?,?,?,?)";
            my $sth = $dbh->prepare($sql) or die "problem with prepare" . DBI->errstr;
            my $rows = $sth->execute($re1, $score, $targetGene, $position, $strand, $geneDescription);
            $dbh->disconnect() or die "problem with disconnect" . DBI->errstr;
          }
            #print "Location: tyler_a1_view.cgi\n\n";
         }
              
        }

    
    # Errors array
    if (@errorsU) {
       # print "Content-type: text/html\n\n";
        print top_html("Re1 Target Gene Data");
        print myUploadTitle();
        print myMenu();
        foreach (@errorsU) {
            print "<br>$_";
        }
        print myUploadForm();
    } 
    
    

} else {
    # form not submitted, so display form
    #print "Content-type: text/html\n\n";
    print top_html("Re1 Target Gene Data");
    print myUploadTitle();
    print myMenu();
    print myUploadForm();
    print bottom_html();
}   
