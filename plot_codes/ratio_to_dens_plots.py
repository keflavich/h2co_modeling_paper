import sys
import h2co_modeling
import pylab as pl
import itertools

datapath = '/Users/adam/work/h2co/modeling_paper/radex_data/' 
figpath = '/Users/adam/work/h2co/modeling_paper/figures/' 

pl.rcParams['font.size'] = 20

master_linestyles = itertools.cycle(['-','--','-.',':'])
master_linestyles = ['-']*10
master_colors = (['#880000', '#008888', '#CCCCCC']+
                 ["#"+x for x in '348ABD, 7A68A6, A60628, 467821, CF4457, 188487, E24A33'.split(', ')])

#tros = h2co_modeling.SmoothtauModels(datafile=datapath+'troscompt/1-1_2-2_XH2CO=1e-9_troscompt.dat')
faur = h2co_modeling.SmoothtauModels(datafile=datapath+'faure/1-1_2-2_XH2CO_fixed_faure.dat')
#green = h2co_modeling.SmoothtauModels(datafile=datapath+'green/1-1_2-2_XH2CO_fixed_green.dat')


abund = -9
for abund in (-8,-9,-10):

    pl.figure(1)
    pl.clf()
    pl.figure(2)
    pl.clf()

    colors = iter(master_colors)
    linestyles = iter(master_linestyles)
    #for abund in (-8.5,-9,-9.5,-10):
    # Need T=50 models?
    for sigma in (1.0, 2.0):
        tau1,tau2,dens,col = faur.select_data(abund, temperature=20)
        tau,vtau,vtau_ratio = faur.generate_tau_functions(abundance=abund)

        tauratio = vtau_ratio(dens, line1=tau1, line2=tau2, sigma=sigma)
        tauA = vtau(dens, line=tau1, sigma=sigma)
        tauB = vtau(dens, line=tau2, sigma=sigma)

        #ok = np.arange(tauratio.size) > np.argmax(tauratio)

        #def ratio_to_dens(ratio):
        #    inds = np.argsort(tauratio[ok])
        #    return np.interp(ratio, tauratio[ok][inds], dens[ok][inds], np.nan, np.nan)

        pl.figure(1)
        pl.plot(dens,tauratio,label='$\sigma=%0.1f$' % (sigma), linewidth=3, alpha=0.7,
                #linestyle=linestyles.next(),
                color=colors.next())

        pl.figure(2)
        C = colors.next()
        pl.plot(dens,tauA,label='$\sigma=%0.1f$' % (sigma), linewidth=3, alpha=0.7,
                #linestyle=linestyles.next(),
                color=C)
        pl.plot(dens,tauB, linewidth=3, alpha=0.7,
                linestyle='--',
                color=C)

    pl.figure(1)
    pl.plot(dens,tau1/tau2,label='$\delta$', linewidth=3, alpha=0.7,
                linestyle=linestyles.next(),
                color=colors.next())

    pl.figure(2)
    C = colors.next()
    pl.plot(dens,tau1,label='$\delta$', linewidth=3, alpha=0.7,
                linestyle=linestyles.next(),
                color=C)
    pl.plot(dens,tau2, linewidth=3, alpha=0.7,
                linestyle='--',
                color=C)


    pl.figure(1)
    pl.grid()

    pl.axis([0,6,0,13])
    pl.legend(loc='best')
    pl.xlabel(r'Volume-averaged density $\log(n(H_2))$')
    pl.ylabel(r'Ratio $\tau_{1-1}/\tau_{2-2}$')

    pl.savefig(figpath+'tau_ratio_vs_density_thinlimit_sigmavary_Xm{}.pdf'.format(abs(abund)),bbox_inches='tight')

    pl.figure(2)
    pl.grid()

    pl.axis([0,8,0.01,10])
    pl.gca().set_yscale('log')
    pl.legend(loc='best')
    pl.xlabel(r'Volume-averaged density $\log(n(H_2))$')
    pl.ylabel(r'$\tau$')

    pl.savefig(figpath+'tau_vs_density_thinlimit_sigmavary_Xm{}.pdf'.format(abs(abund)),bbox_inches='tight')

pl.show()

