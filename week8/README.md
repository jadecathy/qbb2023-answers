## Command to run chicago
- Rscript runChicago.R raw/PCHIC_Data/GM_rep3.chinput GM3 -d raw/Design --en-feat-list raw/Features/featuresGM.txt -e washU_text

## Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.
- Yes it generally make sense to me. The data represents the enrichment of Promoter-Capture Hi-C (pCHiC) interactions. CTCF encodes proteins binding at chromatin domain boundaries, at enhancers and gene promoters, so it's reasonable that CTCF is enriched. Other enriched genes including H3K4me1 (which is usually enriched at active and primed enhancers), H3K4me3 and H3K27ac (both promote gene activation). Promoter-interacting fragments were also enriched for repressed chromatin marks, such as H3K27me3 and H3K9me3, this is more suprising but may be atributed to Polycomb regulation.

## Top 6 interactions between two promoters
911  chr21  34854620  34868437  .  653  18.64  .   0  ...  34861406                                      AP000302.58   +  chr21  34861480  34868437          DNAJC28   +
234  chr20  24972345  25043735  .  614  17.53  .   0  ...  24985047                                            APMAP   +  chr20  25036380  25043735            ACSS1   +
359  chr20  35888367  36164466  .  589  16.82  .   0  ...  36164466                                BLCAP;NNAT;PPIAP3   +  chr20  35888367  35895684             GHRH   +
877  chr21  33755386  33987743  .  536  15.30  .   0  ...  33987743                             AP000275.65;C21orf59   +  chr21  33755386  33767163   C21orf119;URB1   +
721  chr21  26803999  26939577  .  520  14.85  .   0  ...  26805415                                        LINC00158   +  chr21  26926437  26939577         MIR155HG   +
377  chr20  37045992  37082176  .  514  14.66  .   0  ...  37082176  SNHG11;SNHG17;SNORA60;SNORA71C;SNORA71D;SNORA71   +  chr20  37045992  37055959  SNHG17;SNORA71B   +

## Top 6 interactions between promoter and enhancer sets
614  chr20  55957140  56074932  .  1000  28.52  .   0  chr20  55957140  55973022        RBM38;RP4-800J21.3  +  chr20  56067414  56074932  .  -
399  chr20  39640890  39662867  .   601  17.15  .   0  chr20  39656513  39662867                      TOP1  +  chr20  39640890  39647373  .  -
765  chr21  28223187  30117523  .   582  16.62  .   0  chr21  30112950  30117523                 RNU6-872P  +  chr21  28223187  28225329  .  -
726  chr21  26790966  26939577  .   575  16.41  .   0  chr21  26926437  26939577                  MIR155HG  +  chr21  26790966  26793953  .  -
286  chr20  32041602  32262823  .   573  16.36  .   0  chr20  32254019  32262823  ACTL10;NECAB3;RP1-63M2.5  +  chr20  32041602  32060758  .  -
727  chr21  26793954  26939577  .   570  16.26  .   0  chr21  26926437  26939577                  MIR155HG  +  chr21  26793954  26795680  .  -

## Does it make sense for this gene to be interacting with enhancers in GM12878? 
- Yes. Top1 encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. It is very likely that it is actively interacting with enhancer domains for regulation. RBM38 encodes RNA binding motif protein and enables mRNA 3'-UTR binding activity, so it is also likely.