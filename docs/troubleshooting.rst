Troubleshooting
===============

Common setup issues
-------------------

- Nextflow not found: ensure it’s on ``PATH``; see :doc:`getting_started`.
- Container runtime problems: test with ``docker run hello-world`` or use a different profile (``singularity``/``podman``).
- Java version: run ``java -version``; install Java 11+.

Pipeline run errors
-------------------

- Input errors (SDRF/paths): validate your SDRF and use ``--root_folder`` if needed. See :doc:`usage`.
- FASTA issues: ensure FASTA exists and matches recommendations. See :doc:`protein_database`.
- DIA runs: do not include decoys in FASTA; DIA-NN handles decoys internally. See :doc:`dia`.

Sphinx docs build (developers)
------------------------------

- If docs fail to build locally, recreate the venv and install requirements: see ``requirements.txt``.
- For warnings about ``_static`` missing, create ``docs/_static``.

Getting help
------------

- Open an issue: https://github.com/bigbio/quantms/issues
- Join the nf-core Slack ``#quantms`` channel.


