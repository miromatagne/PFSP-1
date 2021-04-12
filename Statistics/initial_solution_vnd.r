srz.files <- list.files("./Results/VND",pattern = ".*SRZ.*.csv")
random.files <- list.files("./Results/VND",pattern = ".*RANDOM.*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")

for(i in seq(1,2)) {
  print(srz.files[i])
  print(random.files[i])
  srz.cost <- read.csv(paste("./Results/VND/",srz.files[i],sep=''))$solution
  rand.cost <- read.csv(paste("./Results/VND/",random.files[i],sep=''))$solution
  srz.time <- read.csv(paste("./Results/VND/",srz.files[i],sep=''))$execution_time
  rand.time <- read.csv(paste("./Results/VND/",random.files[i],sep=''))$execution_time
  
  srz.cost <- 100 * (srz.cost - best.known$BS) / best.known$BS
  rand.cost <- 100 * (rand.cost - best.known$BS) / best.known$BS
  
  print("PERCENTAGE DEVIATION :")
  t <- t.test(srz.cost, rand.cost, paired=T)$p.value
  print(paste("Student t-test:",t))

  w <- wilcox.test(srz.cost, rand.cost, paired=T)$p.value
  print(paste("Wilcoxon test:",w))
  
  # print("EXECUTION TIME :")
  # t <- t.test(srz.time, rand.time, paired=T)$p.value
  # print(paste("Student t-test:",t))
  # 
  # w <- wilcox.test(srz.time, rand.time, paired=T)$p.value
  # print(paste("Wilcoxon test:",w))
}


