import os

#
# 0. user-defined variables
#
raw_fastq_dir = '/Users/adrian/research/keilir/data/testing/'
clean_fastq_dir = '/Users/adrian/research/keilir/data/testing_clean/'
results_dir = '/Users/adrian/research/keilir/results/qc/'
threads = 2

#
# 1. select working files
#
all_input_files = []
folders = os.listdir(raw_fastq_dir)
for folder in folders:

    all_input_files = []
    input_file_names = os.listdir(raw_fastq_dir + folder)
    for input_file_name in input_file_names:
        full_path = raw_fastq_dir + folder + '/' + input_file_name
        all_input_files.append(full_path)

    all_input_files_string = ' '.join(all_input_files)

    #
    # 2. launch command
    #

    output_dir = results_dir + folder
    if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)

    command = 'time fastqc {} -o {} -t {} -a extra_adapters.txt'.format(all_input_files_string, output_dir, threads)

    print()
    print(command)
    print()
    os.system(command)
