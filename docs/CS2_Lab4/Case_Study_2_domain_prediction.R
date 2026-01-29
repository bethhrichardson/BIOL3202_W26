#!/usr/bin/Rscript
##Tells the computer this is R code (optional if you're using an IDE like RStudio)

library(tidyverse)
##loads the tidyverse package

variants <- read_csv("variants.csv")
## Reads the CSV file into R as a tibble (data frame)

variants_with_domain <- variants %>%
## Pipes the data frame into the next command

  mutate(
## takes a column from a data frame line by line and 

    domain = case_when(
##Creates a new column called "domain", and case_when is one of the R equivalents of if/else

      aa_position >= 1   & aa_position <= 58  ~ "oligomerisation",
##Assign oligomerisation domain to any variants between amino acids 1 and 58

      aa_position >= 59  & aa_position <= 437 ~ "catalytic",
##Assign catalytic domain domain to any variants between amino acids 59 and 437

      aa_position >= 438 & aa_position <= 574 ~ "allosteric",
##Assign allosteric domain to any variants between amino acids 438 and 574

      TRUE                                 ~ "unknown"
##Catch any values that do not match the above rules
    )
  )
## Don't forget to close all your brackets or R will yell at you

write_csv(variants_with_domain, file = "variants_with_domain.csv")
##Writes the updated data frame to a new CSV file
