first.files <- list.files("./Results/Iterative Improvement",pattern = ".*FIRST.*.csv")
best.files <- list.files("./Results/Iterative Improvement",pattern = ".*BEST.*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")$BS

for(i in seq(1,6)) {
  print(first.files[i])
  print(best.files[i])
  first.cost <- read.csv(paste("./Results/Iterative Improvement/",first.files[i],sep=''))$solution
  best.cost <- read.csv(paste("./Results/Iterative Improvement/",best.files[i],sep=''))$solution
  first.time <- read.csv(paste("./Results/Iterative Improvement/",first.files[i],sep=''))$execution_time
  best.time <- read.csv(paste("./Results/Iterative Improvement/",best.files[i],sep=''))$execution_time
  
  first.cost <- 100 * (first.cost - best.known) / best.known
  best.cost <- 100 * (best.cost - best.known) / best.known
  
  print("PERCENTAGE DEVIATION :")
  t <- t.test(first.cost, best.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(first.cost, best.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
  
  print("EXECUTION TIME :")
  t <- t.test(first.time, best.time, paired=T)$p.value
  print(paste("Student t-test:",t))
  
  w <- wilcox.test(first.time, best.time, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
}