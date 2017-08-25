This file is a guide to the scripts associated with the preprint:

"Genome size and the extinction of small populations" by Thomas LaBar and Christoph Adami,

available on bioRxiv at : http://www.biorxiv.org/content/early/2017/08/08/173690

There are three main groups of files within this directory:

	configuration files, stored in the directory "config_files"
	submission files, stored in the directory "sub_files"
	data analysis files, stored within the main directory
	
This preprint used the Avida digital evolution systems, described and available at:
https://github.com/devosoft/avida
	
The configuration files are the main ".cfg" files needed to run the Avida program.
They are as follows:

	analyze_lethalmeasure_finaldominant.cfg: A script for Avida's Analyze Mode to
	examine the most abundant final genotype from the 20 additional populations evolved
	under the Variable Mutation Rate treatment to more finely measure the change in the
	likelihood of lethal mutations over time (Figures 2 & 3).
	
	analyze_lethalmeasure.cfg: A script for Avida's Analyze Mode to examine the same data
	as above, but it also analyzes the evolutionary lineage of the final, most abundant,
	genotype.
	
	avida.cfg: This file contains all of the main parameter settings for Avida. These are
	set by the computing cluster submission files located in the "sub_files" directory.
	
	default-heads-minimal.org: Organism file for the minimal, genome length 15, Avida
	ancestor.
	
	environment_notraits.cfg: Avida environment file that turns off selection for the
	9 Avida logic tasks (No Trait Evolution treatment)
	
	environment.cfg: Avida environment file for the Logic-9 environment used in most
	experimental designs here.
	
	events_lethalmeasure.cfg: Avida event file for the 20 additional populations
	evolved under the Variable Mutation Rate treatment.
	
	events.cfg: Avida event file for most of the treatments.
	
	instset_heads.cfg: File that creates the instruction set, or the genetic code,
	for these experiments.
	
	This directory also contains a subdirectory, "event_files_lethalmeasure_replay",
	which contains the event files for experiments where the 5 genotypes were evolved
	at different mutation rates to measure the role of lethal mutational load in
	population extinction (Figure 4)
	
The submission files are the files used to run the experiments on Michigan State's
computing cluster. The main experimental parameters are set in these files.

	avida_a_lethalmeasure_finaldominant.sub: Runs Avida's analyze mode with
	"analyze_lethalmeasure_finaldominant.cfg" as the configuration file.
	
	avida_a_lethalmeasure.sub: Runs Avida's analyze mode with
	"analyze_lethalmeasure.cfg" as the configuration file.
	
	avida_fixedlength.sub: Script to run the Fixed Genome Size treatment
	experiments.
	
	avida_fixedmut.sub: Script to run the Fixed Mutation Rate treatment
	experiments.
	
	avida_lethalmeasure.sub: Runs the 20 additional populations under the
	Variable Mutation Rate treatment to measure the likelihood of lethal mutations
	
	avida_lowmut.sub: Script to run the Low Mutation Rate treatment
	experiments.
	
	avida_notraits.sub: Script to run the No Trait Evolution treatment
	experiments.
	
	avida_repeat.sub: Script to run the Variable Mutation Rate treatment
	experiments. This is called repeat beacause it repeats the original treatment
	of (LaBar and Adami 2016; PLoS Computational Biology)
	
	This directory also contains a subdirectory, "lethalmeasure_varmut", which contains
	the submission files for the five genotypes we evolved at a range of mutation rates
	
The rest of the files are those for data analysis and figure creation.

	figure.r: R script to make all of the manuscript figures.
	
	create_csv.py: Creates a csv file containing the data on extinction and genome size
	for the main treatments
	
	create_lethalmeasure_csv.py: Creates a csv file from the 20 additional populations
	evolved under the Variable Mutation Rate treatment with a variety of statistics
	
	create_lethalmeasure_time_csv.py: Creates a csv file from the 20 additional populations
	evolved under the Variable Mutation Rate treatment to measure how genome size and extinction
	change over time.
	
	create_lethalmeasure_varmut_csv.py: Creates a csv file for the experiments using the
	five genotypes from the 20 additional Variable Mutation Rate treatment populations
	when the genomic mutation rate was varied.
	

