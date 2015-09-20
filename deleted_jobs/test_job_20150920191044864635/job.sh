#!/bin/bash

# set the number of nodes and processes per node
#PBS -l nodes=1:ppn=1

# set max wallclock time
#PBS -l walltime=100:00:00

# set name of job
#PBS -N job

# mail alert at start, end and abortion of execution
#PBS -m bea

# send mail to this address
#PBS -M brett.larder@st-hildas.ox.ac.uk

# use submission environment
#PBS -V




# start job from the directory it was submitted
cd $PBS_O_WORKDIR

module load python

pip install --user -r /data/phys-pw-10pw/shil3504/jobs/test_job/job/requirements.txt




python /data/phys-pw-10pw/shil3504/jobs/test_job/job /data/phys-pw-10pw/shil3504/jobs/test_job/model.pkl /data/phys-pw-10pw/shil3504/jobs/test_job/metadata.txt




