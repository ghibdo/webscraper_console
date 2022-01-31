setwd("~/PycharmProjects/webscraper_bal_sheet")
library("reticulate")
use_python("/usr/local/bin/python3.9")
py_config()

import("pandas")
import("lxml")
import("bs4")
import("requests")

py_run_file("main.py")

console_sales_NA<-py$df
library(tidyr)
library(ggplot2)

p<-console_sales_NA %>%
  gather("Country", "Sales",-Console) %>%
  ggplot(aes(Console, as.numeric(Sales), fill = Country)) +
  geom_bar(position = "dodge", stat = "identity",color="black")+
  labs(y = "Sales in Millions") +
  scale_y_continuous(breaks = seq(0, 160, by = 10))+
  theme_bw() 

p
