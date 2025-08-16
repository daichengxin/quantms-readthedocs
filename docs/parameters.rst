Parameters
===========

This page lists pipeline parameters extracted from the Nextflow schema.

IL_equivalent
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``IL_equivalent``
     - boolean
     - true
     - Should isoleucine and leucine be treated interchangeably when mapping search engine hits to the database? Default: true

acquisition_method
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``acquisition_method``
     - string
     - 
     - Proteomics data acquisition method

add_decoys
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``add_decoys``
     - boolean
     - 
     - Generate and append decoys to the given protein database

add_snr_feature_percolator
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``add_snr_feature_percolator``
     - boolean
     - false
     - Whether add signal-to-noise ratio features for identification rescoring in percolator

add_triqler_output
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``add_triqler_output``
     - boolean
     - false
     - Also create an output in Triqler's format for an alternative manual post-processing with that tool

alignment_order
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``alignment_order``
     - string
     - ``star``
     - The order in which maps are aligned. Star = all vs. the reference with most IDs (default). TreeGuided = an alignment tree is calculated first based on similarity measures of the IDs in the maps.

allowed_missed_cleavages
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``allowed_missed_cleavages``
     - integer
     - 2
     - Specify the maximum number of allowed missed enzyme cleavages in a peptide. The parameter is not applied if `unspecific cleavage` is specified as enzyme.

average
-------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``average``
     - string
     - ``median``
     - Averaging method used to compute protein abundances from peptide abundances.

best_charge_and_fraction
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``best_charge_and_fraction``
     - boolean
     - 
     - Distinguish between fraction and charge states of a peptide. (default: 'false')

calibration_set_size
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``calibration_set_size``
     - number
     - 0.15
     - Percentage of number of calibration set for DeepLC

config_profile_contact
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``config_profile_contact``
     - string
     - 
     - Institutional config contact information.

config_profile_description
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``config_profile_description``
     - string
     - 
     - Institutional config description.

config_profile_name
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``config_profile_name``
     - string
     - 
     - Institutional config name.

config_profile_url
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``config_profile_url``
     - string
     - 
     - Institutional config URL link.

consensusid_algorithm
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``consensusid_algorithm``
     - string
     - ``best``
     - How to combine the probabilities from the single search engines: best, combine using a sequence similarity-matrix (PEPMatrix), combine using shared ion count of peptides (PEPIons). See help for further info.

consensusid_considered_top_hits
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``consensusid_considered_top_hits``
     - integer
     - 
     - Only use the top N hits per search engine and spectrum for combination. Default: 0 = all

consensusid_debug
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``consensusid_debug``
     - integer
     - 0
     - Debug level for ConsensusID. Increase for verbose logging

consider_modloss
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``consider_modloss``
     - boolean
     - false
     - If modloss ions are masked to zeros in the ms2 model. modloss ions are mostly useful for phospho MS2 prediction model.

contrasts
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``contrasts``
     - string
     - 
     - Experimental: Allows full control over contrasts by specifying a set of contrasts in a semicolon separated list of R-compatible contrasts with the condition names/numbers as variables (e.g. `1-2;1-3;2-3`). Overwrites `--ref_condition`.

convert_dotd
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``convert_dotd``
     - boolean
     - 
     - Convert bruker .d files to mzML

custom_config_base
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``custom_config_base``
     - string
     - ``https://raw.githubusercontent.com/nf-core/configs/master``
     - Base directory for Institutional configs.

custom_config_version
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``custom_config_version``
     - string
     - ``master``
     - Git commit id for Institutional configs.

database
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``database``
     - string
     - 
     - The `fasta` protein database used during database search. *Note:* For DIA data, it must not contain decoys.

db_debug
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``db_debug``
     - integer
     - 0
     - Debug level when running the database search. Logs become more verbose and at '>5' temporary files are kept.

decoy_method
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``decoy_method``
     - string
     - ``reverse``
     - Choose the method to produce decoys from input target database.

decoy_string
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``decoy_string``
     - string
     - ``DECOY_``
     - Pre- or suffix of decoy proteins in their accession

decoy_string_position
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``decoy_string_position``
     - string
     - ``prefix``
     - Location of the decoy marker string in the `fasta` accession. Before (prefix) or after (suffix)

decoydatabase_debug
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``decoydatabase_debug``
     - integer
     - 0
     - Debug level for DecoyDatabase step. Increase for verbose logging.

description_correct_features
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``description_correct_features``
     - integer
     - 
     - Use additional features whose values are learnt by correct entries. See help text. Default: 0 = none

diann_debug
-----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``diann_debug``
     - integer
     - 3
     - Debug level

diann_export_xic
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``diann_export_xic``
     - boolean
     - false
     - instructs DIA-NN to extract MS1/fragment chromatograms for identified precursors within X seconds from the elution apex, with X set to 10s if not provided;equivalent to the 'XICs' option in the GUI

diann_normalize
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``diann_normalize``
     - boolean
     - true
     - Enable cross-run normalization between runs by diann.

diann_report_decoys
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``diann_report_decoys``
     - boolean
     - false
     - Save decoy PSMs to the main .parquet report for DIA-NN 2.0.*

diann_speclib
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``diann_speclib``
     - string
     - 
     - The spectral library to use for DIA-NN

email
-----

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``email``
     - string
     - 
     - Email address for completion summary.

email_on_fail
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``email_on_fail``
     - string
     - 
     - Email address for completion summary, only when pipeline fails.

empirical_assembly_log
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``empirical_assembly_log``
     - string
     - 
     - The log file for the empirical assembly, Only used if `--skip_preliminary_analysis` is set to `true` and `--diann_speclib` is passed. If passed, will use that log file to carry out the DIA-NN search, instead of running a preliminary search.

empirical_assembly_ms_n
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``empirical_assembly_ms_n``
     - integer
     - 200
     - The number of randomly selected spectrum files.

enable_diann_mztab
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``enable_diann_mztab``
     - boolean
     - true
     - Export the DIA-NN and DIA results to mzTab

enable_mod_localization
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``enable_mod_localization``
     - boolean
     - 
     - Turn the mechanism on.

enable_pmultiqc
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``enable_pmultiqc``
     - boolean
     - 
     - Enable generation of pmultiqc report? default: 'false'

enzyme
------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``enzyme``
     - string
     - ``Trypsin``
     - The enzyme to be used for in-silico digestion, in 'OpenMS format'

export_decoy_psm
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``export_decoy_psm``
     - boolean
     - 
     - Whether export PSM from decoy in final identification results

export_mztab
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``export_mztab``
     - boolean
     - true
     - Export the results in mzTab format.

extractpsmfeature_debug
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``extractpsmfeature_debug``
     - integer
     - 0
     - Debug level when running the PSMFeatureExtractor step. Increase for verbose logging

fdr_level
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``fdr_level``
     - string
     - ``psm_level_fdrs``
     - Calculate FDR on PSM ('psm_level_fdrs') or peptide level ('peptide_level_fdrs')?

feature_generators
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``feature_generators``
     - string
     - ``deeplc,ms2pip``
     - Which feature generator to generate feature.

feature_with_id_min_score
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``feature_with_id_min_score``
     - number
     - 0.1
     - The minimum probability (e.g.: 0.25) an identified (=id targeted) feature must have to be kept for alignment and linking (0=no filter).

feature_without_id_min_score
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``feature_without_id_min_score``
     - number
     - 0.75
     - The minimum probability (e.g.: 0.75) an unidentified feature must have to be kept for alignment and linking (0=no filter).

find_best_model
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``find_best_model``
     - boolean
     - true
     - If find best MS2 model.

fix_peptides
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``fix_peptides``
     - boolean
     - ``false``
     - Use the same peptides for protein quantification across all samples.(Default false)

fixed_mods
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``fixed_mods``
     - string
     - ``Carbamidomethyl (C)``
     - A comma-separated list of fixed modifications with their Unimod name to be searched during database search

force_model
-----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``force_model``
     - boolean
     - false
     - Force to run with provided MS2PIP model. Don't look for the best model and validation

fragment_mass_tolerance
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``fragment_mass_tolerance``
     - number
     - 0.03
     - Fragment mass tolerance used for database search. The default of 0.03 Da is for high-resolution instruments.

fragment_mass_tolerance_unit
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``fragment_mass_tolerance_unit``
     - string
     - ``Da``
     - Fragment mass tolerance unit used for database search. Possible values are 'ppm' (default) and 'Da'.

hook_url
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``hook_url``
     - string
     - 
     - Incoming hook URL for messaging service

id_only
-------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``id_only``
     - boolean
     - 
     - Only perform identification subworkflow.

idfilter_debug
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``idfilter_debug``
     - integer
     - 0
     - Debug level when running the IDFilter step. Increase for verbose logging

idmapper_debug
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``idmapper_debug``
     - integer
     - 0
     - Debug level for IDMapper step. Increase for verbose logging

idscoreswitcher_debug
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``idscoreswitcher_debug``
     - integer
     - 0
     - Debug level when running the re-scoring. Logs become more verbose and at '>5' temporary files are kept.

include_all
-----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``include_all``
     - boolean
     - true
     - Include results for proteins with fewer proteotypic peptide than indicated by top.

input
-----

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``input``
     - string
     - 
     - URI/path to an SDRF file (.sdrf.tsv) **OR** OpenMS-style experimental design with paths to spectra files (.tsv)

instrument
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``instrument``
     - string
     - 
     - Type of instrument that generated the data. 'low_res' or 'high_res' (default; refers to LCQ and LTQ instruments)

iso_debug
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``iso_debug``
     - integer
     - 0
     - Set the debug level

iso_normalization
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``iso_normalization``
     - boolean
     - false
     - Enable normalization of the channel intensities

isotope_correction
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``isotope_correction``
     - boolean
     - false
     - Enable isotope correction (highly recommended)

isotope_error_range
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``isotope_error_range``
     - string
     - ``0,1``
     - Comma-separated range of integers with allowed isotope peak errors for precursor tolerance (like MS-GF+ parameter '-ti'). E.g. -1,3

klammer
-------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``klammer``
     - boolean
     - 
     - Retention time features are calculated as in Klammer et al. instead of with Elude. Default: false

labelling_type
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``labelling_type``
     - string
     - 
     - Specify the labelling method that was used. Will be ignored if SDRF was given but is mandatory otherwise

lfq_intensity_threshold
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``lfq_intensity_threshold``
     - number
     - 1000
     - The minimum intensity for a feature to be considered for quantification. (default: '10000')

local_input_type
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``local_input_type``
     - string
     - ``mzML``
     - Overwrite the file type/extension of the filename as specified in the SDRF/design

luciphor_debug
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``luciphor_debug``
     - integer
     - 
     - Debug level for Luciphor step. Increase for verbose logging and keeping temp files.

luciphor_decoy_mass
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``luciphor_decoy_mass``
     - number
     - 
     - How much to add to an amino acid to make it a decoy for mod. localization.

luciphor_decoy_neutral_losses
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``luciphor_decoy_neutral_losses``
     - string
     - 
     - List of neutral losses to consider for mod. localization from an internally generated decoy sequence.

luciphor_neutral_losses
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``luciphor_neutral_losses``
     - string
     - 
     - List of neutral losses to consider for mod. localization.

mass_acc_automatic
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``mass_acc_automatic``
     - boolean
     - true
     - Choosing the MS2 mass accuracy setting automatically

mass_recalibration
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``mass_recalibration``
     - boolean
     - 
     - Recalibrates masses based on precursor mass deviations to correct for instrument biases. (default: 'false')

max_fr_mz
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_fr_mz``
     - number
     - 
     - The maximum fragment m/z for the in silico library generation or library-free search

max_mods
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_mods``
     - integer
     - 3
     - Maximum number of modifications per peptide. If this value is large, the search may take very long.

max_multiqc_email_size
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_multiqc_email_size``
     - string
     - ``25.MB``
     - File size limit when attaching MultiQC reports to summary emails.

max_peptide_length
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_peptide_length``
     - integer
     - 40
     - Maximum peptide length to consider (works with MSGF and in newer Comet versions)

max_pr_mz
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_pr_mz``
     - number
     - 
     - The maximum precursor m/z for the in silico library generation or library-free search

max_precursor_charge
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``max_precursor_charge``
     - integer
     - 4
     - Maximum precursor ion charge. Omit the '+'

met_excision
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``met_excision``
     - boolean
     - true
     - Database searches accounted for N-terminal methionine excision, a common co-translational modification where the initial methionine is enzymatically removed from proteins.

min_consensus_support
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_consensus_support``
     - number
     - 
     - A threshold for the ratio of occurrence/similarity scores of a peptide in other runs, to be reported. See help.

min_fr_mz
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_fr_mz``
     - number
     - 
     - The minimum fragment m/z for the in silico library generation or library-free search

min_peaks
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_peaks``
     - integer
     - 10
     - Minimum number of peaks in the spectrum to be considered for the search engine. Default: 10

min_peptide_length
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_peptide_length``
     - integer
     - 6
     - Minimum peptide length to consider (works with MSGF and in newer Comet versions)

min_peptides_per_protein
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_peptides_per_protein``
     - integer
     - 1
     - [Ignored in Bayesian] Minimum number of peptides needed for a protein identification

min_pr_mz
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_pr_mz``
     - number
     - 
     - The minimum precursor m/z for the in silico library generation or library-free search

min_precursor_charge
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_precursor_charge``
     - integer
     - 2
     - Minimum precursor ion charge. Omit the '+'

min_precursor_intensity
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_precursor_intensity``
     - number
     - 1.0
     - Minimum intensity of the precursor to be extracted

min_precursor_purity
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_precursor_purity``
     - number
     - 0.0
     - Minimum fraction of the total intensity. 0.0:1.0

min_reporter_intensity
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``min_reporter_intensity``
     - number
     - 0.0
     - Minimum intensity of the individual reporter ions to be extracted.

mod_localization
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``mod_localization``
     - string
     - ``Phospho (S),Phospho (T),Phospho (Y)``
     - Which variable modifications to use for scoring their localization.

monochrome_logs
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``monochrome_logs``
     - boolean
     - 
     - Do not use coloured log outputs.

ms2_fragment_method
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ms2_fragment_method``
     - string
     - ``HCD``
     - The fragmentation method used during tandem MS. (MS/MS or MS2).

ms2_model
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ms2_model``
     - string
     - ``HCD2021``
     - Which deep learning model to generate feature.

ms2_model_dir
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ms2_model_dir``
     - string
     - 
     - The path of ms2 prediction model files. Providing model file to avoid repeated download and slow internet connection

ms2rescore
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ms2rescore``
     - boolean
     - false
     - Whether performing peptide identification rescoring with LC-MS predictors such as MS²PIP and DeepLC.

ms2rescore_fragment_tolerance
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ms2rescore_fragment_tolerance``
     - number
     - 0.05
     - Fragment mass tolerance used for MS2PIP

msstats_plot_profile_qc
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstats_plot_profile_qc``
     - boolean
     - false
     - Export MSstats profile QC plots including all proteins

msstats_remove_one_feat_prot
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstats_remove_one_feat_prot``
     - boolean
     - true
     - Omit proteins with only one quantified feature?

msstats_threshold
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstats_threshold``
     - number
     - 0.05
     - The threshold value for differential expressed proteins in MSstats plots based on adjusted p-value

msstatsiso_global_norm
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_global_norm``
     - boolean
     - true
     - Reference channel based normalization between MS runs on protein level data?

msstatsiso_reference_normalization
----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_reference_normalization``
     - boolean
     - true
     - Reference channel based normalization between MS runs on protein level data

msstatsiso_remove_norm_channel
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_remove_norm_channel``
     - boolean
     - true
     - Remove 'Norm' channels from protein level data

msstatsiso_rmpsm_withfewmea_withinrun
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_rmpsm_withfewmea_withinrun``
     - boolean
     - true
     - Remove the features that have 1 or 2 measurements within each run

msstatsiso_summarization_method
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_summarization_method``
     - string
     - ``msstats``
     - summarization methods to protein-level can be perfomed

msstatsiso_summaryformultiple_psm
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_summaryformultiple_psm``
     - string
     - ``sum``
     - select the feature with the largest summmation or maximal value

msstatsiso_useunique_peptide
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatsiso_useunique_peptide``
     - boolean
     - true
     - Use unique peptide for each protein

msstatslfq_feature_subset_protein
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatslfq_feature_subset_protein``
     - string
     - ``top3``
     - Which features to use for quantification per protein: 'top3' or 'highQuality' which removes outliers only

msstatslfq_quant_summary_method
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatslfq_quant_summary_method``
     - string
     - ``TMP``
     - which summary method to use: 'TMP' (Tukey's median polish) or 'linear' (linear mixed model)

msstatslfq_removeFewMeasurements
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``msstatslfq_removeFewMeasurements``
     - boolean
     - true
     - Keep features with only one or two measurements across runs?

multiqc_config
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``multiqc_config``
     - string
     - 
     - Custom config file to supply to MultiQC.

multiqc_logo
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``multiqc_logo``
     - string
     - 
     - Custom logo file to supply to MultiQC. File name must also be set in the MultiQC config file

multiqc_methods_description
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``multiqc_methods_description``
     - string
     - 
     - Custom MultiQC yaml file containing HTML including a methods description.

multiqc_title
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``multiqc_title``
     - string
     - 
     - MultiQC report title. Printed as page header, used for filename if not otherwise specified.

mzml_features
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``mzml_features``
     - boolean
     - false
     - Compute with mzmlstatistics step the features at MS1 level and output to a RAW file, only available for mzML files

normalize
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``normalize``
     - boolean
     - ``false``
     - Scale peptide abundances so that medians of all samples are equal.(Default false)

num_enzyme_termini
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``num_enzyme_termini``
     - string
     - ``fully``
     - Specify the amount of termini matching the enzyme cutting rules for a peptide to be considered. Valid values are `fully` (default), `semi`, or `none`

num_hits
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``num_hits``
     - integer
     - 1
     - Specify the maximum number of top peptide candidates per spectrum to be reported by the search engine. Default: 1

openms_peakpicking
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``openms_peakpicking``
     - boolean
     - 
     - Activate OpenMS-internal peak picking

outdir
------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``outdir``
     - string
     - ``./results``
     - The output directory where the results will be saved.

peakpicking_inmemory
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``peakpicking_inmemory``
     - boolean
     - 
     - Perform peakpicking in memory

peakpicking_ms_levels
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``peakpicking_ms_levels``
     - string
     - 
     - Which MS levels to pick as comma separated list. Leave empty for auto-detection.

percolator_debug
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``percolator_debug``
     - integer
     - 0
     - Debug level for Percolator step. Increase for verbose logging

performance_mode
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``performance_mode``
     - boolean
     - true
     - Set Low RAM & High Speed Mode for DIANN, including min-corr, corr-diff, and time-corr-only three parameters

pg_level
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``pg_level``
     - number
     - 2
     - Controls the protein inference mode

picked_fdr
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``picked_fdr``
     - boolean
     - true
     - Use picked protein FDRs

pipelines_testdata_base_path
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``pipelines_testdata_base_path``
     - string
     - ``https://raw.githubusercontent.com/nf-core/test-datasets/``
     - Base URL or local path to location of pipeline test dataset files

plaintext_email
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``plaintext_email``
     - boolean
     - 
     - Send plain-text email instead of HTML.

plex_corr_matrix_file
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``plex_corr_matrix_file``
     - string
     - 
     - Path to the correction matrix file for isobaric labelling, defaults are in assets folder

plfq_debug
----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``plfq_debug``
     - integer
     - 0
     - Debug level when running the re-scoring. Logs become more verbose and at '>666' potentially very large temporary files are kept.

pmultiqc_idxml_skip
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``pmultiqc_idxml_skip``
     - boolean
     - 
     - Skip idXML files (do not generate search engine scores) in pmultiqc report? default: 'true'

pp_debug
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``pp_debug``
     - integer
     - 0
     - Debug level when running the re-scoring. Logs become more verbose and at '>5' temporary files are kept.

precursor_isotope_deviation
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``precursor_isotope_deviation``
     - number
     - 10.0
     - Maximum allowed deviation (in ppm) between theoretical and observed isotopic peaks of the precursor peak

precursor_mass_tolerance
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``precursor_mass_tolerance``
     - integer
     - 5
     - Precursor mass tolerance used for database search. For High-Resolution instruments a precursor mass tolerance value of 5 ppm is recommended (i.e. 5). See also `--precursor_mass_tolerance_unit`.

precursor_mass_tolerance_unit
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``precursor_mass_tolerance_unit``
     - string
     - ``ppm``
     - Precursor mass tolerance unit used for database search. Possible values are 'ppm' (default) and 'Da'.

protein_inference_debug
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_inference_debug``
     - integer
     - 0
     - Debug level for the protein inference step. Increase for verbose logging

protein_inference_method
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_inference_method``
     - string
     - ``aggregation``
     - The inference method to use. 'aggregation' (default) or 'bayesian'.

protein_level_fdr_cutoff
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_level_fdr_cutoff``
     - number
     - 0.01
     - The experiment-wide protein (group)-level FDR cutoff. Default: 0.01

protein_quant
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_quant``
     - string
     - ``unique_peptides``
     - Quantify proteins based on:  * 'unique_peptides' = use peptides mapping to single proteins or a group of indistinguishable proteins (according to the set of experimentally identified peptides) * 'strictly_unique_peptides' (only LFQ) = use peptides mapping to a unique single protein only * 'shared_peptides' = use shared peptides, too, but only greedily for its best group (by inference score and nr. of peptides)

protein_quant_debug
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_quant_debug``
     - integer
     - 0
     - Debug level for the protein quantification step. Increase for verbose logging

protein_score
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protein_score``
     - string
     - ``best``
     - [Ignored in Bayesian] How to aggregate scores of peptides matching to the same protein

protocol
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``protocol``
     - string
     - ``automatic``
     - MSGF only: Labeling or enrichment protocol used, if any (options: 'automatic', 'phospho', 'iTRAQ', 'iTRAQ_phospho', 'TMT', 'none') Default: automatic

psm_clean
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``psm_clean``
     - boolean
     - false
     - Whether remove invalid PSM with empty spectra and invalid feature values

psm_level_fdr_cutoff
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``psm_level_fdr_cutoff``
     - number
     - 0.01
     - The experiment-wide PSM-level FDR cutoff. Default: 0.01

publish_dir_mode
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``publish_dir_mode``
     - string
     - ``copy``
     - Method used to save pipeline results to output directory.

quant_activation_method
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``quant_activation_method``
     - string
     - 
     - Operate only on MSn scans where any of its precursors features a certain activation method. Set to empty to disable.

quantification_method
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``quantification_method``
     - string
     - ``feature_intensity``
     - Choose between feature-based quantification based on integrated MS1 signals ('feature_intensity'; default) or spectral counting of PSMs ('spectral_counting'). **WARNING:** 'spectral_counting' is not compatible with our MSstats step yet. MSstats will therefore be disabled automatically with that choice.

quantify_decoys
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``quantify_decoys``
     - boolean
     - false
     - Also quantify decoys? (Usually only needed for Triqler post-processing output with `--add_triqler_output`, where it is auto-enabled)

quick_mass_acc
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``quick_mass_acc``
     - boolean
     - true
     - when choosing the MS2 mass accuracy setting automatically, DIA-NN will use a fast heuristical algorithm instead of IDs number optimisation

random_preanalysis
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``random_preanalysis``
     - boolean
     - false
     - Enable random selection of spectrum files to generate empirical library.

random_preanalysis_seed
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``random_preanalysis_seed``
     - integer
     - 42
     - Set the random seed for the random selection of spectrum files to generate the empirical library.

ratios
------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ratios``
     - boolean
     - ``false``
     - Add the log2 ratios of the abundance values to the output.

ref_condition
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``ref_condition``
     - string
     - 
     - Experimental: Instead of all pairwise contrasts (default), uses the given condition name/number (corresponding to your experimental design) as a reference and creates pairwise contrasts against it.

reference_channel
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``reference_channel``
     - string
     - ``126``
     - The reference channel, e.g. for calculating ratios.

reindex_mzml
------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``reindex_mzml``
     - boolean
     - true
     - Force initial re-indexing of input mzML files. Also fixes some common mistakes in slightly incomplete/outdated mzMLs. (Default: true for safety)

reporter_mass_shift
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``reporter_mass_shift``
     - number
     - 0.002
     - Allowed shift (left to right) in Th from the expected position

rescore_range
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``rescore_range``
     - string
     - ``independent_run``
     - Rescoring for independent run, Sample or whole experiments

root_folder
-----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``root_folder``
     - string
     - 
     - Root folder in which the spectrum files specified in the SDRF/design are searched

run_fdr_cutoff
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``run_fdr_cutoff``
     - number
     - 0.1
     - FDR cutoff on PSM level (or peptide level; see Percolator options) *per run* before going into feature finding, map alignment and inference. This can be seen as a pre-filter. See

sage_processes
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``sage_processes``
     - integer
     - 1
     - Number of sage processes to be spawned.

scan_window
-----------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``scan_window``
     - integer
     - 8
     - Set the scan window radius to a specific value

scan_window_automatic
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``scan_window_automatic``
     - boolean
     - true
     - Choosing scan_window setting automatically

search_engines
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``search_engines``
     - string
     - ``comet``
     - A comma separated list of search engines to use (and combine). Valid: comet, msgf, sage

shuffle_max_attempts
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``shuffle_max_attempts``
     - integer
     - 30
     - Maximum nr. of attempts to lower the amino acid sequence identity between target and decoy for the shuffle algorithm

shuffle_sequence_identity_threshold
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``shuffle_sequence_identity_threshold``
     - number
     - 0.5
     - Target-decoy amino acid sequence identity threshold for the shuffle algorithm. if the sequence identity is above this threshold, shuffling is repeated. In case of repeated failure, individual amino acids are 'mutated' to produce a difference amino acid sequence.

skip_experimental_design_validation
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_experimental_design_validation``
     - boolean
     - 
     - Skip validation of experimental design.

skip_factor_validation
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_factor_validation``
     - boolean
     - 
     - Skip validation of factor columns.

skip_ms_validation
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_ms_validation``
     - boolean
     - 
     - Skip validation of mass spectrometry files.

skip_post_msstats
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_post_msstats``
     - boolean
     - 
     - Skip MSstats/MSstatsTMT for statistical post-processing?

skip_preliminary_analysis
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_preliminary_analysis``
     - boolean
     - false
     - Skip the preliminary analysis step, thus use the passed spectral library as-is insted of generating a local concensus library.

skip_rescoring
--------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_rescoring``
     - boolean
     - false
     - Skip PSM rescoring steps for specific cases, such as studying pure search engine results and search engine ranks

skip_table_plots
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``skip_table_plots``
     - boolean
     - false
     - Skip protein/peptide table plots with pmultiqc for large dataset.

species_genes
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``species_genes``
     - boolean
     - false
     - Instructs DIA-NN to add the organism identifier to the gene names

subset_max_train
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``subset_max_train``
     - integer
     - 300000
     - Only train an SVM on a subset of PSMs, and use the resulting score vector to evaluate the other PSMs. Recommended when analyzing huge numbers (>1 million) of PSMs. When set to 0, all PSMs are used for training as normal. This is a runtime vs. quality tradeoff. Default: 300,000

targeted_only
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``targeted_only``
     - boolean
     - true
     - Only looks for quantifiable features at locations with an identified spectrum. Set to false to include unidentified features so they can be linked and matched to identified ones (= match between runs). (default: 'true')

test_FDR
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``test_FDR``
     - number
     - 0.05
     - The FDR cutoff to be used during testing of the SVM.

top
---

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``top``
     - integer
     - 3
     - Calculate protein abundance from this number of proteotypic peptides (most abundant first; '0' for all, Default 3)

top_PSMs
--------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``top_PSMs``
     - integer
     - 1
     - Consider only the top X PSMs per spectrum to find the best PSM per peptide. 0 considers all.

trace_report_suffix
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``trace_report_suffix``
     - string
     - 
     - Suffix to add to the trace report filename. Default is the date and time in the format yyyy-MM-dd_HH-mm-ss.

train_FDR
---------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``train_FDR``
     - number
     - 0.05
     - The FDR cutoff to be used during training of the SVM.

unmatched_action
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``unmatched_action``
     - string
     - ``warn``
     - What to do when peptides are found that do not follow a unified set of rules (since search engines sometimes differ in their interpretation of them).

update_PSM_probabilities
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``update_PSM_probabilities``
     - boolean
     - false
     - [Bayesian-only; Experimental] Update PSM probabilities with their posteriors under consideration of the protein probabilities.

use_ols_cache_only
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``use_ols_cache_only``
     - boolean
     - 
     - Use cached version of the Ontology Lookup Service (OLS).

use_shared_peptides
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``use_shared_peptides``
     - boolean
     - true
     - [Ignored in Bayesian] Also use shared peptides during score aggregation to protein level

validate_ontologies
-------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``validate_ontologies``
     - boolean
     - 
     - Check that ontology terms in an input SDRF file exist.

validate_params
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``validate_params``
     - boolean
     - true
     - Boolean whether to validate parameters against the schema at runtime

variable_mods
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``variable_mods``
     - string
     - ``Oxidation (M)``
     - A comma-separated list of variable modifications with their Unimod name to be searched during database search

version
-------

.. list-table::
   :header-rows: 1
   :widths: 28 12 20 40

   * - Name
     - Type
     - Default
     - Description
   * - ``version``
     - boolean
     - 
     - Display version and exit.
