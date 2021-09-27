## 1. General information

-   Title of the dataset: Social-Ecological Assessment of Urban River Corridor Dâmbovița, Bucharest, Romania

-   Description: This dataset contains data generated in the Social-Ecological Assessment of Urban River Corridor (URC) Dâmbovița, Bucharest, Romania, as part of the PhD research "Integrated Urban River Corridors: Spatial Design for Social-Ecological Resilience in Bucharest and Beyond" ([Forgaci, 2018](https://doi.org/10.7480/abe.2018.31)), conducted at TU Delft in 2017. The dataset consists of the geospatial data used for the spatial analyses of URC Dâmbovița and assessment data, including the results of analyses for each indicator used in the assessment.

-   Contact information:

    -   Principal investigator (contact person):

        -   Name: Claudiu Forgaci
        -   Institution: Delft University of Technology
        -   Email: [C.Forgaci\@tudelft.nl](mailto:C.Forgaci@tudelft.nl){.email}

    -   Associated study personnel:

        -   Name: Daniele Cannatella
        -   Institution: Delft University of Technology
        -   Email: [D.Cannatella\@tudelft.nl](mailto:D.Cannatella@tudelft.nl){.email}

-   Funding sources: EIT Climate-KIC

-   Dates of data generation: 2017

## 2. Methodological information

### 2.1 Description of methods

Geospatial data was obtained from OpenStreetMap:

1.  The boundary and segments of the URC were drawn based on the delineation method described in ([Forgaci, 2018, pp.88-89](https://doi.org/10.7480/abe.2018.31))
2.  Relevant features from openly accessible data from OpenSteetMap, EEA Urban Atlas, and ASTER GDEM were clipped within the URC boundary and saved as the base geospatial layers to be used in the spatial analyses.

For each indicator, the data was generated using the following steps:

1.  Indicator-specific spatial analyses were carried out and the results were recorded.

2.  The results from analyses were classified into low, medium, and high based on indicator-specific thresholds, and were given a standardized score of 1, 2, or 3.

### 2.2 Instrument- or software-specific information

-   ArcGIS \#.\# was used to perform the analyses for indicators ...
-   QGIS \#.\# was used to perform the analyses for the delineation of URC Dâmbovița and for the analysis of indicators `A121a` and `A211a`.
-   The ArcGIS tool MatrixGreen was used for the indicator `A211a`.
-   The QGIS plugin Space Syntax Toolkit was used for the indicator `A121a`.

## 3. Data and file overview

### 3.1 File formats and naming conventions

#### 3.1.1 Geospatial data

Geospatial data is stored in the open, non-proprietary, platform-independent and standard-based GeoPackage (`GPKG)` format. It uses an SQLite container that can store multiple features, both vector and raster, and a wide variety of formats, which makes it an portable and accessible format for small-sized datasets.

Geospatial data files in this dataset are named `URC-I.gpkg` and comprise vector and raster features named as `URC-I-layer-name`, where:

-   `URC` indicates that the data is a layer of an Urban River Corridor.

-   `I` is the initial of the river, which is either `D` for river Dâmbovița or `C` for river Colentina.

-   `layer-name` is the name of the layer used for analysis and can be `boundary`, `segments`, `buildings`, `streets`, `green-spaces`, `river-line`, `river-polygon`, `DEM`, or `satellite`.

All geospatial data in this dataset use the Coordinate Reference System (CRS) EPSG:31700 - Dealul Piscului 1970/ Stereo 70.

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

-   `URC-D-assessment.csv` - a table with the summary of assessment scores

    -   

-   `A111a-results.csv` - Slow mobility routes - continuity

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `value` - measured value for `segment`; unit of measurement depends on indicator
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A111b-results.csv` - Slow mobility routes - %

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `value` - measured value for `segment`; unit of measurement depends on indicator
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A121a-results.csv` - Accessibility - network

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `TLEN1` - total length of streets in `segment` with a low integration value
    -   `TLEN2` - total length of streets in `segment` with a medium integration value
    -   `TLEN3` - total length of streets in `segment` with a high integration value
    -   `value1` - percentage of the total length of streets in `segment` with a low integration value
    -   `value1` - percentage of the total length of streets in `segment` with a medium integration value
    -   `value1` - percentage of the total length of streets in `segment` with a high integration value
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A121c-results.csv` - Accessibility - visitors

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `total length` - total length of river bank within `segment`
    -   `service area length` - length of river bank that falls within public transport service areas within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: percentage of `service area length` out of `total length`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A123a-results.csv` - Crossability - linear density of crossings

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `bridges` - number of bridges within `segment`
    -   `length` - length of river measured on the river center line within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: linear density of bridges calculated as `length` / `bridges`
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A123b-results.csv` - Crossability - river width

    -   `segment` - unique number of the corridor segment for which the measurement is recorded
    -   `min_value` - the shortes river width within `segment`
    -   `max_value` - the longest river width within `segment`
    -   `std` - standard deviation, the distribution of river widths within `segment`
    -   `mean_value` - the average river width within `segment`
    -   `value` - measured value for `segment`; unit of measurement depends on indicator: ...
    -   `index` - standardized score of the measured `value` for `segment`; `1` is low, `2` is medium, `3` is high

-   `A131a-results.csv` - Contact with water - points

-   `A211a-results.csv` - Landscape connectivity - connected components

-   `A221-results.csv` - Presence of transversal corridors

-   `A223-results.csv` - Sinuosity

-   `B111a-results.csv` - Diversity of land uses - patch richness diversity

-   `B114-results.csv` -

-   `B121a-results.csv` - Visual permeability - % of visible riverspace

-   `B132a-results.csv` - Waterfront constitutedness - configuration

-   `B211-results.csv` - Biodiversity - presence of species-rich areas

-   `B224-results.csv` - Respect of natural dynamics

-   `B231a-results.csv` - Coverage - % open space

### Additional related data collected

### Versioning

The data was generated between 2017-xx-xx and 2017-xx-xx by Claudiu Forgaci and Daniele Cannatella, and last reviewed on 2021-09-20 by Claudiu Forgaci.

## 4. Sharing and access information

-   License: CC-BY-4.0
-   Publication: [\<https://doi.org/10.7480/abe.2018.31\>](https://doi.org/10.7480/abe.2018.31){.uri}
-   Locations of data:
-   Citation:
