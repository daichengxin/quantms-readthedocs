Getting started
===============

This page helps new users run quantms for the first time and understand the basics.

Prerequisites
-------------

- A Linux or macOS machine with recent ``bash`` and ``Java 11+``
- One container runtime: ``docker`` (recommended), ``singularity`` or ``podman``
- `Nextflow <https://www.nextflow.io/>`__ installed and in ``PATH``

Install Nextflow (one-time)
---------------------------

.. code-block:: bash

   curl -s https://get.nextflow.io | bash
   mv nextflow ~/.local/bin/  # or /usr/local/bin

Run the built-in test (5–10 min)
--------------------------------

.. code-block:: bash

   nextflow run bigbio/quantms -r 1.6.0 -profile test_lfq,docker

This validates your setup end-to-end. See :doc:`usage` for more profiles.

Choose your analysis path
-------------------------

- If your data is DDA (data-dependent acquisition): see :doc:`dda`
- If your data is DIA (data-independent acquisition): see :doc:`dia`
- If you use isobaric labels (TMT/iTRAQ): see :doc:`iso`
- For label-free quantification (LFQ): see :doc:`lfq`

Prepare inputs
--------------

- Read accepted formats and minimal inputs: :doc:`formats`
- Build a proper FASTA (targets + contaminants; decoys optional for DDA): :doc:`protein_database`
- Ensure your SDRF/experimental design is complete: :doc:`usage`

Run a small pilot
-----------------

.. code-block:: bash

   # DDA (label-free) pilot
   nextflow run bigbio/quantms -r 1.6.0 \
     --input path/to/your.sdrf.tsv \
     --database path/to/proteome_plus_contaminants.fasta \
     -profile docker

What’s next
-----------

- Understand outputs and where to find tables and reports: :doc:`quantms_output`
- Statistical analysis with MSstats: :doc:`msstats`
- Quality control with pMultiQC: :doc:`pmultiqc`
- Parameter reference: :doc:`parameters`
- Concepts and acronyms: :doc:`glossary`


