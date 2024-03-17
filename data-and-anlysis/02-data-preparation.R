library(tidyverse)


## Experiment 1

data_raw_01 <- read_csv("01-data-raw/data-raw-pilot-01.csv") |>
  mutate(
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(prompt, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )

sum_stats_01 <- data_raw_01 |> 
  group_by(condition) |> 
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 1")

## Experiment 2

data_raw_02 <- read_csv("01-data-raw/data-raw-pilot-02.csv") |> 
  mutate(
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(name1, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )

sum_stats_02 <- data_raw_02 |>
  group_by(condition) |>
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 2")

## Experiment 3

data_raw_03 <- read_csv("01-data-raw/data-raw-pilot-03.csv") |> 
  mutate(
    condition = str_c(itemType, "-", targeted),
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(name1, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )

sum_stats_03 <- data_raw_03 |>
  group_by(condition) |>
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 3")

## Experiment 4

data_raw_04 <- read_csv("01-data-raw/data-raw-pilot-04.csv") |> 
  mutate(
    condition = str_c(treatment, "-", QUDTarget),
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(name1, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )
  
sum_stats_04 <- data_raw_04 |>
  group_by(condition) |>
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 4")

  
## Experiment 5

data_raw_05 <- read_csv("01-data-raw/data-raw-pilot-05.csv") |> 
  mutate(
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(statement, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )
  
sum_stats_05 <- data_raw_05 |>
  group_by(condition) |>
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 5")

## Experiment 6 (had a coding mistake, which first needs to be fixed)

data_raw_06 <- read_csv("01-data-raw/data-raw-pilot-06.csv") |> 
  mutate(
    modifier  = ifelse(targeted == "first", modifier, ifelse(modifier == "having", "getting", "having")),
    condition = str_c(modifier, "-", position),
    response_type = ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(name1, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first")
  )

sum_stats_06 <- data_raw_06 |>
  group_by(condition) |>
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 6")
