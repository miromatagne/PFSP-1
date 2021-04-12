exchange.files <- list.files("./Results/Iterative Improvement",pattern = ".*EXCHANGE.*.csv")
insert.files <- list.files("./Results/Iterative Improvement",pattern = ".*INSERT.*.csv")
transpose.files <- list.files("./Results/Iterative Improvement",pattern = ".*TRANSPOSE.*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")$BS

for(i in seq(1,4)) {
  print(exchange.files[i])
  print(insert.files[i])
  exchange.cost <- read.csv(paste("./Results/Iterative Improvement/",exchange.files[i],sep=''))$solution
  insert.cost <- read.csv(paste("./Results/Iterative Improvement/",insert.files[i],sep=''))$solution
  exchange.time <- read.csv(paste("./Results/Iterative Improvement/",exchange.files[i],sep=''))$execution_time
  insert.time <- read.csv(paste("./Results/Iterative Improvement/",insert.files[i],sep=''))$execution_time

  exchange.cost <- 100 * (exchange.cost - best.known) / best.known
  insert.cost <- 100 * (insert.cost - best.known) / best.known

  print("PERCENTAGE DEVIATION :")
  t <- t.test(exchange.cost, insert.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(exchange.cost, insert.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))

  print("EXECUTION TIME :")
  t <- t.test(exchange.time, insert.time, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(exchange.time, insert.time, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
}

for(i in seq(1,4)) {
  print(exchange.files[i])
  print(transpose.files[i])
  exchange.cost <- read.csv(paste("./Results/Iterative Improvement/",exchange.files[i],sep=''))$solution
  transpose.cost <- read.csv(paste("./Results/Iterative Improvement/",transpose.files[i],sep=''))$solution
  exchange.time <- read.csv(paste("./Results/Iterative Improvement/",exchange.files[i],sep=''))$execution_time
  transpose.time <- read.csv(paste("./Results/Iterative Improvement/",transpose.files[i],sep=''))$execution_time

  exchange.cost <- 100 * (exchange.cost - best.known) / best.known
  transpose.cost <- 100 * (transpose.cost - best.known) / best.known

  print("PERCENTAGE DEVIATION :")
  t <- t.test(exchange.cost, transpose.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(exchange.cost, transpose.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))

  print("EXECUTION TIME :")
  t <- t.test(exchange.time, transpose.time, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(exchange.time, transpose.time, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
}

for(i in seq(1,4)) {
  print(insert.files[i])
  print(transpose.files[i])
  insert.cost <- read.csv(paste("./Results/Iterative Improvement/",insert.files[i],sep=''))$solution
  transpose.cost <- read.csv(paste("./Results/Iterative Improvement/",transpose.files[i],sep=''))$solution
  insert.time <- read.csv(paste("./Results/Iterative Improvement/",insert.files[i],sep=''))$execution_time
  transpose.time <- read.csv(paste("./Results/Iterative Improvement/",transpose.files[i],sep=''))$execution_time

  insert.cost <- 100 * (insert.cost - best.known) / best.known
  transpose.cost <- 100 * (transpose.cost - best.known) / best.known

  #print("PERCENTAGE DEVIATION :")
  t <- t.test(insert.cost, transpose.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(insert.cost, transpose.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
  
  print("EXECUTION TIME :")
  t <- t.test(insert.time, transpose.time, paired=T)$p.value
  print(paste("Student t-test:",t))
  
  w <- wilcox.test(insert.time, transpose.time, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
}

