import os, datetime, gzip

def printt(label):

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S \t {}".format(label)))

    return None

raw_fastq_dir = '/Users/adrian/research/keilir/data/raw_fastq/'

samples = os.listdir(raw_fastq_dir)
samples = [sample for sample in samples if 'MITF' in sample or '53BP1' in sample]
samples.sort()
print(samples, len(samples))
print()

for sample in samples:
    printt(sample)
    pairs = os.listdir(raw_fastq_dir + sample)
    pairs.sort()

    for pair in pairs:
        target = raw_fastq_dir + sample + '/' + pair

        with gzip.open(target, 'rb') as f:
            for a, b in enumerate(f):
                pass

        number_of_lines = a+1
        reads = number_of_lines/4
        mr = reads/1e6
        message = "{} contains {} lines, {} reads, {:.2f} mr".format(pair, number_of_lines, reads, mr)
        printt(message)
