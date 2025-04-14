import os
import sys
import ROOT
import uproot
import itertools
import numpy as np
import pandas as pd
import mplhep as hep
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from correctionlib.schemav2 import Binning, Category, Correction, CorrectionSet
import correctionlib.schemav2 as cs

data  = ["EGamma"]
mc    = ["DY_Electron"]
eras  = ["Run2024"]
labels = ["Ele"]

lumi = 109.0
com = 13.6

variables = ["pt", "pt_eta", "eta"] 
triggers  = {
    "Muon"   : ["IsoMu24", "Mu17_Mu8_leg1", "Mu17_Mu8_leg2", "Mu12_Ele23_Muonleg", "Mu23_Ele12_Muonleg", "Mu12_Ele23_Muonleg_Iso", "Mu23_Ele12_Muonleg_Iso"], 
    "EGamma" : ["Ele30", "Ele23_Ele12_leg1", "Ele23_Ele12_leg2"],
}


###########
########### Auxiliary functions
########### 

def generateClopperPearsonInterval(effs, nums, dens, variableName):

    effsD = effs * 0
    effsU = effs * 0

    confidenceLevel = 0.68
    alpha = 1 - confidenceLevel

    for i in range(len(effs)):

        if variableName == "pt_eta":
            for j in range(len(effs[i])):
                
                num = nums[i,j]
                den = dens[i,j]
                eff = effs[i,j]

                if den <= 0.0 or num <= 0.0:
                    effsD[i,j] = eff
                    effsU[i,j] = eff
                    continue

                lowerLimit = round(ROOT.Math.beta_quantile(alpha/2,num,den-num + 1),4)
                if num==den:
                    upperLimit=1
                else:
                    upperLimit = round(ROOT.Math.beta_quantile(1-alpha/2,num + 1,den-num),4)
                    
                effsD[i,j] = lowerLimit
                effsU[i,j] = upperLimit

        else:
        
            num = nums[i]
            den = dens[i]
            eff = effs[i]

            if den <= 0.0 or num <= 0.0:
                effsD[i] = eff
                effsU[i] = eff
                continue
            
            lowerLimit = round(ROOT.Math.beta_quantile(alpha/2,num,den-num + 1),4)
            if num==den:
                upperLimit=1
            else:
                upperLimit = round(ROOT.Math.beta_quantile(1-alpha/2,num + 1,den-num),4)
                
            effsD[i] = lowerLimit
            effsU[i] = upperLimit

    return effsD,effsU

def build_schema_recursively(dim, index):
    # If we reach recursion bottom, build and return the systematics node

    if dim == dimensions + 1:
        keys, content = [], []
        for syst, value in all_systematics[index].items():
            keys.append(syst)
            syst = syst if syst != "value" else "nominal"
            content.append({"key": syst, "value": value})
        return cs.Category(
            nodetype="category", input="systematic", content=content
        )

    # If not, build a binning node
    edges = list(map(float, binning[bin_vars[dim - 1]]))
    content = [
        build_schema_recursively(
            dim + 1, tuple(list(index)[0 : dim - 1] + [i] + list(index)[dim:])
        )
        for i in indices[dim - 1]
    ]
    return cs.Binning(        
            nodetype="binning",
            input=bin_vars[dim - 1],
            edges=edges,
            flow="error",
            content=content,        
    )

### ----------------------------------------------------------------------------



dfs_to_json = {}

for i in range(len(data)):

    print("-----------------------------")
    print("")
    print("       RUN TRIGGER SF        ")
    print("")
    print("-----------------------------")
    print("\n")
    
    dataset    = data[i]
    simulation = mc[i]
    era        = eras[i]
    label      = labels[i]
    
    file_data_nominal    = uproot.open(f"efficiency_{dataset}_{era}_nominal{label}.root")
    file_data_TagPt_up   = uproot.open(f"efficiency_{dataset}_{era}_TagPt_up{label}.root")
    file_data_TagPt_down = uproot.open(f"efficiency_{dataset}_{era}_TagPt_down{label}.root")
    file_data_Zmass_up   = uproot.open(f"efficiency_{dataset}_{era}_Zmass_up{label}.root")
    file_data_Zmass_down = uproot.open(f"efficiency_{dataset}_{era}_Zmass_down{label}.root")
    
    file_mc_nominal    = uproot.open(f"efficiency_{simulation}_{era}_nominal{label}.root")
    file_mc_TagPt_up   = uproot.open(f"efficiency_{simulation}_{era}_TagPt_up{label}.root")
    file_mc_TagPt_down = uproot.open(f"efficiency_{simulation}_{era}_TagPt_down{label}.root")
    file_mc_Zmass_up   = uproot.open(f"efficiency_{simulation}_{era}_Zmass_up{label}.root")
    file_mc_Zmass_down = uproot.open(f"efficiency_{simulation}_{era}_Zmass_down{label}.root")
           
    for wp in triggers[dataset]:

        isoLabel = ""
        wp_num = wp
        wp_den = wp
        if wp.endswith("_Iso"):
            wp_den = wp.split("_Iso")[0]
            wp_num = wp.split("_Iso")[0]
            isoLabel = "_Iso"
        
        print("Doing working point: " + wp)
        
        for variable in variables: 
            
            histo_data_nominal_total    = file_data_nominal[f"{wp_den}_{variable}_total"]
            histo_data_TagPt_up_total   = file_data_TagPt_up[f"{wp_den}_{variable}_total"]
            histo_data_TagPt_down_total = file_data_TagPt_down[f"{wp_den}_{variable}_total"]
            histo_data_Zmass_up_total   = file_data_Zmass_up[f"{wp_den}_{variable}_total"]
            histo_data_Zmass_down_total = file_data_Zmass_down[f"{wp_den}_{variable}_total"]
            
            histo_mc_nominal_total    = file_mc_nominal[f"{wp_den}_{variable}_total"]
            histo_mc_TagPt_up_total   = file_mc_TagPt_up[f"{wp_den}_{variable}_total"]
            histo_mc_TagPt_down_total = file_mc_TagPt_down[f"{wp_den}_{variable}_total"]
            histo_mc_Zmass_up_total   = file_mc_Zmass_up[f"{wp_den}_{variable}_total"]
            histo_mc_Zmass_down_total = file_mc_Zmass_down[f"{wp_den}_{variable}_total"]
            
            histo_data_nominal_pass    = file_data_nominal[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_data_TagPt_up_pass   = file_data_TagPt_up[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_data_TagPt_down_pass = file_data_TagPt_down[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_data_Zmass_up_pass   = file_data_Zmass_up[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_data_Zmass_down_pass = file_data_Zmass_down[f"{wp_num}_{variable}{isoLabel}_pass"]
            
            histo_mc_nominal_pass    = file_mc_nominal[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_mc_TagPt_up_pass   = file_mc_TagPt_up[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_mc_TagPt_down_pass = file_mc_TagPt_down[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_mc_Zmass_up_pass   = file_mc_Zmass_up[f"{wp_num}_{variable}{isoLabel}_pass"]
            histo_mc_Zmass_down_pass = file_mc_Zmass_down[f"{wp_num}_{variable}{isoLabel}_pass"]
            
            
            eff_data_nominal    = np.nan_to_num(histo_data_nominal_pass.values()    / histo_data_nominal_total.values())
            eff_data_nominalD, eff_data_nominalU = generateClopperPearsonInterval(eff_data_nominal, histo_data_nominal_pass.values(),histo_data_nominal_total.values(), variable)
            #eff_data_nominalD = abs(eff_data_nominal-eff_data_nominalD)
            #eff_data_nominalU =	abs(eff_data_nominal-eff_data_nominalU)            
            
            eff_data_TagPt_up   = np.nan_to_num(histo_data_TagPt_up_pass.values()   / histo_data_TagPt_up_total.values())
            eff_data_TagPt_down = np.nan_to_num(histo_data_TagPt_down_pass.values() / histo_data_TagPt_down_total.values())
            eff_data_Zmass_up   = np.nan_to_num(histo_data_Zmass_up_pass.values()   / histo_data_Zmass_up_total.values())
            eff_data_Zmass_down = np.nan_to_num(histo_data_Zmass_down_pass.values() / histo_data_Zmass_down_total.values())
            
            eff_mc_nominal    = np.nan_to_num(histo_mc_nominal_pass.values()    / histo_mc_nominal_total.values())
            eff_mc_nominalD, eff_mc_nominalU = generateClopperPearsonInterval(eff_mc_nominal, histo_mc_nominal_pass.values(),histo_mc_nominal_total.values(), variable)
            #eff_mc_nominalD = abs(eff_mc_nominal-eff_mc_nominalD)
            #eff_mc_nominalU = abs(eff_mc_nominal-eff_mc_nominalU)
            
            eff_mc_TagPt_up   = np.nan_to_num(histo_mc_TagPt_up_pass.values()   / histo_mc_TagPt_up_total.values())
            eff_mc_TagPt_down = np.nan_to_num(histo_mc_TagPt_down_pass.values() / histo_mc_TagPt_down_total.values())
            eff_mc_Zmass_up   = np.nan_to_num(histo_mc_Zmass_up_pass.values()   / histo_mc_Zmass_up_total.values())
            eff_mc_Zmass_down = np.nan_to_num(histo_mc_Zmass_down_pass.values() / histo_mc_Zmass_down_total.values())

            Path("TriggerResults/plots").mkdir(parents=True, exist_ok=True)
            
            if variable == "pt_eta":
                
                eta_axis = histo_data_nominal_total.to_hist().axes[0].edges
                pt_axis = histo_data_nominal_total.to_hist().axes[1].edges
                
                sf      = eff_data_nominal * 0
                sf_syst = eff_data_nominal * 0
                sf_stat = eff_data_nominal * 0
                
                counter = 0
                
                sf_save      = np.ones(eff_data_nominal.size)
                sf_stat_save = np.zeros(eff_data_nominal.size)
                sf_syst_save = np.zeros(eff_data_nominal.size)

                eta_low  = np.zeros(eff_data_nominal.size)
                eta_high = np.zeros(eff_data_nominal.size)

                pt_low  = np.zeros(eff_data_nominal.size)
                pt_high = np.zeros(eff_data_nominal.size)
                
                for ieta in range(len(eta_axis)-1):
                    for ipt in range(len(pt_axis)-1):
 
                        eta_low[counter]  = eta_axis[ieta]
                        eta_high[counter] = eta_axis[ieta+1]
        
                        pt_low[counter]  = pt_axis[ipt]
                        pt_high[counter] = pt_axis[ipt+1]

                        dataEff       = eff_data_nominal[ieta, ipt]
                        mcEff         = eff_mc_nominal[ieta, ipt]
                        
                        dataErrD = abs(dataEff - eff_data_nominalD[ieta, ipt])
                        dataErrU = abs(dataEff - eff_data_nominalU[ieta, ipt])
                        mcErrD   = abs(mcEff - eff_mc_nominalD[ieta, ipt])
                        mcErrU   = abs(mcEff - eff_mc_nominalU[ieta, ipt])                        
                        
                        sf_err = 0.0
                        
                        if mcEff:
                            sf[ieta, ipt] = dataEff / mcEff
                        
                        if dataEff and mcEff:
                            dataErr = max(dataErrD, dataErrU)
                            mcErr = max(mcErrD, mcErrU)
                            sf_err = sf[ieta, ipt] * ((dataErr / dataEff)**2 + (mcErr / mcEff)**2)**0.5
                                
                        sf_stat[ieta, ipt] = sf_err
                        
                        dataEff_TagPt_up       = eff_data_TagPt_up[ieta, ipt]
                        mcEff_TagPt_up         = eff_mc_TagPt_up[ieta, ipt]
                        
                        sf_TagPt_up = sf[ieta, ipt]
                        if mcEff_TagPt_up:
                            sf_TagPt_up = dataEff_TagPt_up / mcEff_TagPt_up
                        
                        dataEff_TagPt_down       = eff_data_TagPt_down[ieta, ipt]
                        mcEff_TagPt_down         = eff_mc_TagPt_down[ieta, ipt]
                        
                        sf_TagPt_down = sf[ieta, ipt]
                        if mcEff_TagPt_down:
                            sf_TagPt_down = dataEff_TagPt_down / mcEff_TagPt_down
                        
                        dataEff_Zmass_up       = eff_data_Zmass_up[ieta, ipt]
                        mcEff_Zmass_up         = eff_mc_Zmass_up[ieta, ipt]
                        
                        sf_Zmass_up = sf[ieta, ipt]
                        if mcEff_Zmass_up:
                            sf_Zmass_up = dataEff_Zmass_up / mcEff_Zmass_up
                        
                        dataEff_Zmass_down       = eff_data_Zmass_down[ieta, ipt]
                        mcEff_Zmass_down         = eff_mc_Zmass_down[ieta, ipt]
                        
                        sf_Zmass_down = sf[ieta, ipt]
                        if mcEff_Zmass_down:
                            sf_Zmass_down = dataEff_Zmass_down / mcEff_Zmass_down

                        
                        if abs(sf_TagPt_up - sf[ieta, ipt])>sf_err:
                            sf_syst[ieta, ipt] += abs(sf_TagPt_up - sf[ieta, ipt])**2
                            
                        if abs(sf_TagPt_down - sf[ieta, ipt])>sf_err:
                            sf_syst[ieta, ipt] += abs(sf_TagPt_down - sf[ieta, ipt])**2
                            
                        if abs(sf_Zmass_up - sf[ieta, ipt])>sf_err:
                            sf_syst[ieta, ipt] += abs(sf_Zmass_up - sf[ieta, ipt])**2
                            
                        if abs(sf_Zmass_down - sf[ieta, ipt])>sf_err:
                            sf_syst[ieta, ipt] += abs(sf_Zmass_down - sf[ieta, ipt])**2

                        sf_syst[ieta, ipt] = sf[ieta, ipt]*(sf_syst[ieta, ipt]**0.5)

                        sf_save[counter]      = sf[ieta, ipt]
                        sf_stat_save[counter] = sf_stat[ieta, ipt]
                        sf_syst_save[counter] = sf_syst[ieta, ipt]

                        counter += 1
                        
                ## convert to json
                
                tmpDict = {
                    "etaBin_low": eta_low,
                    "etaBin_high": eta_high,
                    "ptBin_low": pt_low,
                    "ptBin_high": pt_high,
                    "value": sf_save,
                    "stat": sf_stat_save,
                    "syst": sf_syst_save,
                }
                df = pd.DataFrame(tmpDict)
                df = (
                    df.drop_duplicates()
                )
                dfs_to_json[wp] = df
                
                ####### Make plots - SF
                
                hep.style.use("CMS")
                fig, ax = plt.subplots()
                hep.cms.label("Preliminary", ax=ax, data=True, com=com, loc=0)                
                hep.cms.lumitext(f"   {lumi} $fb^{-1}$                    ", ax=ax)
                
                sfPlot = ax.pcolormesh(
                    histo_data_nominal_total.to_hist().axes[0].edges, 
                    histo_data_nominal_total.to_hist().axes[1].edges, 
                    sf.T,
                    vmin=0.6, vmax=1.4
                )
                
                divider = make_axes_locatable(ax)
                cax = divider.append_axes('right', size='5%', pad=0.05)
                fig.colorbar(sfPlot, cax=cax, orientation='vertical')
                
                ax.set_ylabel("pT")
                ax.set_xlabel("eta")

                for (i, j), z in np.ndenumerate(sf.T):
                    ax.text(histo_data_nominal_total.to_hist().axes[0].centers[j],
                            histo_data_nominal_total.to_hist().axes[1].centers[i],
                            '{:0.3f}'.format(round(abs(z), 3)), ha='center', va='center', size=10, color='k')

                
                plt.savefig(f"TriggerResults/plots/scale_factor_{wp}_pt_eta.pdf")
                plt.savefig(f"TriggerResults/plots/scale_factor_{wp}_pt_eta.png")

                ax.text(
                    0.05, 0.95,
                    f"{wp}",
                    fontsize=20,
                    fontweight="bold",
                    fontproperties="Tex Gyre Heros:italic",
                    transform = ax.transAxes
                )
                
                plt.clf()
                plt.close()
                
                hep.style.use("CMS")
                fig, ax = plt.subplots()
                hep.cms.label("Preliminary", ax=ax, data=True, com=com, loc=0)                
                hep.cms.lumitext(f"   {lumi} $fb^{-1}$                    ", ax=ax)
                
                sfPlot = ax.pcolormesh(
                    histo_data_nominal_total.to_hist().axes[0].edges, 
                    histo_data_nominal_total.to_hist().axes[1].edges, 
                    eff_data_nominal.T,
                    vmin=0.6, vmax=1.
                )
                
                divider = make_axes_locatable(ax)
                cax = divider.append_axes('right', size='5%', pad=0.05)
                fig.colorbar(sfPlot, cax=cax, orientation='vertical')
                
                ax.set_ylabel("pT")
                ax.set_xlabel("eta")

                for (i, j), z in np.ndenumerate(eff_data_nominal.T):
                    ax.text(histo_data_nominal_total.to_hist().axes[0].centers[j],
                            histo_data_nominal_total.to_hist().axes[1].centers[i],
                            '{:0.3f}'.format(round(abs(z), 3)), ha='center', va='center', size=10, color='k')

                ax.text(
                    0.05, 0.95,
                    f"{wp}",
                    fontsize=20,
                    fontweight="bold",
                    fontproperties="Tex Gyre Heros:italic",
                    transform = ax.transAxes
                )
                    
                plt.savefig(f"TriggerResults/plots/EffData_{wp}_pt_eta.pdf")
                plt.savefig(f"TriggerResults/plots/EffData_{wp}_pt_eta.png")
                
                plt.clf()
                plt.close()
                
                hep.style.use("CMS")
                fig, ax = plt.subplots()
                hep.cms.label("Preliminary", ax=ax, data=True, com=com, loc=0)                
                hep.cms.lumitext(f"   {lumi} $fb^{-1}$                    ", ax=ax)
                
                sfPlot = ax.pcolormesh(
                    histo_mc_nominal_total.to_hist().axes[0].edges, 
                    histo_mc_nominal_total.to_hist().axes[1].edges, 
                    eff_mc_nominal.T,
                    vmin=0.6, vmax=1.
                )
                
                divider = make_axes_locatable(ax)
                cax = divider.append_axes('right', size='5%', pad=0.05)
                fig.colorbar(sfPlot, cax=cax, orientation='vertical')
                
                ax.set_ylabel("pT")
                ax.set_xlabel("eta")                 

                for (i, j), z in np.ndenumerate(eff_mc_nominal.T):
                    ax.text(histo_mc_nominal_total.to_hist().axes[0].centers[j],
                            histo_mc_nominal_total.to_hist().axes[1].centers[i],
                            '{:0.3f}'.format(round(abs(z), 3)), ha='center', va='center', size=10, color='k')

                ax.text(
                    0.05, 0.95,                 
                    f"{wp}",          
                    fontsize=20,                
                    fontweight="bold",
                    fontproperties="Tex Gyre Heros:italic",
                    transform = ax.transAxes
                )
                    
                plt.savefig(f"TriggerResults/plots/EffMC_{wp}_pt_eta.pdf")
                plt.savefig(f"TriggerResults/plots/EffMC_{wp}_pt_eta.png")

                plt.close()
                
            else:
                
                hep.style.use("CMS")
                fig, ax = plt.subplots()
                hep.cms.label("Preliminary", ax=ax, data=True, com=com, loc=0)                
                hep.cms.lumitext(f"   {lumi} $fb^{-1}$                      ", ax=ax)
                
                xaxis = histo_data_nominal_total.to_hist().axes[0].centers
                xerrs = [
                    histo_data_nominal_total.to_hist().axes.widths[0]/2,
                    histo_data_nominal_total.to_hist().axes.widths[0]/2,
                ]
                yerrs = [
                    abs(eff_data_nominal-eff_data_nominalU), 
                    abs(eff_data_nominal-eff_data_nominalD)
                ]

                plt.errorbar(xaxis, eff_data_nominal, xerr=xerrs, yerr=yerrs, 
                             color='#5790fc', label = f"Data {era}",
                             marker='.', markersize=10.0, linewidth=1., linestyle='none', 
                             capsize=5, fillstyle='none'
                            )
        
                xaxis = histo_mc_nominal_total.to_hist().axes[0].centers
                xerrs_mc = [
                    histo_mc_nominal_total.to_hist().axes.widths[0]/2,
                    histo_mc_nominal_total.to_hist().axes.widths[0]/2,
                ]
                yerrs_mc = [
                    abs(eff_mc_nominal-eff_mc_nominalU), 
                    abs(eff_mc_nominal-eff_mc_nominalD)
                ]
                
                plt.errorbar(xaxis, eff_mc_nominal, xerr=xerrs_mc, yerr=yerrs_mc, 
                             color='#f89c20', label = f"MC",
                             marker='.', markersize=10.0, linewidth=1., linestyle='none', 
                             capsize=5, fillstyle='none'
                            )
                
                ax.set_ylabel("Efficiency")
                ax.set_xlabel(f"{variable}")

                ax.text(
                    0.05, 0.95,
                    f"{wp}",
                    fontsize=20,
                    fontweight="bold",
                    fontproperties="Tex Gyre Heros:italic",
                    transform = ax.transAxes
                )

                plt.legend()
                
                plt.savefig(f"TriggerResults/plots/EffData_{wp}_{variable}.pdf")
                plt.savefig(f"TriggerResults/plots/EffData_{wp}_{variable}.png")                

                plt.close()
    
    
    
    ### start json production
    
    binning = {}
    systematics = ["stat", "syst"]
    variableLabels = ["eta", "pt"]
    outname = f"TriggerResults/scale_factors_{dataset}_{era}.json"
    corrs = []

    print("\n")
    print("The new json file will be stored at: \n")
    print(outname)
    
    for key in dfs_to_json:
        df = dfs_to_json[key]
        for var in variableLabels:
            binning[var] = np.unique(
                list(dfs_to_json[key][var + "Bin_low"].values) + list(dfs_to_json[key][var + "Bin_high"].values)
            )         
        
        indices = [
            list(range(1, len(binning[variableLabel]))) for variableLabel in variableLabels
        ]
    
        output = {}
    
        all_systematics = {}
        for index in itertools.product(*indices):
            subVarKeys = [
                "{}:[{},{}]".format(
                    variableLabels[i],
                    binning[variableLabels[i]][ind - 1],
                    binning[variableLabels[i]][ind],
                )
                for i, ind in enumerate(index)
            ]
            
            _out = output
    
            _out["binning"] = [
                {
                    "variable": vl,
                    "binning": binning[vl].tolist(),
                }
                for vl in variableLabels
            ]
    
            for subVarKey in subVarKeys:
                if subVarKey not in _out:
                    _out[subVarKey] = {}
                _out = _out[subVarKey]
    
            eff_bin = dfs_to_json[key]
    
            for var in variableLabels:
                eff_bin = eff_bin.loc[
                    eff_bin[var + "Bin_high"]
                    == binning[var][list(index)[variableLabels.index(var)]]
                ]
                
            _out["value"] = eff_bin["value"]
    
            if systematics != None:
                for sys in systematics:
                    _out[sys] = eff_bin[sys]
    
            all_systematics[index] = _out.copy()
                
        bin_vars = list(binning.keys())
        dimensions = len(binning)
    
        inputs = [
            cs.Variable(name=bin_var, type="real", description=bin_var)
            for bin_var in bin_vars
        ]
        inputs += [
            cs.Variable(name="systematic", type="string", description="Choose nominal efficiency or one of the uncertainties")
        ]
        
        content = build_schema_recursively(1, tuple([1] * dimensions))

        corr = Correction(
            name=key,
            version=1,
            description=f"Trigger scale factors for HWW analyses: {key}",
            inputs=inputs,
            output=cs.Variable(name="weight", type="real", description="Output scale factor (nominal) or uncertainty"),
            data=content,
        )
        """
        corr = Correction.model_validate(
            {
                "version": 1,
                "name": key,
                "description": f"Trigger scale factors for HWW analyses: {key}",
                "inputs": inputs,
                "output": {
                    "name": "weight",
                    "type": "real",
                    "description": "Output scale factor (nominal) or uncertainty",
                },
                "data": content,
            }
        )
        """
        
        corrs.append(corr)

    cset = CorrectionSet(
        schema_version=2,
        corrections=corrs,
    )

    with open(outname, "w") as fout:
        fout.write(cset.model_dump_json(exclude_unset=True, indent=4))

    import gzip

    with gzip.open(outname+".gz", "wt") as fout:
        fout.write(cset.model_dump_json(exclude_unset=True, indent=4))
    
    #cset = CorrectionSet.parse_obj({"schema_version": 2, "corrections": corrs})
    #cset = CorrectionSet.model_validate({"schema_version": 2, "corrections": corrs})

    # Write out converted json
    #with open(outname, "w") as fout:
    #    fout.write(cset.json(exclude_unset=True, indent=4))
    

