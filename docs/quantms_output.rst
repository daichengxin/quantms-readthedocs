quantms outputs
===============

bigbio/quantms: Output
======================

.. note:: The structured output layout described here was introduced in quantms version 1.5.0. See the `release notes <https://github.com/bigbio/quantms/releases/tag/1.5.0>`__.

Introduction
------------

This document describes the output produced by the pipeline. Most plots are taken from the pMultiQC report, which summarises results at the end of the pipeline.

The directories listed below will be created in the results directory after the pipeline has finished. All paths are relative to the top-level results directory.

Pipeline overview
-----------------

The pipeline is built using `Nextflow <https://www.nextflow.io/>`__ and processes data using the following steps for DDA-LFQ and DDA-ISO data:

1. (optional) Conversion of spectra data to indexedMzML: Using ThermoRawFileParser if Thermo Raw or using OpenMS' FileConverter if just an index is missing
2. (optional) Decoy database generation for the provided DB (fasta) with OpenMS
3. Database search with either MSGF+ and/or Comet through OpenMS adapters
4. (optional) Performs LC-MS predictors such as MS²PIP and DeepLC to add new peptide spectrum match (PSM) features by MS2Rescore
5. (optional) Add spectrum signal-to-noise (SNR) features for Percolator rescore
6. (optional) Merge different MS runs by samples or whole projects
7. PSM rescoring Percolator
8. If multiple search engines were chosen, the results are combined with OpenMS' ConsensusID
9. If multiple search engines were chosen, a combined FDR is calculated
10. Single run PSM/Peptide-level FDR filtering
11. If localization of modifications was requested, Luciphor2 is applied.
12. (**DDA-LFQ**) Protein inference and label-free quantification based on spectral counting or MS1 feature detection, alignment and integration with OpenMS' ProteomicsLFQ. Performs an additional experiment-wide FDR filter on protein (and if requested peptide/PSM-level).
13. (**DDA-ISO**) Extracts and normalizes isobaric labeling
14. (**DDA-ISO**) Protein inference using the OpenMS ProteinInference tool. In addition, protein FDR filtering is performed in this step for Isobaric datasets (TMT, iTRAQ).
15. (**DDA-ISO**) Protein Quantification
16. Generation of QC reports using pMultiQC, a library for QC proteomics data analysis.

For DIA-LFQ experiments, the workflow is different:

1. RAW data is converted to mzML using the ThermoRawFileParser
2. DIA-NN is used for identification and quantification of the peptides and proteins
3. Generation of output files
4. Generation of QC reports using pMultiQC, a library for QC proteomics data analysis.

As an example, a rough visualization of the DDA identification subworkflow can be seen here:

!`quantms LFQ workflow <./images/id-dda-pipeline.png>`_

.. _output-structure:

Output structure
----------------

Output will be saved to the folder defined by the parameter `--outdir`. Each step of the workflow exports different files and reports with the specific data, peptide identifications, protein quantifications, etc. Most of the pipeline outputs are `HUPO-PSI <https://www.psidev.info/>`_ standard file formats:

- `mzML <https://www.psidev.info/mzML>`_: The mzML format is an open, XML-based format for mass spectrometer output files.
- `mzTab <https://www.psidev.info/mztab>`_: mzTab is intended as a lightweight tab-delimited file format to export peptide and protein identification/quantification results.

Default Output Structure
------------------------

By default, quantms organizes output files in a structured way, with specific directories for different types of outputs. The structure varies slightly depending on the workflow type (DIA, ISO, LFQ, etc.), but follows a consistent organization pattern.

Common directories across all workflows:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `pipeline_info/`: Contains Nextflow pipeline information, execution reports, and software versions
- `sdrf/`: Contains SDRF files, OpenMS configs, and other experimental design files
- `pmultiqc/`: Contains pMultiQC reports and visualizations
  - `multiqc_data/`: Raw data used by pMultiQC
  - `multiqc_plots/`: Visualizations in different formats (png, svg, pdf)

DIA workflow output structure:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    results_dia/
    ├── pipeline_info/             # Nextflow pipeline information
    ├── sdrf/                      # SDRF files and configs
    ├── spectra/                   # Spectra-related data (only present if --mzml_features is enabled)
    │   └── thermorawfileparser/   # Converted raw files
    ├── quant_tables/              # Quantification tables and results
    ├── msstats/                   # MSstats processed results
    └── pmultiqc/                  # pMultiQC reports
        ├── multiqc_plots/
        └── multiqc_data/

ISO quantification workflow output structure:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    results_iso/
    ├── pipeline_info/             # Nextflow pipeline information
    ├── sdrf/                      # SDRF files and configs
    ├── quant_tables/              # Quantification tables and results
    ├── msstats/                   # MSstats processed results
    └── pmultiqc/                  # pMultiQC reports
        ├── multiqc_data/
        └── multiqc_plots/

LFQ quantification workflow output structure:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    results_lfq/
    ├── pipeline_info/             # Nextflow pipeline information
    ├── sdrf/                      # SDRF files and configs
    ├── spectra/                   # Spectra-related data (only present if --mzml_features is enabled)
    │   └── mzml_statistics/       # Statistics about mzML files
    ├── quant_tables/              # Quantification tables and results
    ├── msstats/                   # MSstats processed results
    └── pmultiqc/                  # pMultiQC reports
        ├── multiqc_data/
        └── multiqc_plots/

LFQ identification workflow output structure:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    results_lfq_dda_id/
    ├── pipeline_info/             # Nextflow pipeline information
    ├── sdrf/                      # SDRF files and configs
    ├── spectra/                   # Spectra-related data (only present if --mzml_features is enabled)
    │   └── mzml_statistics/       # Statistics about mzML files
    ├── psm_tables/                # PSM tables from identification pipeline
    └── pmultiqc/                  # pMultiQC reports
        └── multiqc_data/

Localize workflow output structure:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    results_localize/
    ├── pipeline_info/             # Nextflow pipeline information
    ├── sdrf/                      # SDRF files and configs
    ├── quant_tables/              # Quantification tables and results
    └── pmultiqc/                  # pMultiQC reports
        ├── multiqc_plots/
        └── multiqc_data/

Verbose Output Structure
------------------------

For more detailed output with all intermediate files, you can use the verbose output configuration by providing the config parameter `-c verbose_modules` when running the pipeline. This will use the `verbose_modules` configuration. It can be useful for debugging or detailed analysis of the pipeline's steps.

The verbose output structure preserves all intermediate files and organizes them in a more detailed directory structure. Here's an example of the verbose output structure for an LFQ analysis:

.. code-block:: text

    results_lfq_verbose/
    ├── pipeline_info/
    ├── sdrf/
    ├── spectra/
    ├── quant_tables/
    ├── msstats/
    └── pmultiqc/

Key Output Files
----------------

Depending on the workflow type, the main output files will be found in the following directories:

- `quant_tables/`: Contains all quantification results including mzTab files, MSstats input files, and other quantification tables
- `psm_tables/`: Contains PSM-level results from the identification pipeline in parquet format
- `msstats/`: Contains MSstats processed results and reports
- `pmultiqc/`: Contains quality control reports and visualizations

The specific files include:

- DDA-LFQ quantification results:
  - ``quant_tables/out.consensusXML`` - `consensusXML <https://github.com/OpenMS/OpenMS/blob/develop/share/OpenMS/SCHEMAS/ConsensusXML_1_7.xsd>`_ format with quantification data
  - ``quant_tables/msstats_in.csv`` - see :ref:`msstats-ready-quantity-tables` quantity tables
  - ``quant_tables/out_triqler.tsv`` - see :doc:`triqler` input format
  - ``quant_tables/out.mzTab`` - `mzTab <https://www.psidev.info/mztab>`_ format with identifications and quantities

- DDA-ISO quantification results:
  - ``quant_tables/out.mzTab`` - `mzTab <https://www.psidev.info/mztab>`_ format with identifications and quantities
  - ``quant_tables/peptide_out.csv`` - see :ref:`tab-based-openms-formats` peptide quantities
  - ``quant_tables/protein_out.csv`` - see :ref:`tab-based-openms-formats` protein quantities
  - ``quant_tables/out_msstats_in.csv`` - see :ref:`msstats-ready-quantity-tables` quantity tables

- DIA-LFQ quantification results:
  - ``quant_tables/diann_report.tsv`` - DIA-NN main report with peptide and protein quantification
  - ``quant_tables/diann_report.pr_matrix.tsv`` - Protein quantification matrix from DIA-NN
  - ``quant_tables/diann_report.pg_matrix.tsv`` - Protein group quantification matrix from DIA-NN
  - ``quant_tables/diann_report.peptide_matrix.tsv`` - Peptide quantification matrix from DIA-NN
  - ``quant_tables/diann_report.lib`` - DIA-NN spectral library
  - ``quant_tables/out_msstats_in.csv`` - see :ref:`msstats-ready-quantity-tables` quantity tables

- MSstats-processed results:
  - ``msstats/out_msstats.mzTab`` - see :ref:`msstats-processed-mztab` mzTab

Output description
------------------

Nextflow pipeline info
----------------------

`Nextflow <https://www.nextflow.io/docs/latest/tracing.html>`__ provides excellent functionality for generating various reports relevant to the running and execution of the pipeline. This will allow you to troubleshoot errors with the running of the pipeline, and also provide you with other information such as launch commands, run times and resource usage.

File types
----------

Spectra
~~~~~~~

Quantms main format for spectra is the open `mzML <https://www.psidev.info/mzML>`_ format. However, it also supports Thermo raw files through conversion with
ThermoRawFileParser. Mixed inputs should be possible but are untested. Conversion results can be cached if run locally or outputted to results.
Mismatches between file extensions in the design and on disk can be corrected through parameters.

Protein database
~~~~~~~~~~~~~~~~

The input protein database needs to be in standard fasta format. We recommend removing stop codons `*` in a way that is suitable to your analysis to avoid
different handling between peptide search engines.

Identifications
~~~~~~~~~~~~~~~

Intermediate output for the PSM/peptide-level filtered identifications per raw/mzML file happens in OpenMS'
internal `idXML <https://github.com/OpenMS/OpenMS/blob/develop/share/OpenMS/SCHEMAS/IdXML_1_5.xsd>`_ format. quantms also provide `parquet <https://github.com/bigbio/quantms.io/blob/dev/docs/psm.rst>`_ output format in identification subworkflow.
Only for DDA currently.

Quantities
~~~~~~~~~~

Depending on the mode, quantms reports its outputs for quantities in different folders and formats, see :ref:`output-structure`.

ConsensusXML
~~~~~~~~~~~~

A `consensusXML <https://github.com/OpenMS/OpenMS/blob/develop/share/OpenMS/SCHEMAS/ConsensusXML_1_7.xsd>`_ file as the closest representation of the internal data
structures generated by OpenMS. Helpful for debugging and downstream processing with OpenMS tools.

Tab-based OpenMS formats
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the consensusXML and idXML formats, OpenMS generates other formats that can help the downstream analysis of the quantms results. DDA-LFQ only.

- peptide_out.tsv: The peptide output (peptide_out.tsv) from `ProteinQuantifier <https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_ProteinQuantifier.html>`_ contains a peptide table with the corresponding quantification data.
- protein_out.tsv: The protein output (protein_out.tsv) from `ProteinQuantifier <https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_ProteinQuantifier.html>`_ contains the protein information including quantification values.

MSstats-ready quantity tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MSstats output is generated for all three pipelines DDA-LFQ, DDA-ISO and DIA-LFQ. A simple tsv file ready to be read by the
OpenMStoMSstats function of the MSstats R package. It should hold the same quantities as the consensusXML but rearranged in a "long" table format with additional
information about the experimental design used by MSstats.

Triqler
~~~~~~~

Output to be used as input in Triqler has similar information in a tsv format as the output for MSstats. Additionally, it contains quantities for
decoy identifications and search engine scores.