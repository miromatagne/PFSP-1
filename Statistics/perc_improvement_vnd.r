result.files <- list.files("./Results/VND",pattern = "*.csv")

ii_srz_files <- c('./Results/Iterative Improvement/SRZ_FIRST_IMPROVEMENT_EXCHANGE.csv','./Results/Iterative Improvement/SRZ_FIRST_IMPROVEMENT_INSERT.csv')
ii_random_files <- c('./Results/Iterative Improvement/RANDOM_INIT_FIRST_IMPROVEMENT_EXCHANGE.csv','./Results/Iterative Improvement/RANDOM_INIT_FIRST_IMPROVEMENT_INSERT.csv')

vnd_srz_files <- c('./Results/VND/SRZ_TRANSPOSE_EXCHANGE_INSERT.csv','./Results/VND/SRZ_TRANSPOSE_INSERT_EXCHANGE.csv')
vnd_random_files <- c('./Results/VND/RANDOM_INIT_TRANSPOSE_EXCHANGE_INSERT.csv','./Results/VND/RANDOM_INIT_TRANSPOSE_INSERT_EXCHANGE.csv')

for(v in vnd_srz_files) {
  for(i in ii_srz_files) {
    v_file <- read.csv(v)
    v.50 <- subset(v_file,grepl("50",instance))
    v.100 <- subset(v_file,grepl("100",instance))
    i_file <- read.csv(i)
    i.50 <- subset(i_file,grepl("50",instance))
    i.100 <- subset(i_file,grepl("100",instance))
    print(v)
    print(i)
    print("50 jobs")
    prob.50 <- (1-v.50$solution/i.50$solution)*100
    print(mean(prob.50))
    print("100 jobs")
    prob.100 <- (1-v.100$solution/i.100$solution)*100
    print(mean(prob.100))
  }
}

for(v in vnd_random_files) {
  for(i in ii_random_files) {
    v_file <- read.csv(v)
    v.50 <- subset(v_file,grepl("50",instance))
    v.100 <- subset(v_file,grepl("100",instance))
    i_file <- read.csv(i)
    i.50 <- subset(i_file,grepl("50",instance))
    i.100 <- subset(i_file,grepl("100",instance))
    print(v)
    print(i)
    print("50 jobs")
    prob.50 <- (1-v.50$solution/i.50$solution)*100
    print(mean(prob.50))
    print("100 jobs")
    prob.100 <- (1-v.100$solution/i.100$solution)*100
    print(mean(prob.100))
  }
}

prob <- (1-vnd_srz_tei$solution/ii_srz_insert$solution)*100
mean(prob)
