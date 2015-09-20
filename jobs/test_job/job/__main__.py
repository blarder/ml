import sys
import pickle
import sklearn


model_output_file = sys.argv[1]
metadata_output_file = sys.argv[2]

# ALGORITHM GOES HERE!

with open(model_output_file, 'w') as f:
    f.write('PICKLED MODEL')

with open(metadata_output_file, 'w') as f:
    f.write('MODEL METADATA')
