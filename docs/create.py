import pydoc
import subprocess

import pypgx
import pypgx.api
from pypgx.api import core
from pypgx.cli import commands

submodules = ['core', 'genotype', 'pipeline', 'plot', 'utils']

credit = """
..
   This file was automatically generated by docs/create.py.
"""

pypgx_help = subprocess.run(['pypgx', '-h'], capture_output=True, text=True, check=True).stdout
pypgx_help = '\n'.join(['   ' + x for x in pypgx_help.splitlines()])

submodule_help = ''

for submodule in submodules:
    description = pydoc.getdoc(getattr(pypgx.api, submodule)).split('\n\n')[0].replace('\n', ' ')
    submodule_help += f'- **{submodule}** : {description}\n'

d = dict(credit=credit, pypgx_help=pypgx_help, submodule_help=submodule_help)

# -- README.rst ---------------------------------------------------------------

readme = """
{credit}
README
******

.. image:: https://badge.fury.io/py/pypgx.svg
    :target: https://badge.fury.io/py/pypgx

.. image:: https://readthedocs.org/projects/pypgx/badge/?version=latest
    :target: https://pypgx.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://anaconda.org/bioconda/pypgx/badges/version.svg
   :target: https://anaconda.org/bioconda/pypgx

.. image:: https://anaconda.org/bioconda/pypgx/badges/license.svg
   :target: https://github.com/sbslee/pypgx/blob/master/LICENSE

.. image:: https://anaconda.org/bioconda/pypgx/badges/downloads.svg
   :target: https://anaconda.org/bioconda/pypgx/files

.. image:: https://anaconda.org/bioconda/pypgx/badges/installer/conda.svg
   :target: https://conda.anaconda.org/bioconda

Introduction
============

The main purpose of the PyPGx package, which is completely free and open
source, is to provide a unified platform for pharmacogenomics (PGx) research.

The package is written in Python, and supports both command line interface
(CLI) and application programming interface (API) whose documentations are
available at the `Read the Docs <https://pypgx.readthedocs.io/en/latest/>`_.

PyPGx is compatible with both of the Genome Reference Consortium Human (GRCh)
builds, GRCh37 (hg19) and GRCh38 (hg38).

There are currently 58 pharmacogenes in PyPGx:

.. list-table::

   * - ABCB1
     - CACNA1S
     - CFTR
     - CYP1A1
     - CYP1A2
   * - CYP1B1
     - CYP2A6/CYP2A7
     - CYP2A13
     - CYP2B6/CYP2B7
     - CYP2C8
   * - CYP2C9
     - CYP2C19
     - CYP2D6/CYP2D7
     - CYP2E1
     - CYP2F1
   * - CYP2J2
     - CYP2R1
     - CYP2S1
     - CYP2W1
     - CYP3A4
   * - CYP3A5
     - CYP3A7
     - CYP3A43
     - CYP4A11
     - CYP4A22
   * - CYP4B1
     - CYP4F2
     - CYP17A1
     - CYP19A1
     - CYP26A1
   * - DPYD
     - F5
     - G6PD
     - GSTM1
     - GSTP1
   * - GSTT1
     - IFNL3
     - NAT1
     - NAT2
     - NUDT15
   * - POR
     - PTGIS
     - RYR1
     - SLC15A2
     - SLC22A2
   * - SLCO1B1
     - SLCO1B3
     - SLCO2B1
     - SULT1A1
     - TBXAS1
   * - TPMT
     - UGT1A1
     - UGT1A4
     - UGT2B7
     - UGT2B15
   * - UGT2B17
     - VKORC1
     - XPC
     -
     -

Your contributions (e.g. feature ideas, pull requests) are most welcome.

| Author: Seung-been "Steven" Lee
| Email: sbstevenlee@gmail.com
| License: MIT License

Installation
============

Following packages are required to run PyPGx:

.. list-table::
   :header-rows: 1

   * - Package
     - Anaconda
     - PyPI
   * - ``fuc``
     - ✅
     - ✅
   * - ``scikit-learn``
     - ✅
     - ✅
   * - ``openjdk``
     - ✅
     - ❌

There are various ways you can install PyPGx. The recommended way is via
conda (`Anaconda <https://www.anaconda.com/>`__):

.. code-block:: text

   $ conda install -c bioconda pypgx

Above will automatically download and install all the dependencies as well.
Alternatively, you can use pip (`PyPI <https://pypi.org/>`__) to install
PyPGx and all of its dependencies except ``openjdk`` (i.e. Java JDK must be
installed separately):

.. code-block:: text

   $ pip install pypgx

Finally, you can clone the GitHub repository and then install PyPGx locally:

.. code-block:: text

   $ git clone https://github.com/sbslee/pypgx
   $ cd pypgx
   $ pip install .

The nice thing about this approach is that you will have access to
development versions that are not available in Anaconda or PyPI. For example,
you can access a development branch with the ``git checkout`` command. When
you do this, please make sure your environment already has all the
dependencies installed.

Structural variation detection
==============================

Many pharmacogenes are known to have `structural variation (SV)
<https://pypgx.readthedocs.io/en/latest/glossary.html#structural-variation-
sv>`__ such as gene deletions, duplications, and hybrids. You can visit the
`Genes <https://pypgx.readthedocs.io/en/latest/genes.html>`__ page to see the
list of genes with SV.

Some of the SV events can be quite challenging to detect accurately with
next-generation sequencing (NGS) data due to misalignment of sequence reads
caused by sequence homology with other gene family members (e.g. CYP2D6 and
CYP2D7). PyPGx attempts to address this issue by training a `support vector
machine (SVM) <https://scikit-learn.org/stable/modules/generated/sk
learn.svm.SVC.html>`__-based multiclass classifier using the `one-vs-rest
strategy <https://scikit-learn.org/stable/modules/generated/sklearn.multi
class.OneVsRestClassifier.html>`__ for each gene for each GRCh build. Each
classifier is trained using copy number profiles of real NGS samples as well
as simulated ones.

You can plot copy number profile and allele fraction profile with PyPGx to
visually inspect SV calls. Below are CYP2D6 examples:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - SV Name
     - Profile
   * - Normal
     - .. image:: https://raw.githubusercontent.com/sbslee/pypgx-data/main/dpsv/GRCh37-CYP2D6-8.png
   * - DeletionHet
     - .. image:: https://raw.githubusercontent.com/sbslee/pypgx-data/main/dpsv/GRCh37-CYP2D6-1.png
   * - Duplication
     - .. image:: https://raw.githubusercontent.com/sbslee/pypgx-data/main/dpsv/GRCh37-CYP2D6-2.png
   * - Tandem3
     - .. image:: https://raw.githubusercontent.com/sbslee/pypgx-data/main/dpsv/GRCh37-CYP2D6-9.png
   * - Tandem2C
     - .. image:: https://raw.githubusercontent.com/sbslee/pypgx-data/main/dpsv/GRCh37-CYP2D6-7.png

GRCh37 vs. GRCh38
=================

When working with PGx data, it's not uncommon to encounter a situation
where you are handling GRCh37 data in one project but GRCh38 in another. You
may be tempted to use tools like ``LiftOver`` to convert GRCh37 to GRCh38, or
vice versa, but deep down you know it's going to be a mess (and please don't
do this). The good news is, PyPGx supports both of the builds!

In many of the PyPGx actions, you can simply indicate which human genome
build to use. For example, you can use ``assembly`` for the API and
``--assembly`` for the CLI. **Note that GRCh37 will always be the default.**
Below is an example of using the API:

.. code:: python3

    >>> import pypgx
    >>> pypgx.list_variants('CYP2D6', alleles=['*4'], assembly='GRCh37')
    ['22-42524947-C-T']
    >>> pypgx.list_variants('CYP2D6', alleles=['*4'], assembly='GRCh38')
    ['22-42128945-C-T']

However, there is one important caveat to consider if your sequencing data is
GRCh38. That is, sequence reads must be aligned only to the main contigs
(i.e. ``chr1``, ``chr2``, ..., ``chrX``, ``chrY``), and not to the
alternative (ALT) contigs such as ``chr1_KI270762v1_alt``. This is because
the presence of ALT contigs reduces the sensitivity of variant calling
and many other analyses including SV detection. Therefore, if you have
sequencing data in GRCh38, make sure it's aligned to the main contigs only.

The only exception to above rule is the GSTT1 gene, which is located on
``chr22`` for GRCh37 but on ``chr22_KI270879v1_alt`` for GRCh38. This gene is
known to have an extremely high rate of gene deletion polymorphism in the
population and thus requires SV analysis. Therefore, if you are interested in
genotyping this gene with GRCh38 data, then you must include that contig
when performing read alignment. To this end, you can easily filter your
reference FASTA file before read alignment so that it only contains the main
contigs plus the ALT contig. If you don't know how to do this, here's one way
using the ``fuc`` program (which should have already been installed along
with PyPGx):

.. code-block:: text

    $ cat contigs.list
    chr1
    chr2
    ...
    chrX
    chrY
    chr22_KI270879v1_alt
    $ fuc fa-filter in.fa --contigs contigs.list > out.fa

Archive file, semantic type, and metadata
=========================================

In order to efficiently store and transfer data, PyPGx uses the ZIP archive
file format (``.zip``) which supports lossless data compression. Each archive
file created by PyPGx has a metadata file (``metadata.txt``) and a data file
(e.g. ``data.tsv``, ``data.vcf``). A metadata file contains important
information about the data file within the same archive, which is expressed
as pairs of ``=``-separated keys and values (e.g. ``Assembly=GRCh37``):

.. list-table::
    :widths: 20 40 40
    :header-rows: 1

    * - Metadata
      - Description
      - Examples
    * - ``Assembly``
      - Reference genome assembly.
      - ``GRCh37``, ``GRCh38``
    * - ``Control``
      - Control gene.
      - ``VDR``, ``chr1:10000-20000``
    * - ``Gene``
      - Target gene.
      - ``CYP2D6``, ``GSTT1``
    * - ``Platform``
      - Genotyping platform.
      - ``WGS``, ``Targeted``, ``Chip``
    * - ``Program``
      - Name of the phasing program.
      - ``Beagle``, ``SHAPEIT``
    * - ``Samples``
      - Samples used for inter-sample normalization.
      - ``NA07000,NA10854,NA11993``
    * - ``SemanticType``
      - Semantic type of the archive.
      - ``CovFrame[CopyNumber]``, ``Model[CNV]``

Notably, all archive files have defined semantic types, which allows us to
ensure that the data that is passed to a PyPGx command (CLI) or method (API)
is meaningful for the operation that will be performed. Below is a list of
currently defined semantic types:

- ``CovFrame[CopyNumber]``
    * CovFrame for storing target gene's per-base copy number which is computed from read depth with control statistics.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``, ``Platform``, ``Control``, ``Samples``.
- ``CovFrame[DepthOfCoverage]``
    * CovFrame for storing read depth for all target genes with SV.
    * Requires following metadata: ``Assembly``, ``SemanticType``, ``Platform``.
- ``CovFrame[ReadDepth]``
    * CovFrame for storing read depth for single target gene.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``, ``Platform``.
- ``Model[CNV]``
    * Model for calling CNV in target gene.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``, ``Control``.
- ``SampleTable[Alleles]``
    * TSV file for storing target gene's candidate star alleles for each sample.
    * Requires following metadata: ``Platform``, ``Gene``, ``Assembly``, ``SemanticType``, ``Program``.
- ``SampleTable[CNVCalls]``
    * TSV file for storing target gene's CNV call for each sample.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``, ``Control``.
- ``SampleTable[Genotypes]``
    * TSV file for storing target gene's genotype call for each sample.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``.
- ``SampleTable[Phenotypes]``
    * TSV file for storing target gene's phenotype call for each sample.
    * Requires following metadata: ``Gene``, ``SemanticType``.
- ``SampleTable[Results]``
    * TSV file for storing various results for each sample.
    * Requires following metadata: ``Gene``, ``Assembly``, ``SemanticType``.
- ``SampleTable[Statistcs]``
    * TSV file for storing control gene's various statistics on read depth for each sample. Used for converting target gene's read depth to copy number.
    * Requires following metadata: ``Control``, ``Assembly``, ``SemanticType``, ``Platform``.
- ``VcfFrame[Consolidated]``
    * VcfFrame for storing target gene's consolidated variant data.
    * Requires following metadata: ``Platform``, ``Gene``, ``Assembly``, ``SemanticType``, ``Program``.
- ``VcfFrame[Imported]``
    * VcfFrame for storing target gene's raw variant data.
    * Requires following metadata: ``Platform``, ``Gene``, ``Assembly``, ``SemanticType``.
- ``VcfFrame[Phased]``
    * VcfFrame for storing target gene's phased variant data.
    * Requires following metadata: ``Platform``, ``Gene``, ``Assembly``, ``SemanticType``, ``Program``.

Phenotype prediction
====================

Many genes in PyPGx have a genotype-phenotype table available from the
Clinical Pharmacogenetics Implementation Consortium (CPIC) or
the Pharmacogenomics Knowledge Base (PharmGKB). PyPGx uses these tables to
perform phenotype prediction with one of the two methods:

- Method 1. Simple diplotype-phenotype mapping: This method directly uses the
  diplotype-phenotype mapping as defined by CPIC or PharmGKB. Using the
  CYP2B6 gene as an example, the diplotypes \*6/\*6, \*1/\*29, \*1/\*2,
  \*1/\*4, and \*4/\*4 correspond to Poor Metabolizer, Intermediate
  Metabolizer, Normal Metabolizer, Rapid Metabolizer, and Ultrarapid
  Metabolizer.
- Method 2. Summation of haplotype activity scores: This method uses a
  standard unit of enzyme activity known as an activity score. Using the
  CYP2D6 gene as an example, the fully functional reference \*1 allele is
  assigned a value of 1, decreased-function alleles such as \*9 and \*17
  receive a value of 0.5, and nonfunctional alleles including \*4 and \*5
  have a value of 0. The sum of values assigned to both alleles constitutes
  the activity score of a diplotype. Consequently, subjects with \*1/\*1,
  \*1/\*4, and \*4/\*5 diplotypes have an activity score of 2 (Normal
  Metabolizer), 1 (Intermediate Metabolizer), and 0 (Poor Metabolizer),
  respectively.

Please visit the `Genes <https://pypgx.readthedocs.io/en/latest/
genes.html>`__ page to see the list of genes with a genotype-phenotype
table and each of their prediction method.

To perform phenotype prediction with the API, you can use the
``pypgx.predict_phenotype`` method:

.. code:: python3

    >>> import pypgx
    >>> pypgx.predict_phenotype('CYP2D6', '*4', '*5')   # Both alleles have no function
    'Poor Metabolizer'
    >>> pypgx.predict_phenotype('CYP2D6', '*5', '*4')   # The order of alleles does not matter
    'Poor Metabolizer'
    >>> pypgx.predict_phenotype('CYP2D6', '*1', '*22')  # *22 has uncertain function
    'Indeterminate'
    >>> pypgx.predict_phenotype('CYP2D6', '*1', '*1x2') # Gene duplication
    'Ultrarapid Metabolizer'

To perform phenotype prediction with the CLI, you can use the
``call-phenotypes`` command. It takes a ``SampleTable[Genotypes]`` file as
input and outputs a ``SampleTable[Phenotypes]`` file:

.. code-block:: text

   $ pypgx call-phenotypes genotypes.zip phenotypes.zip

Getting help
============

For detailed documentations on the CLI and API, please refer to the
`Read the Docs <https://pypgx.readthedocs.io/en/latest/>`_.

For getting help on the CLI:

.. code-block:: text

   $ pypgx -h

{pypgx_help}

For getting help on a specific command (e.g. call-genotypes):

.. code-block:: text

   $ pypgx call-genotypes -h

Below is the list of submodules available in the API:

{submodule_help}
For getting help on a specific submodule (e.g. ``utils``):

.. code:: python3

   >>> from pypgx.api import utils
   >>> help(utils)

For getting help on a specific method (e.g. ``predict_phenotype``):

.. code:: python3

   >>> import pypgx
   >>> help(pypgx.predict_phenotype)

In Jupyter Notebook and Lab, you can see the documentation for a python
function by hitting ``SHIFT + TAB``. Hit it twice to expand the view.

CLI examples
============

We can print the metadata of an archive file:

.. code-block:: text

    $ pypgx print-metadata grch37-depth-of-coverage.zip

Above will print:

.. code-block:: text

    Assembly=GRCh37
    SemanticType=CovFrame[DepthOfCoverage]
    Platform=WGS

We can run the NGS pipeline for the *CYP2D6* gene:

.. code-block:: text

    $ pypgx run-ngs-pipeline \\
    CYP2D6 \\
    grch37-CYP2D6-pipeline \\
    --variants grch37-variants.vcf.gz \\
    --depth-of-coverage grch37-depth-of-coverage.zip \\
    --control-statistics grch37-control-statistics-VDR.zip

Above will create a number of archive files:

.. code-block:: text

    Saved VcfFrame[Imported] to: grch37-CYP2D6-pipeline/imported-variants.zip
    Saved VcfFrame[Phased] to: grch37-CYP2D6-pipeline/phased-variants.zip
    Saved VcfFrame[Consolidated] to: grch37-CYP2D6-pipeline/consolidated-variants.zip
    Saved SampleTable[Alleles] to: grch37-CYP2D6-pipeline/alleles.zip
    Saved CovFrame[ReadDepth] to: grch37-CYP2D6-pipeline/read-depth.zip
    Saved CovFrame[CopyNumber] to: grch37-CYP2D6-pipeline/copy-number.zip
    Saved SampleTable[CNVCalls] to: grch37-CYP2D6-pipeline/cnv-calls.zip
    Saved SampleTable[Genotypes] to: grch37-CYP2D6-pipeline/genotypes.zip
    Saved SampleTable[Phenotypes] to: grch37-CYP2D6-pipeline/phenotypes.zip
    Saved SampleTable[Results] to: grch37-CYP2D6-pipeline/results.zip

API examples
============

We can obtain allele function for the *CYP2D6* gene:

.. code:: python3

    >>> import pypgx
    >>> pypgx.get_function('CYP2D6', '*1')
    'Normal Function'
    >>> pypgx.get_function('CYP2D6', '*4')
    'No Function'
    >>> pypgx.get_function('CYP2D6', '*22')
    'Uncertain Function'
    >>> pypgx.get_function('CYP2D6', '*140')
    'Unknown Function'

We can predict phenotype for the *CYP2D6* gene based on two haplotype calls:

.. code:: python3

    >>> import pypgx
    >>> pypgx.predict_phenotype('CYP2D6', '*4', '*5')   # Both alleles have no function
    'Poor Metabolizer'
    >>> pypgx.predict_phenotype('CYP2D6', '*5', '*4')   # The order of alleles does not matter
    'Poor Metabolizer'
    >>> pypgx.predict_phenotype('CYP2D6', '*1', '*22')  # *22 has uncertain function
    'Indeterminate'
    >>> pypgx.predict_phenotype('CYP2D6', '*1', '*1x2') # Gene duplication
    'Ultrarapid Metabolizer'
""".format(**d)

readme_file = f'{core.PROGRAM_PATH}/README.rst'

with open(readme_file, 'w') as f:
    f.write(readme.lstrip())

# -- cli.rst -----------------------------------------------------------------

cli = """
{credit}

CLI
***

Introduction
============

This page describes the command line interface (CLI) for PyPGx.

For getting help on the CLI:

.. code-block:: text

   $ pypgx -h

{pypgx_help}

For getting help on a specific command (e.g. call-genotypes):

.. code-block:: text

   $ pypgx call-genotypes -h

""".format(**d)

for command in commands:
    s = f'{command}\n'
    s += '=' * (len(s)-1) + '\n'
    s += '\n'
    s += '.. code-block:: text\n'
    s += '\n'
    s += f'   $ pypgx {command} -h\n'
    command_help = subprocess.run(['pypgx', command, '-h'], capture_output=True, text=True, check=True).stdout
    command_help = '\n'.join(['   ' + x for x in command_help.splitlines()])
    s += command_help + '\n'
    s += '\n'
    cli += s

cli_file = f'{core.PROGRAM_PATH}/docs/cli.rst'

with open(cli_file, 'w') as f:
    f.write(cli.lstrip())

# -- api.rst -----------------------------------------------------------------

api = """
{credit}
API
***

Introduction
============

This page describes the application programming interface (API) for PyPGx.

Below is the list of submodules available in the API:

{submodule_help}

For getting help on a specific submodule (e.g. utils):

.. code:: python3

   from pypgx.api import utils
   help(utils)

""".format(**d)

for submodule in submodules:
    s = f'{submodule}\n'
    s += '=' * (len(s)-1) + '\n'
    s += '\n'
    s += f'.. automodule:: pypgx.api.{submodule}\n'
    s += '   :members:\n'
    s += '\n'
    api += s

with open(f'{core.PROGRAM_PATH}/docs/api.rst', 'w') as f:
    f.write(api.lstrip())

# -- sdk.rst -----------------------------------------------------------------

sdk = """
{credit}
SDK
***

Introduction
============

This page describes the software development kit (SDK) for PyPGx.

utils
=====

.. automodule:: pypgx.sdk.utils
   :members:

""".format(**d)

with open(f'{core.PROGRAM_PATH}/docs/sdk.rst', 'w') as f:
    f.write(sdk.lstrip())
