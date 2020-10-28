import fanc
import fanc.plotting as fancplot
import logging
import matplotlib
import os
import pybedtools
import re
import seaborn

# import sys

matplotlib.use('agg')
logging.basicConfig(level=logging.INFO)

gd7_nc14_hic = fanc.load(os.path.join("data", "hic", "merged",
                                      "gd7-nc14", "hic",
                                      "gd7-nc14_2kb.hic"), mode="r")
gd7_nc14_hic_plot = fancplot.HicPlot(gd7_nc14_hic, vmin=1e-03,
                                     vmax=1e-01, norm="log",
                                     draw_minor_ticks=False, title="gd7")

Tollrm910_nc14_hic = fanc.load(os.path.join("data", "hic", "merged",
                                            "Tollrm910-nc14", "hic",
                                            "Tollrm910-nc14_2kb.hic"),
                               mode="r")
Tollrm910_nc14_hic_plot = fancplot.HicPlot(Tollrm910_nc14_hic, vmin=1e-03,
                                           vmax=1e-01, norm="log",
                       draw_minor_ticks=False, title="Tollrm910")

Toll10B_nc14_hic = fanc.load(os.path.join("data", "hic", "merged",
                                          "Toll10B-nc14", "hic",
                                          "Toll10B-nc14_2kb.hic"), mode="r")
Toll10B_nc14_hic_plot = fancplot.HicPlot(Toll10B_nc14_hic, vmin=1e-03,
                                         vmax=1e-01, norm="log",
                                         draw_minor_ticks=False,
                                         title="Toll10B")

genes = "external_data/flybase/dmel-all-r6.30.gtf.gz"
genes_plot = fancplot.GenePlot(genes, squash=True, group_by="gene_symbol",
                               aspect=0.15, label_field="gene_symbol",
                               show_labels=False, draw_minor_ticks=False)

rnaseq_dict = {name: os.path.join("external_data", "koenecke_2016_2017", "rnaseq_aligned",
                                  name + "_sorted_filtered_merged_canonical_chrs_rnaseq.bw")
               for name in ["gd7", "tlrm910", "tl10b"]}

h3k27ac_dict = {name: os.path.join("external_data", "koenecke_2016_2017", "chipseq_aligned",
                                   "H3K27ac_" + name + "_sorted_filtered_merged_canonical_chrs.bw")
                for name in ["gd7", "tl10b"]}
h3k27ac_dict["Tollrm910"] = os.path.join("external_data", "extra_chip-seq", "chipseq_aligned",
                                   "H3K27ac_Tollrm910_sorted_filtered_merged_canonical_chrs.bw")

h3k27me3_dict = {name: os.path.join("external_data", "koenecke_2016_2017", "chipseq_aligned",
                                   "H3K27me3_" + name + "_sorted_filtered_merged_canonical_chrs.bw")
                for name in ["gd7", "tl10b"]}
h3k27me3_dict["Tollrm910"] = os.path.join("external_data", "extra_chip-seq", "chipseq_aligned",
                                   "H3K27me3_Tollrm910_sorted_filtered_merged_canonical_chrs.bw")

ins_dict = {name: os.path.join("data", "boundaries", name + "_2kb_8.bw")
            for name in ["gd7-nc14", "Tollrm910-nc14", "Toll10B-nc14", "3-4h"]}

rnaseq_ylim = fancplot.helpers.LimitGroup()
h3k27ac_ylim = fancplot.helpers.LimitGroup()
h3k27me3_ylim = fancplot.helpers.LimitGroup()
polii_ylim = fancplot.helpers.LimitGroup()

polii_chip_late = os.path.join("external_data", "blythe_2015", "aligned",
                               "PolII-pSer5_NC14-late_sorted_filtered_merged_canonical_chrs.bw")

polii_late_plot = fancplot.LinePlot(polii_chip_late, fill=False,
                                    plot_kwargs={'color': "black"},
                                    draw_minor_ticks=False, aspect=0.05,
                                    ylim=polii_ylim, n_yticks=2)

rnaseq_plot_gd7 = fancplot.LinePlot(rnaseq_dict['gd7'], fill=False,
                                    plot_kwargs={'color': "#648fff"},
                                    draw_minor_ticks=False, aspect=0.05,
                                    ylim=rnaseq_ylim, n_yticks=2)

h3k27ac_plot_gd7 = fancplot.LinePlot(h3k27ac_dict['gd7'], fill=False,
                                     plot_kwargs={'color': "#648fff"},
                                     draw_minor_ticks=False, aspect=0.05,
                                     ylim=h3k27ac_ylim, n_yticks=2)
h3k27me3_plot_gd7 = fancplot.LinePlot(h3k27me3_dict['gd7'], fill=False,
                                      plot_kwargs={'color': "#648fff"},
                                      draw_minor_ticks=False, aspect=0.05,
                                      ylim=h3k27me3_ylim, n_yticks=2)

rnaseq_plot_Tollrm910 = fancplot.LinePlot(rnaseq_dict['tlrm910'], fill=False,
                                          plot_kwargs={'color': "#dc267f"},
                                          draw_minor_ticks=False, aspect=0.05,
                                          ylim=rnaseq_ylim, n_yticks=2)

h3k27ac_plot_Tollrm910 = fancplot.LinePlot(h3k27ac_dict['Tollrm910'], fill=False,
                                           plot_kwargs={'color': "#dc267f"},
                                           draw_minor_ticks=False, aspect=0.05,
                                           ylim=h3k27ac_ylim, n_yticks=2)
h3k27me3_plot_Tollrm910 = fancplot.LinePlot(h3k27me3_dict['Tollrm910'], fill=False,
                                            plot_kwargs={'color': "#dc267f"},
                                            draw_minor_ticks=False, aspect=0.05,
                                            ylim=h3k27me3_ylim, n_yticks=2)

rnaseq_plot_toll10b = fancplot.LinePlot(rnaseq_dict['tl10b'], fill=False,
                                        plot_kwargs={'color': "#ffb000"},
                                        draw_minor_ticks=False, aspect=0.05,
                                        ylim=rnaseq_ylim, n_yticks=2)

h3k27ac_plot_toll10b = fancplot.LinePlot(h3k27ac_dict['tl10b'], fill=False,
                                         plot_kwargs={'color': "#ffb000"},
                                         draw_minor_ticks=False, aspect=0.05,
                                         ylim=h3k27ac_ylim, n_yticks=2)
h3k27me3_plot_toll10b = fancplot.LinePlot(h3k27me3_dict['tl10b'], fill=False,
                                          plot_kwargs={'color': "#ffb000"},
                                          draw_minor_ticks=False, aspect=0.05,
                                          ylim=h3k27me3_ylim, n_yticks=2)

gd7_enh = "data/supplementary_tables/gd7_candidate_enhancers.bed"
gd7_enh_plot = fancplot.GenomicFeaturePlot(gd7_enh,
                                           aspect=0.02, color="#648fff",
                                           draw_minor_ticks=False)

Tollrm910_enh = "data/supplementary_tables/Tollrm910_candidate_enhancers.bed"
Tollrm910_enh_plot = fancplot.GenomicFeaturePlot(Tollrm910_enh,
                                                 aspect=0.02, color="#dc267f",
                                                 draw_minor_ticks=False)

toll10b_enh = "data/supplementary_tables/Toll10B_candidate_enhancers.bed"
toll10b_enh_plot = fancplot.GenomicFeaturePlot(toll10b_enh,
                                               aspect=0.02, color="#ffb000",
                                               draw_minor_ticks=False)


def plot_region(name, region, promoter, rnaseq_ylim):
    output_file = os.path.join("figures", "figure_4_panels", name + ".pdf")
    logging.info("Working on %s", name)
    logging.info("Will write output to %s", output_file)

    gd7_v4c = fancplot.Virtual4CPlot(gd7_nc14_hic, viewpoint=promoter,
                                     aspect=0.05, color="#648fff",
                                     draw_minor_ticks=False)
    Tollrm910_v4c = fancplot.Virtual4CPlot(Tollrm910_nc14_hic, viewpoint=promoter,
                                           aspect=0.05, color="#dc267f",
                                           draw_minor_ticks=False)
    Toll10B_v4c = fancplot.Virtual4CPlot(Toll10B_nc14_hic, viewpoint=promoter,
                                         aspect=0.05, color="#ffb000",
                                         draw_minor_ticks=False)

    ha_plot = fancplot.HighlightAnnotation(bed=pybedtools.BedTool(re.sub(":|-", " ", promoter), from_string=True),
                                           plot1=gd7_v4c, plot2=Toll10B_v4c,
                                           plot_kwargs={"color": "gray"})

    plots = [gd7_nc14_hic_plot,
             rnaseq_plot_gd7,
             h3k27ac_plot_gd7, gd7_enh_plot,
             h3k27me3_plot_gd7,

             Tollrm910_nc14_hic_plot,
             rnaseq_plot_Tollrm910,
             h3k27ac_plot_Tollrm910, Tollrm910_enh_plot,
             h3k27me3_plot_Tollrm910,

             Toll10B_nc14_hic_plot,
             rnaseq_plot_toll10b,
             h3k27ac_plot_toll10b, toll10b_enh_plot,
             h3k27me3_plot_toll10b,
             
             gd7_v4c,
             Tollrm910_v4c,
             Toll10B_v4c,
             ha_plot,
             genes_plot
             ]

    with fancplot.GenomicFigure(plots, ticks_last=True) as gfig:
        fig, axes = gfig.plot(region)
        seaborn.despine(ax=axes[15], top=True, right=True)
        seaborn.despine(ax=axes[16], top=True, right=True)
        seaborn.despine(ax=axes[17], top=True, right=True)
        # axes[15].set_ylim([0, 0.02])
        # axes[16].set_ylim([0, 0.02])
        # axes[17].set_ylim([0, 0.02])
        # RNA-seq axes
        axes[1].set_ylim([0, rnaseq_ylim])
        axes[6].set_ylim([0, rnaseq_ylim])
        axes[11].set_ylim([0, rnaseq_ylim])
        # seaborn.despine(ax=axes[4], bottom=True)
        # seaborn.despine(ax=axes[5], bottom=True)
        fig.savefig(output_file)


regions = [
           # housekeeping genes
           ("RpS12", "3L:12,900,000-13,100,000", "3L:13022351-13024350", 30),
           ("eEF1delta", "2L:10,100,000-10,300,000", "2L:10231506-10233505", 30),
           ("x16", "2L:6,800,000-7,000,000", "2L:6919211-6921210", 30),
           ("Nipped-B", "2R:4,600,000-4,800,000", "2R:4728018-4730017", 30),

           # expressed in Toll10B
           ("twi", "2R:22,900,000-23,100,000", "2R:23045321-23047320", 100),  # twi
           ("sna", "2L:15,350,000-15,550,000", "2L:15477261-15479260", 100),  # sna
           ("if", "X:16,700,000-16,900,000", "X:16782435-16784434", 15),   # if
           ("NetA", "X:14,600,000-14,800,000", "X:14652882-14654881", 20),   # NetA, NetB
           # expressed in Tollrm9/10
           ("sog", "X:15,500,000-15,700,000", "X:15625541-15627540", 30),   # sog
           ("brk", "X:7,200,000-7,400,000", "X:7306938-7308937", 30),  # brk
           # expressed in gd7
           ("Doc1", "3L:8,950,000-9,100,000", "3L:9040601-9042600", 20),    # Doc1, Doc2
           ("pnr", "3R:15,950,000-16,150,000", "3R:16033585-16035584", 15),  # pnr
           ("C15", "3R:21,400,000-21,600,000", "3R:21498985-21500984", 15),  # C15
           # example regions
           # ("2L_example", "2L:5,000,000-8,000,000"),  # example region on 2L
           # ("2R_example", "2R:20,000,000-22,000,000"),  # drop in ssim in Toll10B
           # ("3L_example", "3L:13,000,000-15,000,000"),  # drop in ssim in all

           # regions from Ghavi-Helm et al. 2014
           # ap, Abd-b, E2f, pdm2, Con, eya, stumps, Mef2, sli and slp1 genes
           ("ap", "2R:5,600,000-5,800,000", "2R:5725833-5727832", 20),
           ("Abd-B", "3R:16,900,000-17,100,000", "3R:16967575-16969574", 30),
           ("E2f1", "3R:21,500,000-21,700,000", "3R:21659872-21661871", 20),
           ("pdm2", "2L:12,500,000-12,700,000", "2L:12677603-12679602", 20),
           ("Con", "3L:4,900,000-5,100,000", "3L:4975177-4977176", 15),
           ("eya", "2L:6,400,000-6,600,000", "2L:6545977-6547976", 30),
           ("stumps", "3R:14,500,000-14,700,000", "3R:14590619-14592618", 30),
           ("Mef2", "2R:9,800,000-10,000,000", "2R:9957859-9959858", 30),
           ("sli", "2R:15,800,000-16,000,000", "2R:15921119-15923118", 30),
           ("slp1", "2L:3,700,000-3,900,000", "2L:3824674-3826673", 20),
           # additional genes suggested by Mike Levine 
           ("fog", "X:22,800,000-22,900,000", "X:22854195-22856194", 15),
           ("rho", "3L:1,350,000-1,500,000", "3L:1462810-1464809", 15),
           ("vn",  "3L:5,800,000-5,900,000", "3L:5844665-5846664", 20),
           ("pyr", "2R:11,700,000-11,850,000", "2R:11711262-11713261", 15),
           ("ths", "2R:11,700,000-11,850,000", "2R:11789365-11791364", 15),
           ("ind", "3L:15,000,000-15,100,000", "3L:15042925-15044924", 15),
           ("dpp", "2L:2,400,000-2,500,000", "2L:2449192-2451191", 15)
           ]

for name, region, promoter, ylim in regions:
    plot_region(name, region, promoter, ylim)
