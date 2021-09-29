# Load packages ----
library(readr)
library(dplyr)
library(stringr)

# Reduce table to minimum scores ----
# on each sub-category of assessment, keeping both the 
# social and ecological indicators of each sub-category

## Read all scores
results_all <- read_csv("URC-D-data/URC-D-assessment-all.csv")

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
      mutate(m = min(c_across())) %>% 
      select(m)
    results_minimum <- cbind(results_minimum, results_indicator)
  } else {
    results_minimum <- cbind(results_minimum, results_indicator)
  }
}
colnames(results_minimum)[-1] <- assessment_categories

## Print table with minimum values
results_minimum <- tibble(results_minimum)

# Assess results using the method of mirrored assessment
## Where can social-ecological integration be improved
for (i in 1:length(results_minimum$segment)) {
  cat(paste0(results_minimum[i, 1], ":\n"))
  for (j in 2:(length(results_minimum)-9)) {
    if (results_minimum[i, j] < results_minimum[i, j+3]) {
      cat(paste0("Social-Ecological Integration can be improved with ", colnames(results_minimum[, j]), "\n"))
    } else if (results_minimum[i, j] > results_minimum[i, j+3]){
      cat(paste0("Social-Ecological Integration can be improved with ", colnames(results_minimum[, j+3]), "\n"))
    } else {
      cat(paste0("Improvign Social-Ecological Integration needs intervention in both ", 
                   colnames(results_minimum[, j]),
                   " and ",
                   colnames(results_minimum[, j+3]), "\n"))
    }
  }
  for (j in (length(results_minimum)-5):(length(results_minimum)-3)) {
    if (results_minimum[i, j] < results_minimum[i, j+3]) {
      cat(paste0("Social-Ecological Integration can be improved with ", colnames(results_minimum[, j]), "\n"))
    } else if (results_minimum[i, j] > results_minimum[i, j+3]){
      cat(paste0("Social-Ecological Integration can be improved with ", colnames(results_minimum[, j+3]), "\n"))
    } else {
      cat(paste0("Improvign Social-Ecological Integration needs intervention in both ", 
                 colnames(results_minimum[, j]),
                 " and ",
                 colnames(results_minimum[, j+3]), "\n"))
    }
  }
}
