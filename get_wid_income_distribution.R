#' To install the [wid library](https://github.com/thomasblanchet/wid-r-tool):
#' > install.packages("devtools")
#' > devtools::install_github("WIDworld/wid-r-tool")
#' 
#' Run the `download_and_export_income_distribution` function to export income
#' distribution.
#' Example:
#' > download_and_export_income_distribution("income_distribution.csv")

library(wid)
library(tidyverse)

get_main_quantiles <- function(){
  quantiles <- c()
  
  # Generate centiles strings, from "p0p1" to "p98p99"
  for(i in 0:98){
    j = i + 1
    next_centile <- paste0("p", i, "p", j)
    quantiles <- c(quantiles, next_centile)  
  }
  
  # Generate millile strings, from "p99.1p99.2" to "p99.8p99.9"
  for(i in 1:8){
    j = i + 1
    next_millile <- paste0("p99.", i, "p99.", j)
    quantiles <- c(quantiles, next_millile)  
  }
  
  # Add the last millile
  quantiles <- c(quantiles, "p99.9p100")
  
  return(quantiles)
}


download_and_export_income_distribution <- function(export_path){
  wid_df <- download_wid(
    indicators = "tptinc",        # "t" is for threshold, "ptinc" is for income
    areas = "WO",                 # "WO" means the entire world
    years = c(2021),              # 2021 is the latest available date as of 2023
    perc = get_main_quantiles(),
    ages = "all",
    pop = "all",
    metadata = TRUE,
    include_extrapolations = TRUE,
    verbose = FALSE
  )
  
  # Replace "p0p1" by "p0" and so on, sort by threshold value, and export to csv
  wid_df <- wid_df %>%
    mutate(percentile = str_extract(percentile, "^p[^p]+")) %>%
    arrange(value) %>%
    write_csv(export_path)
  
  return(wid_df)
}
