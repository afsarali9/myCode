#!/usr/bin/perl

# Author: Tyler Murphy
# Purpose: The purpose of this project is to access genbank data repositories
#   according to two command-line arguments (file and gene), writing to output files
#   the binomial gene name and the protein sequence, gene sequence, or reverse-compliment
#   of the protein sequence.


use strict;
use warnings;
use Bio::Seq;
use Bio::SeqIO;
use Bio::DB::GenBank;
use Bio::Species;
use Cwd 'abs_path';


# accept @ARGS when calling script for id and geneName
my $in = $ARGV[0];
my $geneName = $ARGV[1];

# open file and read through each line
open(my $fh, '<:encoding(UTF-8)', $in) or die "Could not open file $in";
 
# Create two outfile variables
my $dnaOutFile = "dna_tyler_$geneName.fa";
my $protOutFile = "aa_tyler_$geneName.fa";

# create bio::seq objects to output dna and protein
my $seqioDNA_o = Bio::SeqIO->new( '-format' => 'fasta' , -file => ">$dnaOutFile");
my $seqioPROT_o = Bio::SeqIO->new( '-format' => 'fasta' , -file => ">$protOutFile");

while (my $id = <$fh>) {
  chomp $id;
  print "$id\n";

  # if both $id and $geneName were entered, then proceed
  if ($in && $geneName) {
  
  # get a GenBank file by ID number from repository
  my $db_o = Bio::DB::GenBank->new;
  my $seq_o = $db_o->get_Seq_by_id($id);
    if ($seq_o) {
        
        #get species binomial name using Bio::Species and replace spaces with underscore
        my $species_o = Bio::Species->new;
        $species_o = $seq_o->species;
        my $bi = $species_o->binomial('FULL');    
        $bi =~ s/ /_/g;
        print $bi;
    
    # store all features of seq_o in feat_o
      foreach my $feat_o ($seq_o->get_SeqFeatures()) {
          
          # if the feature is CDS, continue...
          if (($feat_o->primary_tag() eq "CDS")){
              # ...followed by each tag stored in tag_o
              foreach my $tagvalue ($feat_o->get_tag_values('gene')){
                  # if the set of values include one for specific gene 
                  if ($tagvalue eq $geneName) {
                      foreach my $transvalue ($feat_o->get_tag_values('translation')){
                          
                          # isolate subsequence
                          my $subseq = $seq_o->subseq($feat_o->start,$feat_o->end);
                          
                          # create sequence objects containing binomial id and subsequence or protein sequence
                          my $sequence_o = Bio::Seq->new ( -id => $bi, -seq => $subseq);
                          my $seqProt_o = Bio::Seq->new ( -id => $bi, -seq => $transvalue);
                          
                          # create revcomp object for later use if necessary
                          my $revcomp_o = $sequence_o->revcom();
                          
                          # create the reverse compliment manually, as revcom() is stored in an object.
                          my $reverseSeq = reverse($subseq);
                          $reverseSeq =~ tr/ATGC/TACG/;
                          my $sequenceRev_o = Bio::Seq->new (-id => $bi, -seq => $reverseSeq);
                          
                          # create absolute path variable to store location of outfile.
                          my $path = abs_path($0);
                          $path =~ s/A2.pl//;
                          
                          # write data to file depending on whether strand is +1 vs -1
                          if ($feat_o->strand == 1) {
                              $seqioDNA_o->write_seq($sequence_o);
                              print "-" x60, "\n";
                              print "DNA file created with binomial name and subsequence.\n";
                              print "File name: dna_tyler_$geneName.fa\n";
                              print "Location: $path\n";
                              
                          } else {
                              $seqioDNA_o->write_seq($sequenceRev_o);
                              print "-" x60, "\n";
                              print "DNA file created with binomial name and reverse compliment of subsequence.\n";
                              print "File name: dna_tyler_$geneName.fa\n";
                              print "Location: $path\n";
                          }
                          # write protein seq to file                  
                          $seqioPROT_o->write_seq($seqProt_o);
                          print "-" x60, "\n";
                          print "Protein file created.\n";
                          print "File name: aa_tyler_$geneName.fa\n";
                          print "Location: $path\n";           
                          
                           
                      }
                  }
              }
          }
              
             
      }
        
    } else {
        print "Unable to obtain sequence $id\n";
    }
  } else {
      print "Gene ID and Gene Name were not entered.";
  }
}