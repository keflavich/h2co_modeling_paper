import h2co_modeling
import pylab as pl

datapath = '/Users/adam/work/h2co/modeling_paper/radex_data/' 
figpath = '/Users/adam/work/h2co/modeling_paper/figures/' 

master_linestyles = ['-','--',':']*10
master_colors = (['#880000', '#008888', '#CCCCCC']+
                 ["#"+zz for zz in '348ABD, 7A68A6, A60628, 467821, CF4457, 188487, E24A33'.split(', ')])

tros = h2co_modeling.SmoothtauModels(datafile=datapath+'troscompt/1-1_2-2_XH2CO=1e-9_troscompt.dat')
faur = h2co_modeling.SmoothtauModels(datafile=datapath+'faure/1-1_2-2_XH2CO_fixed_faure.dat')
green = h2co_modeling.SmoothtauModels(datafile=datapath+'green/1-1_2-2_XH2CO_fixed_green.dat')

linestyles = iter(master_linestyles)
colors = iter(master_colors)

sigma = 0.0

for ii,temperature in enumerate((20,50,80)):
    pl.figure(ii+1)
    pl.clf()
    pl.suptitle("T = %iK" % temperature)


    for abund in (-10,-9,-8):
        col = colors.next()
        ax1 = pl.subplot(3,1,1)
        for pub,ls in zip((tros,faur,green),('-','--',':')):
            pub.plot_x_vs_y('dens','tau11',linewidth=3,alpha=0.7,color=col,axis=ax1,
                             temperature=temperature, abundance=abund,
                             sigma=sigma,
                             linestyle=ls)
                         #label='X=%0.2g' % (abund,))
        ax1.set_yscale('log')
        ax1.set_xlim(2,7)
        ax1.set_ylim(1e-3,1e2)
        ax2 = pl.subplot(3,1,2)
        for pub,ls in zip((tros,faur,green),('-','--',':')):
            pub.plot_x_vs_y('dens','tau22',linewidth=3,alpha=0.7,color=col,axis=ax2,abundance=abund,
                             temperature=temperature,
                             sigma=sigma,
                             linestyle=ls,)
        ax2.set_yscale('log')
        ax2.set_xlim(2,8)
        ax2.set_ylim(1e-4,1e2)

        ax3 = pl.subplot(3,1,3)
        for pub,ls in zip((tros,faur,green),('-','--',':')):
            pub.plot_x_vs_y('dens','tauratio',linewidth=3,alpha=0.7,color=col,axis=ax3,abundance=abund,
                             temperature=temperature,
                             sigma=sigma,
                             linestyle=ls,)
            pub.plot_x_vs_y('dens','oitaruat',linewidth=1,alpha=0.7,color=col,axis=ax3,abundance=abund,
                             temperature=temperature,
                             sigma=sigma,
                             linestyle=ls,)
        ax3.set_xlim(2,7)
        ax3.set_ylim(0,15)

    # merge the two (now three) plots
    ax1.set_xticklabels([])
    ax1.set_yticklabels([x.get_text() for x in ax1.get_yticklabels()[1:]])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([x.get_text() for x in ax1.get_yticklabels()[1:]])
    pl.subplots_adjust(hspace=0.0)

    ax1.plot([],color='k',linewidth=2,alpha=0.8,label='Troscompt')
    ax1.plot([],color='k',linewidth=2,alpha=0.8,label='Faure',linestyle='--')

    ax1.legend(loc='upper left',fontsize=14)
    ax3.set_xlabel("log$_{10}(n_{H_2})$ cm$^{-3}$")
    ax1.set_ylabel(r'o-H$_2$CO $\tau_{1-1}$')
    ax2.set_ylabel(r'o-H$_2$CO $\tau_{2-2}$')
    ax3.set_ylabel(r'Ratio')

    pl.savefig(figpath+"Faure_Troscompt_compare_T=%i.pdf" % temperature)

pl.show()
