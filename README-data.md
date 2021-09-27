<!-- Note: README.pdf is a rendered version of this README.md file. -->

# Dataset from the Social-Ecological Assessment of Urban River Corridor Dâmbovița, Bucharest, Romania



#### Table of Contents

1.  [General information](#1-General-information)

2.  [Methodological information](#2-Methodological-information)

    2.1. [Description of methods](#2-1-Description-of-methods)

    2.2. [Instrument- or software-specific information](#2-2-Instrument-or-software-specific-information)

    2.3. [Software and data references](#2-3-Software-and-data-references)

3.  [Data and file overview](#3-Data-and-file-overview)

    3.1. [File formats and naming conventions](#3-1-File-formats-and-naming-conventions)

    3.2. [File list and descriptions](#3-2-File-list-and-descriptions)

    3.3. [Versioning](#3-3-Versioning)

4.  [Sharing and access information](#4-Sharing-and-access-information)



## 1. General information

-   Title of the dataset: Social-Ecological Assessment of Urban River Corridor Dâmbovița, Bucharest, Romania

-   Description: This dataset contains data generated in the Social-Ecological Assessment of Urban River Corridor (URC) Dâmbovița, Bucharest, Romania, as part of the PhD research "Integrated Urban River Corridors: Spatial Design for Social-Ecological Resilience in Bucharest and Beyond" ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)), conducted at TU Delft in 2017. The dataset consists of the geospatial data used for the spatial analyses of URC Dâmbovița and assessment data, including the results of analyses for each indicator used in the assessment.

-   Contact information:

    -   Principal investigator (contact person):

        -   Name: Claudiu Forgaci
        -   Institution: Delft University of Technology
        -   Email: [C.Forgaci\@tudelft.nl](mailto:C.Forgaci@tudelft.nl)

    -   Associated study personnel:

        -   Name: Daniele Cannatella
        -   Institution: Delft University of Technology
        -   Email: [D.Cannatella\@tudelft.nl](mailto:D.Cannatella@tudelft.nl)

-   Funding sources: EIT Climate-KIC

-   Dates of data generation: The data was generated between 2017-11-14 and 2018-06-25 by Claudiu Forgaci and Daniele Cannatella, and last reviewed on 2021-09-27 by Claudiu Forgaci.



## 2. Methodological information

### 2.1 Description of methods

In preparation for the spatial analyses used in the assessment, [geospatial data](#3-1-1-Geospatial-data) was obtained as follows:

1.  The boundary and segments of the URC were drawn based on the delineation method described in ([Forgaci, 2018, pp. 88-89](https://doi.org/10.7480/abe.2018.31))
2.  Relevant vector and raster data openly accessible from OpenSteetMap (2015), Urban Atlas (EEA, 2010), and SRTM (EROS, 2017) were clipped to the URC boundary and saved as base geospatial layers to be used in the spatial analyses.

For each indicator, the assessment data was generated using the following steps:

1.  Indicator-specific spatial analyses were carried out and the results were recorded.

2.  The results from analyses were classified into low, medium, and high based on indicator-specific thresholds, and were given a standardized score of 1, 2, or 3.

### 2.2 Instrument- or software-specific information

ArcGIS v10.2 and v10.3 were used to perform the analyses for most indicators, except for the spatial delineation of URC Dâmbovița and for the analysis of indicator `A121a` which was performed in QGIS 2.\#. The choice for ArcGIS or QGIS or for different versions thereof depended on the requirements of plugins used for specific analyses:

-   MatrixGreen v1.10.1 ([Bodin and Zetterberg, 2010](https://www.stockholmresilience.org/research/modelling-and-visualisation-lab/matrixgreen.html)) for ArcGIS v10.3.0 was used for the green network analysis of indicator `A211a`.

-   Axwoman v6.3 ([Jiang, 2015](http://giscience.hig.se/binjiang/Axwoman/)) for ArcGIS v10.2.0 was used to isolate the transversal roads used by indicator `A221`.

-   [Space Syntax Toolkit](https://github.com/SpaceGroupUCL/qgisSpaceSyntaxToolkit) (Gil et al., 2015) for QGIS v2.14 and above was used for the indicator `A121a`.

### 2.3 Software and data references

-   Earth Resources Observation And Science (EROS) Center. (2017). Shuttle Radar Topography Mission (SRTM) 1 Arc-Second Global [Data set]. U.S. Geological Survey. <https://doi.org/10.5066/F7PR7TFT> [Data file from 2017-11-17]

-   Bodin, Ö. and A. Zetterberg (2010) MatrixGreen User's Manual: Landscape Ecological Network Analysis Tool. Stockholm university and Royal Institute of Technology (KTH), Stockholm.

-   EEA, 2010, Mapping guide for a European Urban Atlas, European Environment Agency, Copenhagen, <http://www.eea.europa.eu/data-and-maps/data/urban-atlas#tab-methodology>.

-   Gil, J., Varoudis, T., Karimi, K., Penn, A., 2015. The Space Syntax Toolkit: integrating depthmapX and exploratory spatial analysis workflows in QGIS, in: Proceedings of the 10th International Space Syntax Symposium, University College London, London, UK, p. 148:1-148:12.

-   Jiang B. (2015), Axwoman 6.3: An ArcGIS extension for urban morphological analysis, <http://giscience.hig.se/binjiang/Axwoman/>, University of Gävle, Sweden.

-   OpenStreetMap contributors. (2015) Planet dump [Data file from 2017-11-14]. Retrieved from <https://planet.openstreetmap.org>.



## 3. Data and file overview

### 3.1 File formats and naming conventions

#### 3.1.1 Geospatial data

Geospatial data is stored in the open, non-proprietary, platform-independent and standard-based GeoPackage (`GPKG`) format. `GPKG` uses an SQLite container that can store multiple features, both vector and raster, and a wide variety of formats, which makes it a portable and accessible format for small-sized datasets.

Geospatial data files in this dataset are named `URC-I.gpkg` and comprise vector and raster features named as `URC-I-layer-name`, where:

-   `URC` indicates that the data is a layer of an Urban River Corridor.

-   `I` is the initial of the river, which is `D` for river Dâmbovița.

-   `layer-name` is the name of the layer used for analysis and can be `boundary`, `segments`, `buildings`, `streets`, `green-spaces`, `river-line`, `river-polygon`, `DEM`, or `satellite`.

All geospatial data in this dataset use the European Terrestrial Reference System 1989 (ETRS89).

#### 3.1.2 Assessment data

The list of indicators and the results of the assessment are stored in `CSV` files. Each `CSV` file represents the result for one indicator and it is named after the indicator, that is, with a capital letter followed by three digits and a lowercase letter followed by the suffix `-results` (e.g. `A123a-results.csv`), where:

-   The capital letter is either `A` if the indicator measures *connectivity* or `B` if it measures *spatial capacity*.

-   The first digit is either `1`, when the indicator is in the *social* category, or `2`, if the indicator is of *ecological* kind.

-   The second digit, numbered incrementally and starting with 1, indicates *the main sub-category* specific to the main category indicated by the capital letter A or B.

-   The third digit, numbered incrementally and starting with 1, indicates *the spatial element* that is measured.

-   The lowercase letter is optional and, if present, it represents *a specific method of measurement* of the spatial element indicated by the third digit.

### 3.2 File list and descriptions

#### 3.2.1 Geospatial data

The following features are stored in `URC-D.gpkg`:

-   `URC-D-boundary` - a vector feature with the outer boundary of URC Dâmbovița, delineated according to the method described in ([Forgaci, 2018, pp.88-89](https://doi.org/10.7480/abe.2018.31))

-   `URC-D-segments` - a vector feature with `URC-D-boundary`, segmented according to the method described in ([Forgaci, 2018, pp.88-89](https://doi.org/10.7480/abe.2018.31))

-   `URC-D-buildings` - a vector feature extracted from OpenStreetMap (..-..-..) of all buildings located within `URC-D-boundary`.

-   `URC-D-river-line` - a vector feature extracted from OpenStreetMap (..-..-..) of the center line of the river Dâmbovița.

-   `URC-D-river-polygon` - a vector feature extracted from OpenStreetMap (..-..-..) of the river surface as a polygon.

-   `URC-D-DEM` - a raster feature with the digital elevation model of the area within `URC-D-boundary`.

#### 3.2.2 Assessment data

-   `URC-D-indicators.csv` - a table with the list of indicators

    -   `id` - unique indicator name as defined in Section 3.1.2
    -   `name` - the name of the indicator
    -   `definition` - definition of what is measured and how the measurement is standardized on the three-point assessment scale
    -   `source` - literature reference, if any

-   `URC-D-assessment.csv` - a table with the summary of assessment scores

    -   

-   `A111a-results.csv` - Slow mobility routes - continuity

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `value` - measured value for `segment`; unit of measurement depends on indicator
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A111b-results.csv` - Slow mobility routes - %

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `value` - measured value for `segment`; unit of measurement depends on indicator
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A121a-results.csv` - Accessibility - network

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `TLEN1` - total length of streets in `segment` with a low integration value
    -   `TLEN2` - total length of streets in `segment` with a medium integration value
    -   `TLEN3` - total length of streets in `segment` with a high integration value
    -   `value1` - percentage of the total length of streets in `segment` with a low integration value
    -   `value2` - percentage of the total length of streets in `segment` with a medium integration value
    -   `value3` - percentage of the total length of streets in `segment` with a high integration value
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A121c-results.csv` - Accessibility - visitors

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `total_length` - total length of river bank within `segment`
    -   `service area length` [rename to `accessible_length`]- length of river bank that falls within public transport service areas within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: percentage of `service area length` out of `total length`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A123a-results.csv` - Crossability - linear density of crossings

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `bridges` - number of bridges within `segment`
    -   `length` - length of river measured on the river center line within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: linear density of bridges calculated as `length` / `bridges`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A123b-results.csv` - Crossability - river width

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `min_value` - the shortes river width within `segment`
    -   `max_value` - the longest river width within `segment`
    -   `std` - standard deviation, the distribution of river widths within `segment`
    -   `mean_value` - the average river width within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: ...
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A131a-results.csv` - Contact with water - points

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `bridges` - number of bridges within `segment`
    -   `length` - length of river measured on the river center line within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: linear density of bridges calculated as `length` / `bridges`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A211a-results.csv` - Landscape connectivity - connected components

-   `A221-results.csv` - Presence of transversal corridors

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `length_transversal` - total length of transversal streets within `segment`
    -   `length_transversal_green` - length of of transversal roads crossing or touching a green space within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: percentage of `length_green` out of `length_transversal`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A223-results.csv` - Sinuosity

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)
    -   `length_river` - length of the river measured along the center line within `segment`
    -   `length_valley` - length of the valley measured along ta straight line connecting the entry and exit points of the river within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: `length_river` / `length_valley`

-   `A231-results.csv` - Presence of ecotones

    -   `segment` - unique id of the corridor segment for which the measurement is recorded, with the prefix `CS` and numbered incrementally from upstream to downstream with a two-digit format starting from `01` (i.e. `CS01`, `CS02`, etc.)

    -   `length_riverbanks` - total length of riverbanks within `segment`

    -   `length_ecotones` - total length of observed ecotones within `segment`

    -   `value` - measured value for `segment`; unit of measurement depends on indicator: percentage of `length_ecotones` out of `length_riverbanks`

    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `B111a-results.csv` - Diversity of land uses - patch richness diversity

    -   

-   `B121a-results.csv` - Visual permeability - % of visible riverspace

-   `B132a-results.csv` - Waterfront constitutedness - configuration

-   `B211-results.csv` - Biodiversity - presence of species-rich areas

-   `B224-results.csv` - Respect of natural dynamics

-   `B231a-results.csv` - Coverage - % open space



## 4. Sharing and access information

-   License: CC-BY-4.0
-   Publication: https://doi.org/10.7480/abe.2018.31
-   Locations of data: 4TU.ResearchData
-   Citation: Forgaci, C. (2021). Social-Ecological Assessment of Urban River Corridor Dâmbovița, Bucharest, Romania [Data set]. https://doi.org/10.4121/15126795.v2
