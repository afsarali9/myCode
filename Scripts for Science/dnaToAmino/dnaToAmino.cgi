#!/usr/bin/perl

# Title: DNA Conversion to Amino Acid Output 

# Author: Tyler Murphy
# Purpose: Create a tool that takes dna sequence input and outputs the
#		corresponding amino acid sequence and molecular weight of the 
#		molecule.  
  
  
use strict;
use warnings;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;
use DBI;
require 'dnaToAmino_lib.pl';
  
  
#   Create Hash Table of Amino Acids
my %rnahash = (  
TTT=> "K", TTC=> "K",  
CTT=> "E", CTC=> "E",  
TTG=> "N", TTA=> "N",  
CTG=> "D", CTA=> "D",  
TGT=> "T", TGG=> "T", TGC=> "T", TGA=> "T",  
CGT=>"A", CGG=>"A", CGC=>"A", CGA=>"A",  
CCT=> "G", CCG=> "G", CCC=> "G", CCA=> "G",  
CAT=> "V", CAG=> "V", CAC=> "V", CAA=> "V",  
TAT=> "M", TAC=> "M", 
ATT=> "*", ATC=> "*", ACT=> "*",  
TAG=> "I", TAA=> "I",  
ATG=> "Y", ATA=> "Y",  
GTT=> "Q", GTC=> "Q",  
TCG=> "S", TCA=> "S", AGT=> "S", AGG=> "S", AGC=> "S", AGA=> "S",  
GTG=> "H", GTA=> "H",  
ACG=> "C", ACA=> "C",  
GGT=> "P", GGG=> "P", GGC=> "P", GGA=> "P",  
ACC=> "W",  
TCT=> "R", TCC=> "R", GCT=> "R", GCG=> "R", GCC=> "R", GCA=> "R",  
AAT=> "L", AAC=> "L", GAT=> "L", GAG=> "L", GAC=> "L", GAA=> "L",  
AAG=> "F", AAA=> "F");  
  
#   Variable/Array/Hash Declarations 
my $rawDna = $ARGV[0]; 
my @dnatriplet = keys(%rnahash); 
my @rnasingle = values(%rnahash); 
 
my ($dna, $bp, $codon, $i, $j, $k, $join, $startvalue); 
my (@codonarray, @format); 
 
#   Obtain the string:
if (param()) {
    print "Content-type: text/html\n\n";
    print top_html("DNA to Amino Acid Conversion Tool");
    print myAddTitle();
    print myform();
    my $break = "\n\n";
    
    # form must have been submitted, so validate data
    my $dna = param("dnaIN");

    #   Remove invalid characters using regular experessions, convert to uppercase: 
    $dna =~ s/[^ATCGatcg]//g;  
    $dna = uc($dna);  
     
    #   Remove any bases off the end of the string that is not divisible by 3. 
    while (scalar length($dna) %3 != 0){  
        chop($dna); 
    }  
         
    #   Loop through dna string, assign every 3 bases to variable, 
    #   loop variable through hash table, assign hash values to variable. 
    for($i=0; $i< scalar length($dna); $i+=3){ 
        $bp = substr($dna, $i, 3); 
        $codon .= $rnahash{$bp};  
    } 
    
    #	Split dna string and assign to hash: 
    @codonarray = split //, $codon; 
     
     
    #   Print format loops: 
    $startvalue = 1; 
    foreach (@codonarray){ 
        printf ("%*s ", 10, $startvalue); 
    #	Splice together every 10 values from @codonarray:
    #   Store each group of 10 as entries in the array @format
        for (my $j = 0; $j<6; $j++){ 
            @format = splice(@codonarray, 0, 10); 
            $join = join('', @format); 
            print("$join"); 
     
    #	Add space between sections of 10: 
        if (($j<5) and (((length($join)) == 10))){ 
            print " " 
            } 		
        }	 
        print "\n"; 
         
    #	Increases starting value for each new right-justified line 
        $startvalue += 60; 
    } 
      
    #	Calculate molecular weight of dna string: 
    my %dnahash = (A => 135.13, T => 126.10, C => 111.10, G => 150.12); 
    my $weight; 
    my $bp2; 
     
    for($k=0; $k< scalar length($dna); $k+=1){ 
       $bp2 = substr($dna, $k, 1); 
       $weight += $dnahash{$bp2}; 
        }
        printf("Total molecular weight in g/mol is: %.4f\n", $weight);
} else {
    # form not submitted so display the form
    print "Content-type: text/html\n\n";
    print top_html("DNA to Amino Acid Conversion Tool");
    print myAddTitle();
    print myform();  
}
