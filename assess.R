# Load packages ----
library(readr)
library(dplyr)
library(stringr)
library(purrr)

# Reduce table to minimum scores ----
# on each sub-category of assessment, keeping both the 
# social and ecological indicators of each sub-category

## Read all scores
results_all <- read_csv2("URC-D-assessment-all.csv")

## Remove punctuation marks from column names
colnames(results_all)[-1] <- str_replace_all(colnames(results_all)[-1], "[[:punct:]]", "")

## Extract assessment categories from column names
assessment_categories <- colnames(results_all)[-1] %>% 
  substr(., 1, 3) %>% 
  unique

## Create table with minimum values
results_minimum <- tibble(results_all[,1])
for (i in assessment_categories) {
  results_indicator <- results_all %>% 
    select(starts_with(i)) 
  if (dim(results_indicator) > 1) {
    cnames <- colnames(results_indicator)
    results_indicator <- results_indicator %>% 
      rowwise() %>% 
      mutate(m = min(c(A121a, A121c, A123a, A123b))) # minimum does not work yet !!!!
    results_minimum <- cbind(results_minimum, results_indicator)
  } else {
    results_minimum <- cbind(results_minimum, results_indicator)
  }
}

## 