###
### usage: time python trimmer.py &> messages.trimmer.txt
###

import os, datetime, sys, re

def printt(label):

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S \t {}".format(label)))

    return None

def trimmomatic_caller(sample):

    executable='time java -jar {}trimmomatic-0.39.jar PE -threads {} -phred33 '.format(trimmomatic_path,number_threads)

    #
    # typical options for RNAseq
    #options=' ILLUMINACLIP:{}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'.format(adapter_file)
    #
    # options specific for CUT & RUN:
    # from https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1802-4
    # https://bitbucket.org/qzhudfci/cutruntools/src/default/integrated.sh
    # ILLUMINACLIP:$adapterpath/Truseq3.PE.fa:2:15:4:4:true LEADING:20 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:25
    #
    # their options
    options=' ILLUMINACLIP:{}:2:15:4:4:True LEADING:20 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:25'.format(adapter_file)

    # my options
    #options=' ILLUMINACLIP:{}:2:30:10:2:True LEADING:20 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:25'.format(adapter_file)

    #
    #
    #

    detected = os.listdir(raw_fastq_dir + sample)
    detected.sort()
    print(detected)

    input1 = raw_fastq_dir + sample + '/' + detected[0]
    input2 = raw_fastq_dir + sample + '/' + detected[1]

    output_dir = clean_fastq_dir + sample + '/'
    if os.path.exists(output_dir) == False:
        os.mkdir(output_dir)

    output1 = output_dir + sample + '_R1_clean.fastq.gz'
    output2 = output_dir + sample + '_R2_clean.fastq.gz'

    garbage1 = output_dir + sample + '_R1_garbage.fastq.gz'
    garbage2 = output_dir + sample + '_R2_garbage.fastq.gz'

    input_files = input1 + ' ' + input2
    output_files = output1 + ' ' + garbage1 + ' ' + output2 + ' ' + garbage2

    command = executable + input_files + ' ' + output_files + options

    printt('about to clean {}'.format(sample))
    print('')
    print(command)
    print('')
    os.system(command)
    print('')
    #sys.exit()

    return None

# 0. user defined variablessample
raw_fastq_dir = '/Users/adrian/research/keilir/data/raw_fastq/'
clean_fastq_dir = '/Users/adrian/research/keilir/results/trimming/their/'
trimmomatic_path = '/Users/adrian/software/Trimmomatic-0.39/'
adapter_file = trimmomatic_path + 'adapters/TruSeq3-PE-2.fa'
number_threads = 4 # marginal improvement using 8 threads vs 4. Keep 4.

# 1. recover samples
all_labels = os.listdir(raw_fastq_dir)
all_labels.sort()
print(all_labels)

# 2. iterate Trimmomatic
for label in all_labels:
    trimmomatic_caller(label)
