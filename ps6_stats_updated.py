#!/usr/bin/env python

# Program Header
# Course: Bi621
# Name:   Gerardo Perez
# Description: Python script that computes and collects assembly statistics
# from fasta files
#
#
# Development Environment: Atom 1.38.2
# Version: Python 3.7.3
# Date:  06/21/2019
#################################################




# Imports modules
import argparse
import re
import matplotlib.pyplot as plt

# Creates an arguement passer
parser = argparse.ArgumentParser(description="A program for K-mers")

# Adds arguemets by calling the arguement passer
parser.add_argument("-k", "--kmer_size", type = int, help="specify the k-mer size", required=True)


# Adds arguemets by calling the arguement passer
parser.add_argument("-f", "--filename", help="specify the filename", required=True)
#args = parser.parse_args()

# Adds arguemets by calling the arguement passer
parser.add_argument("-o", "--outputname", help="specify the filename", required=True)

# Parses arguemets through using the parse args method.
args = parser.parse_args()

# creates variables for args parse
K = args.kmer_size
file=args.filename
output=args.outputname


#Creates variables
N50 = 0
#K = 49

#Creates lists
Kmer_len = []
physical_length = []
Kmer_cov = []

# opens a text file to read and stores the text file as a variable.
with open(file, 'r') as fh:

    # A for loop that goes through each line in the text file.
    for line in fh:

        # regex function that finds the line that has the specific first character.
        if re.match(r'^>', line):

            #Uses regex to find the specif pattern and returns an array of finds.
            match1 = re.findall(r'length_(\d+)_cov_.*', line)

            # for loop that goes through an array
            for i in match1:

                # adds float values to a new list
                Kmer_len.append(float(i))

                #sorts the list
                Kmer_len.sort(reverse=True)

            #Uses regex to find the specif pattern.
            match2 = re.findall(r'length_\d+_cov_(.*)', line)

            # for loop that goes through an array
            for i in match2:

                # adds float values to a new list
                Kmer_cov.append(float(i))

                #sorts the list
                Kmer_cov.sort(reverse=True)

# for loop that goes through the lengh of an array
for i in range(len(Kmer_len)):

    # adds computed values to a new list
    physical_length.append(Kmer_len[i] + K -1)


number_contigs = len(physical_length)

max_contig = physical_length[0]

mean_contig = sum(physical_length)/len(physical_length)

total_len_contigs = sum(physical_length)

half_sum = total_len_contigs/2

# Jason said that might be wrong
mean_depth_coverage = sum(Kmer_cov)/(len(Kmer_cov))

# Creates a variable
kmer_sum = 0

# for loop that goes through the lengh of an array
for i in range(len(physical_length)):

        # computes the physical length sum using the for loop
        kmer_sum = kmer_sum + physical_length[i]

        # if statemnt that checks if the physical length
        # sum equals or is greater then the mid point
        if kmer_sum>= half_sum:

            # If true than the index value is stored into a variable
            N50 = physical_length[i]


            break




# prints statements
print("Number of contigs:", number_contigs)
print("Maximum contig lenth:", max_contig)
print("Mean contig:", mean_contig)
print("Total length of the genome assembly:",total_len_contigs )
print("Mean depth coverage:", mean_depth_coverage)
print("N50 value of assembly:", N50)

# Opens a text file to write, stores the text file as a variable.
f1 = open('%s_stats_kmer.tsv'%file, 'w')



# writes the formatted output to the tsv file.
f1.write("Number of contigs:%f\n" % number_contigs)
f1.write("Maximum contig lenth:%f\n" % max_contig)
f1.write("Mean contig:%f\n" % mean_contig)
f1.write("Total length of the genome assembly:%f\n" % total_len_contigs)
f1.write("Mean depth coverage:%f\n" % mean_depth_coverage)
f1.write("N50 value of assembly:%f\n"% N50)






# Creates a list
div_hundred=[]

# for loop that goes through a list
for i in physical_length:

    # index is converted to an int
    i = int(i)

    # int value is computed to the rounded down hundred
    div_hundred.append((i//100)*100)




# Creates a dictionary
contig_dict = {}

# for loop that goes through a range of 100 with a set max value
for i in range(0, int(max_contig), 100):

    #stores 0 as a value for the key
    contig_dict[i] = 0

# for loop that goes through a list
for contig in physical_length:

    # for loop that goes through the keys in dictionary
    for hundred in contig_dict.keys():

        # If statement that compares contig to hundred values
        if contig>= hundred:

            # If true then value is stored into variable
            bucket=hundred

    # If statement that checks if key is in dictionary
    if bucket in contig_dict:

        # if true than increments a value of one
        contig_dict[bucket]+=1


# writes the formatted output to the tsv file
f1.write("# Contig length\tNumber of contigs in this category\n")

# A for loop that goes through the items in the dictionary.
for key, value in contig_dict.items():

    # writes the formatted output to the tsv file.
    f1.write("{0}\t{1}\n".format(key,value))


f1.close()


# Plots the distribution of quality scores of a specific index position
# in the array.
plt.bar(contig_dict.keys(), contig_dict.values(), log=True)


# Labels a title
plt.title('KMER_LENGTH = %i' %K)

# Labels Y axis
plt.ylabel('Number of contigs in this category')

# Limits the x-axis in plot
#plt.xlim(0,100)

# Labels x axis
plt.xlabel('Contig length ')

# Outputs the plot.
#plt.show()

# outputs a png file
plt.savefig(output)









#
