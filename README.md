# Social-Ecologically Integrated Urban River Corridors - Assessment Framework

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

This repository contains GIS scripts and workflows used in the social-ecological integration assessment of the river Dâmbovița, Bucharest, as part of the research "Integrated Urban River Corridors: Spatial Design for Social-Ecological Resilience in Bucharest and Beyond" ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)), conducted at TU Delft under the supervision of Prof. Arjan van Timmeren, Prof. Machiel van Dorst, and [Dr. Jorge Gil](https://github.com/jorgegil) and with contributions from Dr. Daniele Cannatella and Vincent Babes.

The assessment framework consists of [an indicator system](#Indicator-system) and a [method of social-ecological integration assessment](#Method-of-social-ecological-integration-assessment) applied as a geospatial analysis of [Corridor Segments (CS) as analytical units of an Urban River Corridor (URC)](#Spatial-delineation) in question.

The spatial analyses used in the application of the assessment framework on URC Dambovita were conducted in ArcGIS. Therefore, most workflows are either available as Python scripts exported from ArcMap's ModelBuilder or are provided in the form of detailed workflow descriptions. [We are currently translating these workflows](#Future-directions) into open source GIS software. [Contributions](#How-to-contribute) are especially encouraged to that end.

## Indicator system

Informed by an overview of current approaches to urban river assessment in urban planning and design, landscape architecture and landscape ecology, and structured by the four properties of URCs identified in Forgaci ([2018](https://doi.org/10.7480/abe.2018.31))—namely, Connectivity, Spatial capacity, Integration, and Multiscalarity—, the assessment framework comprises a system of social and ecological indicators of connectivity (with the sub-categories of lateral, longitudinal, and vertical connectivity) and spatial capacity (with the sub-categories of diversity, quality, and composition). The full list of indicators of the indicator system is available at https://doi.org/10.4121/15126795.

![Social-Ecological Integration Assessment Framework](fig/framework.png "Social-Ecological Integration Assessment Framework")

## Method of social-ecological integration assessment

The method makes use of a mirrored assessment chart which confronts the results from the analysis of social and ecological indicators of corresponding sub-categories. For instance, ecological spatial diversity measured in the level of biodiversity of local habitats is confronted with social spatial diversity measured through the multifunctionality of local public spaces. The assessment is carried out on corridor segment (CS) scale and summarised on the scale of the entire URC. As a planning or design decision tool, this method of assessment highlights key areas of intervention where a minimum desirable goal of social-ecological integration can be achieved. The following figure shows how scores recorded for a CS on the mirrored assessment chart can lead to decisions on where strategic interventions (marked with '+') can increase social-ecological integration. The script `assess.R` in this repository generates a table of minimum values and highlights areas of improvement towards social-ecological integration for the case study URC Dambovita.

![](fig/assessment.png)

## Spatial delineation

As depicted in the figure below, the delineation of an URC, that is, its **outer boundary**, its **corridor segments** and **the river space**, is carried out as follows:

1.  The edges of the river valley are determined, for instance, from a digital elevation model.
2.  The main roads that are parallel, adjacent to, and outside the river valley are identified as the **outer boundary** of the URC. The ends of the corridor are determined by municipal or metropolitan administrative boundaries in such a way that continuity with the surrounding (non-urbanized) landscape is ensured.
3.  The outer boundary is adjusted with a walkshed (i.e. the area accessible within a walking distance) of 500m calculated from both edges of the river.
4.  After the outer boundary of the URC is delineated, **corridor segments** (CSs) are determined by dividing the URC along major transversal traffic lines. This way, spatially continuous units (i.e. uninterrupted by traffic barriers) are identified along the URC. The assumption made in this step is that urban areas between two major crossings have distinct morphological characteristics.
5.  The **river space** is defined as the open space surrounding the river and delineated by the first line of buildings.

![](fig/delineation.jpg)

To account for local characteristics, this method of delineation requires a qualitative judgement of the morphological particularities of the site in question. This is especially the case for corridor segment delineation, where variations in distance between major crossings may lead to an unbalanced subdivision of the corridor. If two consecutive major crossing are too close to each other (the case of narrow rivers with many crossings), adjacent segments with similar morphological characteristics can be merged. If consecutive crossings are too far from each other (the case of wide rivers), then the URC can be further subdivided based on changes in morphological characteristics of the oversized corridor segment.

## Application on URC Dâmbovița, Bucharest

The assessment was carried out on a selection of indicators on URC Dâmbovița, Bucharest. An example of the results for one indicator is illustrated below. [`URC-D-analyses/`](URC-D-analyses/) contains scripts and workflows describing analyses carried out in ArcMap v10.2 and v10.3. [`URC-D-data/`](URC-D-data/) contains the geospatial data used for the analyses as well as the assessment results. For some indicators selected for assessment, the analytical workflows were saved with ArcMap's ModelBuilder. For indicators where the workflow was not recorded in an ArcMap model, a detailed description of the analytical steps was provided in a text file.

To reproduce the analyses for URC Dâmbovița, follow these steps:

1. For each indicator in `URC-D-analyses/`, depending on the format in which the workflow is available, do one of the following:
    - import the toolbox `URC-D.tbx` and run the models in ArcMap
    - run the Python script
    - follow the steps described in [Appendix E](https://journals.open.tudelft.nl/plugins/generic/pdfJsViewer/pdf.js/web/viewer.html?file=https%3A%2F%2Fjournals.open.tudelft.nl%2Fabe%2Farticle%2Fdownload%2F3275%2F3447%2F8841#9789463661096-TXT.indd%3A.322609%3A59470) of Integrated Urban River Corridors ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)) in another GIS software.

2. Translate the values resulting from analysis into standardized scores according to the indicator definitions described in https://doi.org/10.4121/15126795 and add the scores to the score chart. In this repository, scores were stored in [`URC-D-assessment-all.csv`](URC-D-data/URC-D-assessment-all.csv)

3. Run the script `assess.R` to determine the minimum desirable goal and to identify potentials of improved social-ecological integration in each corridor segment. In this repository, results of the assessment were stored in [`URC-D-assessment-minimum.csv`](URC-D-data/URC-D-assessment-minimum.csv)

>![Results for indicator A121c](fig/A121c.png "Results for indicator A121c") Accessibility from public transport stops (A121c Accessibility – visitors), as an example of a connectivity indicator applied on URC Dâmbovița and detailed on corridor segment CS03.

Detailed descriptions of the workflows and software used in the application of each indicator are also available in [Appendix E](https://journals.open.tudelft.nl/plugins/generic/pdfJsViewer/pdf.js/web/viewer.html?file=https%3A%2F%2Fjournals.open.tudelft.nl%2Fabe%2Farticle%2Fdownload%2F3275%2F3447%2F8841#9789463661096-TXT.indd%3A.322609%3A59470) of Integrated Urban River Corridors ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)). The data set with the assessment results for URC Dâmbovița can be found at <https://doi.org/10.4121/15126795>. The assessment framework and its application are described in detail in [Chapters 5 and 6](https://journals.open.tudelft.nl/plugins/generic/pdfJsViewer/pdf.js/web/viewer.html?file=https%3A%2F%2Fjournals.open.tudelft.nl%2Fabe%2Farticle%2Fdownload%2F3275%2F3447%2F8841#9789463661096-TXT.indd%3A.322290%3A59394) of Integrated Urban River Corridors ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)), respectively.

## Future directions

The workflows included in this repository were developed and applied in the proprietary software ArcGIS. Therefore, driven by current and future applications of riverspace analysis in research, we aim to **develop and share those workflows in an open-source format**. We are currently translating the analyses into R, leveraging the GIS capabilities of the R packages `sf` and `terra`. For a wider impact in the research community interested in the social-ecologically integrated URC assessment, in the future we aim to open up the workflows to Python users as well.

The indicator system and workflows are relevant beyond the focus of this assessment framework on social-ecological integration. They contribute to **the development of improved riverspace morphology analysis tools**. The development of general open source riverspace morphology analysis tools, which also leverage the increased availability of spatial-temporal big data, is the main direction in which we aim to channel our research software development efforts. The indicator system and analytical blocks developed in this framework provide a solid methodological base to that end.

## How to contribute

We welcome contributions from researchers from the field of urbanism or from any other relevant fields (e.g. water management, sociology, ecology) engaged in the analysis of riverside urban spaces. Contributions can be of at least two kinds:

- If you have potential use cases or ideas for cross-disciplinary application, please do share them by opening a GitHub issue. 

- If you want to contribute to the development of the assessment framework, we are especially interested in translating the GIS workflow to an open source format. Contributions to that end are especially welcome. Please open an issue to discuss your contribution before making a pull request.

For updates on this project as well as other related research or development efforts, follow [@claudiuforgaci](https://twitter.com/claudiuforgaci) on Twitter.