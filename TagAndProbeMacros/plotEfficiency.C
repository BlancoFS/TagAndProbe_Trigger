void plotEfficiency(TString rootFiles, TString triggerFile)
{

ifstream inRootFile;
inRootFile.open(rootFiles.Data());
while(!inRootFile.eof())
{
	TString rootFile;
	inRootFile>>rootFile;
	if(inRootFile.eof()) break;	

	gStyle->SetOptStat(0);
	gStyle->SetPaintTextFormat("1.2f");

     	TFile *f1 = new TFile(rootFile.Data());
        ifstream inFile;
 	inFile.open(triggerFile.Data());
	TString trigger_name;
	TMultiGraph *mg = new TMultiGraph();
        TCanvas *c = new TCanvas("c","",200,10,600,500);
        //c->SetGridx();      
        //c->SetGridy();
	TString SysType = rootFile.ReplaceAll("efficiency","");
	SysType.ReplaceAll(".root","");
	cout<<"systType : "<<SysType.Data()<<"  ,rootFile : "<<rootFile.Data()<<endl;

	while(!inFile.eof())
	  {
	    TH1F *h_total;
	    TH1F *h_pass; 
	    TH2F *h2_total;
	    TH2F *h2_pass; 
	    TEfficiency* grl=0 ;
	    TGraphAsymmErrors * gra=0 ;
	    inFile>>trigger_name;
	    if(inFile.eof()) break;
	    TString total = trigger_name.Data(); 	
	    total += "_total"; 	
	    if(total.Contains("_Iso") ) total.ReplaceAll("_Iso","");
	    TString pass = trigger_name.Data(); 	
	    pass += "_pass";

	    // Nominal syst variations
	    bool doNominal = (rootFile.Contains("nominal"));
	    TH2F *h2_total_pTup;
            TH2F *h2_pass_pTup;

	    TH2F *h2_total_pTdown;
            TH2F *h2_pass_pTdown;

	    TH2F *h2_total_ZmassUp;
            TH2F *h2_pass_ZmassUp;

	    TH2F *h2_total_ZmassDown;
            TH2F *h2_pass_ZmassDown;

	    TEfficiency* grl_pTup=0 ;
	    TEfficiency* grl_pTdown=0 ;
	    TEfficiency* grl_ZmassUp=0 ;
	    TEfficiency* grl_ZmassDown=0 ;
	    
	    if(total.Contains("pt_eta"))
	      {
		TString textFileName = trigger_name.Data();
		textFileName += SysType;
		textFileName+="_efficiency.txt";
		ofstream outfile(textFileName.Data());
		if (doNominal){

		  //TString file_pT_up = "efficiency_TagPt_up_Ele.root";
		  //TString file_pT_down = "efficiency_TagPt_down_Ele.root";
		  //TString file_Z_up = "efficiency_Zmass_up_Ele.root";
		  //TString file_Z_down = "efficiency_Zmass_down_Ele.root";

		  //TString file_pT_up = "efficiency_TagPt_up_Mu.root";
                  //TString file_pT_down = "efficiency_TagPt_down_Mu.root";
                  //TString file_Z_up = "efficiency_Zmass_up_Mu.root";
                  //TString file_Z_down = "efficiency_Zmass_down_Mu.root";
		  /**
		  // MC Muon Run2022EE
		  TString file_pT_up = "efficiency_DY_Run2022E_TagPt_up_Mu.root";
                  TString file_pT_down = "efficiency_DY_Run2022E_TagPt_down_Mu.root";
                  TString file_Z_up = "efficiency_DY_Run2022E_Zmass_up_Mu.root";
		  TString file_Z_down = "efficiency_DY_Run2022E_Zmass_down_Mu.root";
		  
		  // MC Electron Run2022EE
		  TString file_pT_up = "efficiency_DY_Run2022E_TagPt_up_Ele.root";
                  TString file_pT_down = "efficiency_DY_Run2022E_TagPt_down_Ele.root";
                  TString file_Z_up = "efficiency_DY_Run2022E_Zmass_up_Ele.root";
                  TString file_Z_down = "efficiency_DY_Run2022E_Zmass_down_Ele.root";
		  
		  // Data Electron Run2022BCD
		  TString file_pT_up = "efficiency_Run2022BCD_TagPt_up_Ele.root";
                  TString file_pT_down = "efficiency_Run2022BCD_TagPt_down_Ele.root";
                  TString file_Z_up = "efficiency_Run2022BCD_Zmass_up_Ele.root";
                  TString file_Z_down = "efficiency_Run2022BCD_Zmass_down_Ele.root";
		  
		  TString file_pT_up = "efficiency_Run2022BCD_TagPt_up_Mu.root";
                  TString file_pT_down = "efficiency_Run2022BCD_TagPt_down_Mu.root";
                  TString file_Z_up = "efficiency_Run2022BCD_Zmass_up_Mu.root";
                  TString file_Z_down = "efficiency_Run2022BCD_Zmass_down_Mu.root";
		  
		  // MC Electron Run2022BCD
		  TString file_pT_up = "efficiency_DY_Run2022BCD_TagPt_up_Ele.root";
                  TString file_pT_down = "efficiency_DY_Run2022BCD_TagPt_down_Ele.root";
                  TString file_Z_up = "efficiency_DY_Run2022BCD_Zmass_up_Ele.root";
                  TString file_Z_down = "efficiency_DY_Run2022BCD_Zmass_down_Ele.root";
		  **/
		  // MC Muon Run2022BCD
                  TString file_pT_up = "efficiency_DY_Run2022BCD_TagPt_up_Mu.root";
                  TString file_pT_down = "efficiency_DY_Run2022BCD_TagPt_down_Mu.root";
                  TString file_Z_up = "efficiency_DY_Run2022BCD_Zmass_up_Mu.root";
                  TString file_Z_down = "efficiency_DY_Run2022BCD_Zmass_down_Mu.root";
		  
		  
		  TFile *f1_pT_up      = new TFile(file_pT_up.Data());
		  TFile *f1_pT_down    = new TFile(file_pT_down.Data());
		  TFile *f1_Zmass_up   = new TFile(file_Z_up.Data());
		  TFile *f1_Zmass_down = new TFile(file_Z_down.Data());

		  h2_total_pTup = (TH2F*)f1_pT_up->Get(total.Data());
		  h2_pass_pTup = (TH2F*)f1_pT_up->Get(pass.Data());

		  h2_total_pTdown = (TH2F*)f1_pT_down->Get(total.Data());
		  h2_pass_pTdown = (TH2F*)f1_pT_down->Get(pass.Data());

		  h2_total_ZmassUp = (TH2F*)f1_Zmass_up->Get(total.Data());
		  h2_pass_ZmassUp = (TH2F*)f1_Zmass_up->Get(pass.Data());

		  h2_total_ZmassDown = (TH2F*)f1_Zmass_down->Get(total.Data());
		  h2_pass_ZmassDown = (TH2F*)f1_Zmass_down->Get(pass.Data());

		  grl_pTup = new TEfficiency(*h2_pass_pTup,*h2_total_pTup);
		  grl_pTdown = new TEfficiency(*h2_pass_pTdown,*h2_total_pTdown);
		  grl_ZmassUp = new TEfficiency(*h2_pass_ZmassUp,*h2_total_ZmassUp);
		  grl_ZmassDown = new TEfficiency(*h2_pass_ZmassDown,*h2_total_ZmassDown);
		  
		  c->SetLogy();
                  h2_total = (TH2F*)f1->Get(total.Data());
                  h2_pass = (TH2F*)f1->Get(pass.Data());
                  h2_total->GetYaxis()->SetTitle("pt");
                  h2_total->GetXaxis()->SetTitle("eta");
                  grl = new TEfficiency(*h2_pass,*h2_total);
                  grl->SetTitle(h2_total->GetTitle());
                  grl->Draw("colztext");

		  float eff = 0.0;
		  float eff_stat = 0.0;

		  float eff_ptUp = 0.0;
		  float	eff_ptDown = 0.0;
		  float	eff_ZUp = 0.0;
		  float	eff_ZDown = 0.0;

		  float sys_var = 0.0;
		  
		  for(int ieta = 1; ieta <= h2_pass->GetNbinsX(); ieta++){
                    for(int ipt = 1; ipt <= h2_pass->GetNbinsY(); ipt++){
                      int globalBin = grl->GetGlobalBin(ieta,ipt);
		      sys_var	= 0.0;

		      eff = (float)grl->GetEfficiency(globalBin);
		      if (grl->GetEfficiencyErrorLow(globalBin)>grl->GetEfficiencyErrorUp(globalBin)){
			eff_stat = (float)grl->GetEfficiencyErrorLow(globalBin);
		      }else{
			eff_stat = (float)grl->GetEfficiencyErrorUp(globalBin);
		      }
		      
		      eff_ptUp   = (float)grl_pTup->GetEfficiency(globalBin);
		      eff_ptDown = (float)grl_pTdown->GetEfficiency(globalBin);
		      eff_ZUp    = (float)grl_ZmassUp->GetEfficiency(globalBin);
		      eff_ZDown  = (float)grl_ZmassDown->GetEfficiency(globalBin);

		      //cout << "------------------------" << endl;
		      //cout << "eff           -> " << eff << endl;
		      //cout << "err stat      -> " << eff_stat << endl;
		      //cout << "mass up eff   -> " << eff_ZUp << endl;
		      //cout << "pT up err     -> " << fabs(eff_ptUp-eff) << endl;
		      //cout << "pT down err   -> " << fabs(eff_ptDown-eff) << endl;
		      //cout << "mass up err   -> " << fabs(eff_ZUp-eff) << endl;
		      //cout << "mass down err -> " << fabs(eff_ZDown-eff) << endl;
		      
		      eff_ptUp = (fabs(eff_ptUp-eff)>eff_stat) ? eff_ptUp : eff;
		      eff_ptDown = (fabs(eff_ptDown-eff)>eff_stat) ? eff_ptDown : eff;
		      eff_ZUp = (fabs(eff_ZUp-eff)>eff_stat) ? eff_ZUp : eff;
		      eff_ZDown = (fabs(eff_ZDown-eff)>eff_stat) ? eff_ZDown : eff;

		      //cout << "- - - - - - - - - - - " << endl;
		      //cout << "pT up err     -> " << fabs(eff_ptUp-eff) << endl;
                      //cout << "pT down err   -> " << fabs(eff_ptDown-eff) << endl;
                      //cout << "mass up err   -> " << fabs(eff_ZUp-eff) << endl;
                      //cout << "mass down err -> " << fabs(eff_ZDown-eff) << endl;

		      if (eff==0.0){
			sys_var = 0.0;
		      }else{
			sys_var = eff*sqrt( (fabs(eff_ptUp-eff)/eff)*(fabs(eff_ptUp-eff)/eff) + (fabs(eff_ptDown-eff)/eff)*(fabs(eff_ptDown-eff)/eff) + (fabs(eff_ZUp-eff)/eff)*(fabs(eff_ZUp-eff)/eff) + (fabs(eff_ZDown-eff)/eff)*(fabs(eff_ZDown-eff)/eff));
		      }

		      cout << "total syst -> " << sys_var << endl;
		      
                      outfile << std::fixed;

                      outfile << setprecision(2)<< h2_pass->GetXaxis()->GetBinLowEdge(ieta)<<"\t" << setprecision(2)<< h2_pass->GetXaxis()->GetBinUpEdge(ieta)<< "\t";
                      outfile << setprecision(1)<<h2_pass->GetYaxis()->GetBinLowEdge(ipt) <<setprecision(1)<< "\t" << h2_pass->GetYaxis()->GetBinUpEdge(ipt) << "\t" << setprecision(3)<<"\t";

                      outfile << std::fixed;
                      outfile<< grl->GetEfficiency(globalBin)<<setprecision(3)<<"\t"<<grl->GetEfficiencyErrorLow(globalBin)<<setprecision(3)<<"\t"<<grl->GetEfficiencyErrorUp(globalBin)<<setprecision(3)<<"\t"<<sys_var<<setprecision(3)<<"\t"<<sys_var<<setprecision(3)<<endl;
                      outfile << std::fixed;
                    }
                  }
		  
		}else{		
		  c->SetLogy();
		  h2_total = (TH2F*)f1->Get(total.Data());
		  h2_pass = (TH2F*)f1->Get(pass.Data());
		  h2_total->GetYaxis()->SetTitle("pt");
		  h2_total->GetXaxis()->SetTitle("eta");
		  grl = new TEfficiency(*h2_pass,*h2_total);
		  grl->SetTitle(h2_total->GetTitle());
		  grl->Draw("colztext");
		  for(int ieta = 1; ieta <= h2_pass->GetNbinsX(); ieta++){
		    for(int ipt = 1; ipt <= h2_pass->GetNbinsY(); ipt++){
		      int globalBin = grl->GetGlobalBin(ieta,ipt);
		      outfile << std::fixed;
		      
		      outfile << setprecision(2)<< h2_pass->GetXaxis()->GetBinLowEdge(ieta)<<"\t" << setprecision(2)<< h2_pass->GetXaxis()->GetBinUpEdge(ieta)<< "\t";
		      outfile << setprecision(1)<<h2_pass->GetYaxis()->GetBinLowEdge(ipt) <<setprecision(1)<< "\t" << h2_pass->GetYaxis()->GetBinUpEdge(ipt) << "\t" << setprecision(3)<<"\t";
		      
		      outfile << std::fixed;
		      outfile<< grl->GetEfficiency(globalBin)<<setprecision(3)<<"\t"<<grl->GetEfficiencyErrorLow(globalBin)<<setprecision(3)<<"\t"<<grl->GetEfficiencyErrorUp(globalBin)<<setprecision(3) <<endl;
		      outfile << std::fixed;
		    }
		  }
		}
		outfile.close();
	      }
	    
	    else {
	      
	      c->SetLogy(0);
	      h_total = (TH1F*)f1->Get(total.Data());
	      h_pass = (TH1F*)f1->Get(pass.Data());
	      if(total.Contains("pt")){h_total->GetXaxis()->SetTitle("pT in (GeV)");h_pass->GetXaxis()->SetTitle("pT in (GeV)");}
	      if(total.Contains("eta")){h_total->GetXaxis()->SetTitle("eta");h_total->GetXaxis()->SetTitle("eta");}
	      h_total->GetYaxis()->SetRangeUser(0,1);
	      h_total->GetYaxis()->SetTitle("efficiency");
	      h_pass->GetYaxis()->SetTitle("efficiency");
	      h_pass->GetYaxis()->SetRangeUser(0,1);
	      //        grl = new TEfficiency(*h_pass,*h_total);
	      //	grl->SetLineColor(1);
	      //	grl->SetMarkerStyle(20);
	      //	grl->SetMarkerColor(1);
	      //        grl->SetTitle(h_total->GetTitle());
	      //   	grl->Draw("APE");
	      
	      TString graph_name = trigger_name.Data();
	      graph_name += SysType;
	      graph_name += "_efficiency";
	      gra = new TGraphAsymmErrors (h_pass,h_total); 
	      gra->SetLineColor(1);
	      gra->SetName(graph_name.Data());
	      gra->SetMarkerStyle(20);
	      gra->SetMarkerColor(1);
	      gra->SetTitle(h_total->GetTitle());
	      gra->Draw("APE");
	      gra->GetYaxis()->SetRangeUser(0,1);
	      
	    }
	    
	    TString pngFileName = trigger_name.Data() ;
	    pngFileName += SysType;
	    pngFileName +=  "_efficiency.png";
	    TString rootFileName = trigger_name.Data() ;
	    rootFileName += SysType;
	    rootFileName +=  "_efficiency.root";
	    c->SaveAs(pngFileName.Data());
	    if(!rootFileName.Contains("pt_eta"))
	      {	TFile file_out(rootFileName.Data(),"RECREATE");
		file_out.cd();
  		gra->Write();
	      }
	    else
	      {c->SaveAs(rootFileName.Data());}
	    c->Clear();
	    gSystem->Exec("mkdir -p results");
	    TString dirName = "results/";
	    dirName+=trigger_name.Data();
	    gSystem->Exec("mkdir -p  "+ dirName);
	    gSystem->Exec("mv " + trigger_name+"*  "+dirName);
	    delete grl;
	    delete gra;
	  }
	delete c;
	delete mg;
 }
}
