library(ggplot2) # install these packages
Args <- commandArgs()
# Data loading, calculation
setwd(Args[6]) # data path
da <- read.csv(Args[7])
names <- da[,1]
da <- as.matrix(da[,-1])
row_sum <- apply(da,1,sum)
col_sum <- apply(da,2,sum)
da_ratio <- da/outer(sqrt(row_sum),sqrt(col_sum))
#da_weight <- da/outer(row_sum,rep(1,length(col_sum)))
da_ratio[is.nan(da_ratio)] <- 0 
rownames(da_ratio) <- names
#heatmap(da)

# csv output

write.csv(da_ratio, file=Args[8],row.names=TRUE)
#write.csv(da_weight, file="da_weight.csv",row.names=FALSE)


da_ratio <- read.csv(Args[8],stringsAsFactors=FALSE)
names <- da_ratio[,1]
da_ratio <- as.matrix(da_ratio[,-1])
rownames(da_ratio) <- names

pdf(Args[9],width=30,height=30,family="GB1")
heatmap(da_ratio)


# Plot

hc <- hclust(dist(da_ratio), "ave")
pdf(Args[10],width=50,height=20,family="GB1")
plot(hc)


hc2<- hclust(dist(t(da_ratio)), "ave")
pdf(Args[11],width=50,height=20,family="GB1")
plot(hc2)
cluster_plot<-heatmap.2(ratio, col=redblue(100), scale="row",
                        key=TRUE, symkey=FALSE, density.info="none", trace="none", cexRow=0.5)

