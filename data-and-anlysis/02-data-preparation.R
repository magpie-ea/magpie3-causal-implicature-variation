library(tidyverse)
library(tidyboot)

## bootstrapped CI

bootstrap_ci <- function(data, R=1000, ci=0.95) {
  n <- length(data)
  boot_means <- numeric(R)
  
  for(i in 1:R) {
    sample_indices <- sample(x=1:n, size=n, replace=TRUE)
    boot_sample <- data[sample_indices]
    boot_means[i] <- mean(boot_sample)
  }
  
  alpha <- (1 - ci) / 2
  lower_bound <- quantile(boot_means, probs=alpha)
  upper_bound <- quantile(boot_means, probs=1-alpha)
  
  return(data.frame("lower" = lower_bound, "mean" = mean(data), "upper" = upper_bound))
}


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

## Experiment 7

bad_IDs <- c(3237, 3242, 3238, 3243, 3245, 3279, 3269, 3282, 3287, 3294, 3324, 3329)

data_raw_07 <- read_csv("01-data-raw/data-raw-pilot-07.csv") |> 
  filter(! submission_id %in% bad_IDs) |> 
  mutate(
    response_type = ifelse(trialType == "FC-interpretation", 
                           ifelse(str_extract(response, "^[a-zA-Z]+") == str_extract(prompt, "^[a-zA-Z]+"),
                           "first-causes-second", "second-causes-first"),
                           "free generation"
    )) |> 
  mutate(
    generation = case_when(
        group == 'cause-first' & trialType == 'generation-task-1' ~ 'cause-first',
        group == 'effect-first' & trialType == 'generation-task-2' ~ 'cause-first',
        group == 'cause-first' & trialType == 'generation-task-2' ~ 'effect-first',
        group == 'effect-first' & trialType == 'generation-task-1' ~ 'effect-first',
        TRUE ~ "NA"
  ))

sum_stats_07 <- data_raw_07 |>
  filter(trialType == "FC-interpretation") |>
  group_by(group) |> 
  summarize(first_is_cause = mean(response_type == "first-causes-second")) |> 
  mutate(experiment = "Exp. 7") |> 
  rename(condition = group)

data_raw_07 |> 
  filter(trialType != "FC-interpretation") |> 
  group_by(generation, trialType) |>  
  reframe(bootstrap_ci(responseTime)) |> 
  ggplot(aes(x = trialType, y = mean, color = generation, group = generation)) + 
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.2) +
  geom_line() +
  geom_point(size = 2.5)

data_raw_07 |> 
  filter(trialType != "FC-interpretation") |> 
  group_by(generation) |>  
  reframe(bootstrap_ci(responseTime)) |> 
  ggplot(aes(x = generation, y = mean, color = generation, group = generation)) + 
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.2) +
  geom_point(size = 2.5)


# Prep the free production data

# Words to be replaced with their initials
words_to_initials <- c(
  'Themaglin' = 'T', 'Rebosen' = 'R', 'Denoden' = 'D', 
  'Flembers' = 'F', 'Agoriv' = 'A', 'Ceflar' = 'C',
  'themaglin' = 'T', 'rebosen' = 'R', 'denoden' = 'D', 
  'flembers' = 'F', 'agoriv' = 'A', 'ceflar' = 'C'
  )

# Function to replace words with their initials
replace_words_with_initials <- function(text, replacements) {
  for (word in names(replacements)) {
    text <- str_replace_all(text, word, replacements[word])
  }
  return(text)
}

data_p7_free_prod <- data_raw_07 |> 
  filter(trialType != "FC-interpretation") |> 
  select(submission_id, trialNR, generation, response) |> 
  pivot_wider(names_from = generation, values_from = response) |> 
  mutate(`effect-first-prepped` = map_chr(`effect-first`, replace_words_with_initials, replacements = words_to_initials),
         `cause-first-prepped`  = map_chr(`cause-first`, replace_words_with_initials, replacements = words_to_initials)) |>
  mutate(
    nr_characters_effect_first = str_length(`effect-first-prepped`),
    nr_characters_cause_first = str_length(`cause-first-prepped`)
  ) 

# get average number of characters per response and number of unique responses
# Define the function
string_lengths <- function(strings) {
  sapply(strings, nchar)
}
data_p7_free_prod |>
  select(submission_id, trialNR, `effect-first-prepped`, `cause-first-prepped`, 
         nr_characters_effect_first, nr_characters_cause_first) |>
  pivot_longer(cols = c(`effect-first-prepped`, `cause-first-prepped`), names_to = "condition", values_to = "generation") |>
  mutate(string_length = string_lengths(generation)) |>
  group_by(condition) |>
  summarize(
    mean_nr_characters = mean(string_length),
    # SD_nr_characters = sd(string_length),
    nr_unique_responses = n_distinct(generation)
  )
  
data_p7_free_prod |>  
  write_csv('prepped-data-pilot-07.csv')

## merging all results togeter

sum_stats <- 
  bind_rows(
    sum_stats_01, sum_stats_02, sum_stats_03, 
    sum_stats_04, sum_stats_05, sum_stats_06, 
    sum_stats_07
    )






