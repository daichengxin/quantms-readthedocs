Quickstart
==========

Run a complete small example with Docker in minutes.

.. code-block:: bash

   # 1) Install Nextflow (once)
   curl -s https://get.nextflow.io | bash
   mv nextflow ~/.local/bin/

   # 2) Run quantms test workflow
   nextflow run bigbio/quantms -r 1.6.0 -profile test_lfq,docker

Key outputs
-----------

- See :doc:`quantms_output` for folder structure and tables
- See :doc:`pmultiqc` for QC report
- See :doc:`msstats` for downstream statistics

Next steps
----------

- Switch to your own SDRF and FASTA following :doc:`getting_started` and :doc:`formats`
- Tune parameters in :doc:`parameters`


