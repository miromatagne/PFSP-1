result.files <- list.files("./Results/Iterative Improvement",pattern = "*.csv")
best.known <- read.csv("./Results/bestSolutions.txt")
best.known.50 <- subset(best.known,grepl("50",oiiProblem))
best.known.100 <- subset(best.known,grepl("100",oiiProblem))

execution.times.50 <- c()
execution.times.100 <- c()
costs.50 <- c()
costs.100 <- c()

lapply(result.files, function(x) {
  name <- paste("./Results/Iterative Improvement/",x,sep='')
  res <- read.csv(name)
  res.50 <- subset(res,grepl("50",instance))
  res.100 <- subset(res,grepl("100",instance))
  res.50.cost <- 100 * (res.50$solution - best.known.50$BS) / best.known.50$BS
  res.100.cost <- 100 * (res.100$solution - best.known.100$BS) / best.known.100$BS
  res.50.time <- res.50$execution_time
  res.100.time <- res.100$execution_time
  print(x)
  print(paste("Average relative percentage deviation on 50 jobs :", mean(res.50.cost)))
  print(paste("Average computation time on 50 jobs :", mean(res.50.time)))
  print(paste("Average relative percentage deviation on 100 jobs :", mean(res.100.cost)))
  print(paste("Average computation time on 100 jobs :", mean(res.100.time)))
  print("----------------------------------------------------------")
  execution.times.50 <<- c(execution.times.50,mean(res.50.time))
  execution.times.100 <<- c(execution.times.100,mean(res.100.time))
  costs.50 <<- c(costs.50,mean(res.50.cost))
  costs.100 <<- c(costs.100,mean(res.100.cost))
})

legend <- c("RBE","RBI","RBT","RFE","RFI","RFT","SBE","SBI","SBT","SFE","SFI","SFT")

x <- barplot(execution.times.50,names.arg=legend,col="lightblue",main="Execution times on 50 jobs", ylab="Time (s)",ylim=c(0,120),cex.lab=1.5, cex.axis=1.5)
y <- as.matrix(execution.times.50)
text(x,y+3,labels=as.character(round(y,digits=2)),cex=1.5)

x <- barplot(execution.times.100,names.arg=legend,col="lightblue",main="Execution times on 100 jobs", ylab="Time (s)",ylim=c(0,2500),cex.lab=1.5, cex.axis=1.5)
y <- as.matrix(execution.times.100)
text(x,y+80,labels=as.character(round(y,digits=2)),cex=1.5)

x <- barplot(costs.50,names.arg=legend,col="lightblue",main="Percentage deviations for 50 jobs", ylab="Deviation (%)",ylim=c(0,50),cex.lab=1.5, cex.axis=1.5)
y <- as.matrix(costs.50)
text(x,y+1,labels=as.character(round(y,digits=2)),cex=1.5)

x <- barplot(costs.100,names.arg=legend,col="lightblue",main="Percentage deviations for 100 jobs", ylab="Deviation (%)",ylim=c(0,50),cex.lab=1.5, cex.axis=1.5)
y <- as.matrix(costs.100)
text(x,y+1,labels=as.character(round(y,digits=2)),cex=1.5)

