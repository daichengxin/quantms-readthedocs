Tutorials
=========

Beginner: DDA LFQ from SDRF
---------------------------

1. Prepare SDRF and FASTA as in :doc:`getting_started`
2. Run:

   .. code-block:: bash

      nextflow run bigbio/quantms -r 1.6.0 \
        --input project.sdrf.tsv \
        --database proteome_plus_contaminants.fasta \
        -profile docker

3. Inspect outputs: :doc:`quantms_output`
4. MSstats differential analysis: :doc:`msstats`

Intermediate: DIA library-free with DIA-NN
------------------------------------------

1. Build FASTA with UniProt + contaminants (use description variant for DIA): :doc:`protein_database`
2. Run:

   .. code-block:: bash

      nextflow run bigbio/quantms -r 1.6.0 \
        --input project.sdrf.tsv \
        --database proteome_plus_contaminants.fasta \
        --acquisition_method dia \
        -profile docker

3. Review DIA-NN settings: :doc:`dia`
4. QC with :doc:`pmultiqc`

Advanced: Rescoring and model choices
-------------------------------------

- Learn about rescoring options and models: :doc:`rescoring`
- Consider deep-learning predictors and model selection


