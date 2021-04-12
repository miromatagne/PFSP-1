setwd("/Users/miro/OneDrive - Universite Libre de Bruxelles/ULB/MA1/Heuristic optimization/Project/info-h413-implementation-exercise-1/Statistics")
srz.files <- list.files("./Results/Iterative Improvement",pattern = ".*SRZ.*.csv")
random.files <- list.files("./Results/Iterative Improvement",pattern = ".*RANDOM.*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")$BS

for(i in seq(1,6)) {
  print(srz.files[i])
  print(random.files[i])
  srz.cost <- read.csv(paste("./Results/Iterative Improvement/",srz.files[i],sep=''))$solution
  rand.cost <- read.csv(paste("./Results/Iterative Improvement/",random.files[i],sep=''))$solution
  srz.time <- read.csv(paste("./Results/Iterative Improvement/",srz.files[i],sep=''))$execution_time
  rand.time <- read.csv(paste("./Results/Iterative Improvement/",random.files[i],sep=''))$execution_time
  
  srz.cost <- 100 * (srz.cost - best.known) / best.known
  rand.cost <- 100 * (rand.cost - best.known) / best.known
  
  #print("PERCENTAGE DEVIATION :")
  #t <- t.test(srz.cost, rand.cost, paired=T)$p.value
  #print(paste("Student t-test:",t))
  
  #w <- wilcox.test(srz.cost, rand.cost, paired=T)$p.value
  #print(paste("Wilcoxon test:",w))
  
  print("EXECUTION TIME :")
  t <- t.test(srz.time, rand.time, paired=T)$p.value
  print(paste("Student t-test:",t))
  
  w <- wilcox.test(srz.time, rand.time, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
}