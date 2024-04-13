library(tidyverse)
library(tidyboot)
library(brms)

string_lengths <- function(strings) {
  sapply(strings, nchar)
}

data_cleaned <- read_csv("04-prepped-data-pilot-manual-cleaning.csv") |> 
  mutate(
    nChar_mf = sapply(response_prepped, nchar)
  )

data_cleaned |> 
  ggplot(aes(x = nChar_mf )) +
  geom_histogram(binwidth = 1) +
  facet_wrap(~prodType)

# use BRMS to run a Poisson regression model, comparing prodType

fit <- brm(
  formula = nChar_mf ~ prodType,
  data = data_cleaned,
  family = poisson()
)

hypothesis(fit, "prodTypeeffect > 0")
