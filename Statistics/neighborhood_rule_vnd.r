tei.files <- list.files("./Results/VND",pattern = ".*TRANSPOSE_EXCHANGE_INSERT.*.csv")
tie.files <- list.files("./Results/VND",pattern = ".*TRANSPOSE_INSERT_EXCHANGE.*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")$BS

for(i in seq(1,2)) {
  print(tei.files[i])
  print(tie.files[i])
  tei.cost <- read.csv(paste("./Results/VND/",tei.files[i],sep=''))$solution
  tie.cost <- read.csv(paste("./Results/VND/",tie.files[i],sep=''))$solution
  tei.time <- read.csv(paste("./Results/VND/",tei.files[i],sep=''))$execution_time
  tie.time <- read.csv(paste("./Results/VND/",tie.files[i],sep=''))$execution_time
  
  tei.cost <- 100 * (tei.cost - best.known) / best.known
  tie.cost <- 100 * (tie.cost - best.known) / best.known
  
  #print("PERCENTAGE DEVIATION :")
  t <- t.test(tie.cost, tei.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(tie.cost, tei.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
  
  # print("EXECUTION TIME :")
  # t <- t.test(tie.time, tei.time, paired=T)$p.value
  # print(paste("Student t-test:",t))
  # 
  # w <- wilcox.test(tie.time, tei.time, paired=T)$p.value
  # print(paste("Wilcoxon test:",w))
}

