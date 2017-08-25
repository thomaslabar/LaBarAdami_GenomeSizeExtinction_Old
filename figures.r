library(readr)
library(ggplot2)
library(plyr)

setwd("Documents/Research/driftextinction")

data <- read_csv("data.csv")
data_original <- data[data$Treatment == "repeat",]
data_lowmut <- data[data$Treatment == "lowmut",]
data_fixedmut <- data[data$Treatment == "fixedmut",]
data_notraits <- data[data$Treatment == "notraits",]
data_fixedlength <- data[data$Treatment == "fixedlength",]

data_lethalmeasure <- read_csv("data_lethalmeasure.csv")
data_lethalmeasure_time <- read_csv("data_lethalmeasure_time.csv")
data_lethalmeasure_varmut <- read_csv("data_lethalmeasure_varmut.csv")

#####
#Code for Table 1
#####
extinct_data <- data[data$Extinction == 1,]
count(extinct_data,"Treatment")

#####
# Surviving vs. Extinct Genome Size for Variable Mutation Rate Populations
#####
median(data_original[data_original$Extinction == 1,]$FinalGenomeSize) #Extinct
median(data_original[data_original$Extinction == 0,]$FinalGenomeSize) #Surviving
wilcox.test(data_original[data_original$Extinction == 1,]$FinalGenomeSize,
            data_original[data_original$Extinction == 0,]$FinalGenomeSize,
            alternative="greater")

#####
#Code for Figure 1
#####
data_original$Extinction <- factor(data_original$Extinction)
ggplot(data_original, aes(Extinction, FinalGenomeSize)) + 
  geom_boxplot() + 
  geom_jitter(width = 0.2) + 
  theme_bw(base_size=18) + 
  scale_x_discrete(labels=c("Surviving\nPopulations","Extinct\nPopulations")) + 
  ylim(0, 500) +
  ylab("Genome Size (instructions)") + xlab("") +
  theme(
    plot.background = element_blank()
    ,panel.grid.major = element_blank()
    ,panel.grid.minor = element_blank()
    ,panel.border = element_blank()
  ) +
  theme(axis.line.x = element_line(color="black", size = 0.25),
        axis.line.y = element_line(color="black", size = 0.25))
ggsave("manuscript/figure1.pdf",dpi=600,height=4,width=6)

#####
#Code for Figure 2
#####
ggplot(data_lethalmeasure_time, aes(Generation, DominantGenomeSize)) + 
  geom_line(aes(group = Replicate, linetype = factor(Extinct))) + 
  theme_bw(base_size=18) + 
  ylab("Genome Size (instructions)") + xlab("Generation") +
  theme(
    plot.background = element_blank(),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank()
    ,legend.position="none"
  ) +
  theme(axis.line.x = element_line(color="black", size = 0.25),
        axis.line.y = element_line(color="black", size = 0.25))
ggsave("manuscript/figure2.pdf",dpi=600,height=4,width=6)

#####
# Genome Size for Variable Mutation Rate vs No Trait Evolution Populations
#####
median(data_original$FinalGenomeSize) #Variable Mutation Rate
median(data_notraits$FinalGenomeSize) #No Trait Evolution
wilcox.test(data_original$FinalGenomeSize,
            data_notraits$FinalGenomeSize,
            alternative="two.sided")

#####
# U_lethal for Surviving vs Extinct Populations
#####
median(data_lethalmeasure[data_lethalmeasure$Extinction == 1,]$ProbLethal) #Extinct
median(data_lethalmeasure[data_lethalmeasure$Extinction == 0,]$ProbLethal) #Surviving
wilcox.test(data_lethalmeasure[data_lethalmeasure$Extinction == 1,]$ProbLethal,
            data_lethalmeasure[data_lethalmeasure$Extinction == 0,]$ProbLethal,
            alternative="greater")

#####
# Code for Figure 3
#####
data_lethalmeasure$Extinction <- factor(data_lethalmeasure$Extinction)
ggplot(data_lethalmeasure, aes(Extinction, ProbLethal)) + 
  geom_boxplot() + 
  geom_jitter(width = 0.2) + 
  theme_bw(base_size=18) + 
  ylim(0,0.5) +
  scale_x_discrete(labels=c("Surviving\nPopulations","Extinct\nPopulations")) + 
  ylab("Lethal Mutation Rate (/genome/generation)") + xlab("") +
  theme(
    plot.background = element_blank()
    ,panel.grid.major = element_blank()
    ,panel.grid.minor = element_blank()
    ,panel.border = element_blank()
  ) +
  theme(axis.line.x = element_line(color="black", size = 0.25),
        axis.line.y = element_line(color="black", size = 0.25),
        axis.title.y = element_text(size=12),
        axis.text.y = element_text(size=12))
ggsave("manuscript/figure3.pdf",dpi=600,height=4,width=6)

#####
# Code for Figure 4
#####
ggplot(data_lethalmeasure_varmut, aes(LethalMutationRate, NumExtinctions, shape = factor(GenomeSize))) + 
  geom_line(aes(group = GenomeSize)) + 
  #geom_point(aes(shape = GenomeSize)) +
  geom_point() +
  scale_shape_manual(values = c(0,1,2,3,4), name = "", 
                     labels=c(" L = 16", " L = 32", " L = 50", " L = 176", " L = 208")) +
  theme_bw(base_size=18) + 
  ylab("Extinct Populations") + xlab("Lethal Mutation Rate (/genome/generation)") +
  xlim(0, 4) +
  labs(linetype='custom title') +
  theme(
    plot.background = element_blank(),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank()
    #,legend.position="none"
  ) +
  theme(axis.line.x = element_line(color="black", size = 0.25),
        axis.line.y = element_line(color="black", size = 0.25),
        axis.title.x = element_text(size=12),
        axis.text.x = element_text(size=12))
ggsave("manuscript/figure4.pdf",dpi=600,height=4,width=6)

#####
# Correlation between number of lethal mutations and genome size
#####
cor.test(data_lethalmeasure$GenomeSize,data_lethalmeasure$NumLethal,
         method = "pearson")

#####
# Code for Figure 5
#####
ggplot(data_lethalmeasure, aes(GenomeSize, NumLethal)) + 
  geom_point(shape=19) +
  xlim(0,250) + 
  theme_bw(base_size=18) + 
  ylab("Lethal Mutations") + xlab("Genome Size (instructions)") +
  theme(
    plot.background = element_blank()
    ,panel.grid.major = element_blank()
    ,panel.grid.minor = element_blank()
    ,panel.border = element_blank()
  ) +
  theme(axis.line.x = element_line(color="black", size = 0.25),
        axis.line.y = element_line(color="black", size = 0.25))
ggsave("manuscript/figure5.pdf",dpi=600,height=4,width=6)

