# Needleman-Wunsch Sequence Alignment Script

# Author: Tyler Murphy
# Purpose: Recreate the NW algorithm for DNA alignment with a simple script.

use strict;
use warnings;

my $s1 = "ACTGATTCA";
my $s2 = "ACGCATCA";
my $len1 = (length($s1)) + 1;
my $len2 = (length($s2)) + 1;
my $match = 1;
my $mismatch = -1;
my $gap = -2;
my ($matrix, $i, $j, $k, $l, @twoD);

# Split sequences into arrays
my @seq1 = split(//, $s1);
my @seq2 = split(//, $s2);

# Build matrix
for ($k=0; $k<=$len2 -1; $k++){
	# build first row
	if ($k=0){
		for ($i=0; $i<=$len2-1; $i++){
			if($i=0){
				$twoD[$k][$i] = 0;
			} else {
				$twoD[$k][$i] = ($gap + ($twoD[$k][$i-1]));
			}
		}
	} else {
	
	# calculate remaining rows using max of 3 possible values
		for ($j=0; $j<=$len1-1; $j++){
			if ($j=0){
				$twoD[$k][$i] = ($gap + $twoD[$k-1][$j]);
			} else {
				my @num;
				# Variable 1
				push (@num, $gap + $twoD[$k-1][$j]);
				# Variable 2
				push (@num, $gap + $twoD[$k][$j-1]);
				# Variable 3
				if ($seq1[$j-1] eq $seq2[$k-1]){
					push (@num, $$match + $twoD[$k-1][$j-1]);
				} else {
					push (@unm, $mismatch + $twoD[$k-1][$j-1]);
				}
				# sort @num
				my @sorted = sort {$a <=> $b} @num;
				$twoD[$k][$j] = splice(@sorted, ($gap+1));
			}
		}
	}
}

foreach $i (@twoD){
	print "@{$i}\n";
}
