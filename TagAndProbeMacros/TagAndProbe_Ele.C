#define TagAndProbe_cxx
#include "TagAndProbe.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void TagAndProbe::Loop(TString output)
{
   if (fChain == 0) return;
  bool RunSystematic=false;
  //vector<TString> systematicVar =  {"nominal"};
  //vector<TString> systematicVar =  {"TagPt_up"};
  //vector<TString> systematicVar =  {"TagPt_down"};
  //vector<TString> systematicVar =  {"Zmass_up"};
  vector<TString> systematicVar =  {"Zmass_down"};
  if (RunSystematic)
    {
      systematicVar.push_back("TagPt_up");
      systematicVar.push_back("TagPt_down");
      systematicVar.push_back("Zmass_up");
      systematicVar.push_back("Zmass_down");
    }
  
for(int i=0; i<systematicVar.size();i++)
{

   double ptTag = 37; 
   double zMassL = 60; 
   double zMassR = 120;

   if(systematicVar.at(i).Contains("TagPt_up")) ptTag = 41;
   if(systematicVar.at(i).Contains("TagPt_down")) ptTag = 33;
   if(systematicVar.at(i).Contains("Zmass_up")) {zMassL = 50; zMassR = 130;}
   if(systematicVar.at(i).Contains("Zmass_down")) {zMassL = 70; zMassR = 110;}
 
   cout<<systematicVar.at(i).Data()<<endl;
   cout<<" ptTag : "<<ptTag<<" , zMassL : "<<zMassL<<" , zMassR : "<<zMassR<<endl;
   output = "";
   output +="efficiency_DY_Run2022E_";
   output += systematicVar.at(i);
   output +="_Ele.root";

   TFile *file = new TFile(output.Data(),"RECREATE");
   Long64_t nentries = fChain->GetEntriesFast();
   double eta_bins[19] = {-2.5,-2.4,-2.3,-2.2,-2.1,-1.566,-1.4442,-0.8,-0.4,0,0.4,0.8,1.4442,1.566,2.1,2.2,2.3,2.4,2.5};
   double pt_bins_Ele35[16] = {5. ,  15. ,  25. ,  31. ,  32.5,  33.5,  34.5,  35.5,  36.5, 37.5,  39. ,  42.5,  47.5,  55. ,  80. , 150. };
   double pt_bins_Ele23_Ele12_leg1[14] = {0,20,23,24,25,26,30,35,40,45,50,60,100,200};
   double pt_bins_Ele23_Ele12_leg2[16] = {0,10,12,13,14,15,20,25,30,35,40,45,50,60,100,200};

   double PU_bins[8] = {0,20,30,40,50,60,70,100};


// HLT Ele35

   TH1F *h_Ele35_pt_total = new TH1F("Ele35_pt_total","Ele35_pt",15,pt_bins_Ele35);
   TH1F *h_Ele35_eta_total = new TH1F("Ele35_eta_total","Ele35_eta",18,eta_bins);
   TH2F *h_Ele35_pt_eta_total = new TH2F("Ele35_pt_eta_total","Ele35_pt_eta",18,eta_bins,15,pt_bins_Ele35);
   TH1F *h_Ele35_pt_pass = new TH1F("Ele35_pt_pass","Ele35_pt",15,pt_bins_Ele35);
   TH1F *h_Ele35_eta_pass = new TH1F("Ele35_eta_pass","Ele35_eta",18,eta_bins);
   TH2F *h_Ele35_pt_eta_pass = new TH2F("Ele35_pt_eta_pass","Ele35_pt_eta",18,eta_bins,15,pt_bins_Ele35);

   h_Ele35_pt_total->Sumw2();
   h_Ele35_eta_total->Sumw2();
   h_Ele35_pt_eta_total->Sumw2();
   h_Ele35_pt_pass->Sumw2();
   h_Ele35_eta_pass->Sumw2();
   h_Ele35_pt_eta_pass->Sumw2();

// HLT Ele23_Ele12 Ele23 leg
   TH1F *h_Ele23_Ele12_leg1_pt_total = new TH1F("Ele23_Ele12_leg1_pt_total","Ele23_Ele12_leg1_pt",13,pt_bins_Ele23_Ele12_leg1);
   TH1F *h_Ele23_Ele12_leg1_eta_total = new TH1F("Ele23_Ele12_leg1_eta_total","Ele23_Ele12_leg1_eta",18,eta_bins);
   TH2F *h_Ele23_Ele12_leg1_pt_eta_total = new TH2F("Ele23_Ele12_leg1_pt_eta_total","Ele23_Ele12_leg1_pt_eta",18,eta_bins,13,pt_bins_Ele23_Ele12_leg1);
   TH1F *h_Ele23_Ele12_leg1_pt_pass = new TH1F("Ele23_Ele12_leg1_pt_pass","Ele23_Ele12_leg1_pt",13,pt_bins_Ele23_Ele12_leg1);
   TH1F *h_Ele23_Ele12_leg1_eta_pass = new TH1F("Ele23_Ele12_leg1_eta_pass","Ele23_Ele12_leg1_eta",18,eta_bins);
   TH2F *h_Ele23_Ele12_leg1_pt_eta_pass = new TH2F("Ele23_Ele12_leg1_pt_eta_pass","Ele23_Ele12_leg1_pt_eta",18,eta_bins,13,pt_bins_Ele23_Ele12_leg1);
      
   h_Ele23_Ele12_leg1_pt_total->Sumw2();
   h_Ele23_Ele12_leg1_eta_total->Sumw2();
   h_Ele23_Ele12_leg1_pt_eta_total->Sumw2();
   h_Ele23_Ele12_leg1_pt_pass->Sumw2();
   h_Ele23_Ele12_leg1_eta_pass->Sumw2();
   h_Ele23_Ele12_leg1_pt_eta_pass->Sumw2();

// HLT Ele23_Ele12 Ele12 leg
   TH1F *h_Ele23_Ele12_leg2_pt_total = new TH1F("Ele23_Ele12_leg2_pt_total","Ele23_Ele12_leg2_pt",15,pt_bins_Ele23_Ele12_leg2);
   TH1F *h_Ele23_Ele12_leg2_eta_total = new TH1F("Ele23_Ele12_leg2_eta_total","Ele23_Ele12_leg2_eta",18,eta_bins);
   TH2F *h_Ele23_Ele12_leg2_pt_eta_total = new TH2F("Ele23_Ele12_leg2_pt_eta_total","Ele23_Ele12_leg2_pt_eta",18,eta_bins,15,pt_bins_Ele23_Ele12_leg2);
   TH1F *h_Ele23_Ele12_leg2_pt_pass = new TH1F("Ele23_Ele12_leg2_pt_pass","Ele23_Ele12_leg2_pt",15,pt_bins_Ele23_Ele12_leg2);
   TH1F *h_Ele23_Ele12_leg2_eta_pass = new TH1F("Ele23_Ele12_leg2_eta_pass","Ele23_Ele12_leg2_eta",18,eta_bins);
   TH2F *h_Ele23_Ele12_leg2_pt_eta_pass = new TH2F("Ele23_Ele12_leg2_pt_eta_pass","Ele23_Ele12_leg2_pt_eta",18,eta_bins,15,pt_bins_Ele23_Ele12_leg2);

   h_Ele23_Ele12_leg2_pt_total->Sumw2();
   h_Ele23_Ele12_leg2_eta_total->Sumw2();
   h_Ele23_Ele12_leg2_pt_eta_total->Sumw2();
   h_Ele23_Ele12_leg2_pt_pass->Sumw2();
   h_Ele23_Ele12_leg2_eta_pass->Sumw2();
   h_Ele23_Ele12_leg2_pt_eta_pass->Sumw2();


   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      if(jentry%50000 == 0)cout<<"number of events processed : "<<jentry<<endl;
      if(nEle!=2) continue;
      int first  = rand()%2;
      int second = (first+1)%2;      
      if(ele_charge->at(first) * ele_charge->at(second)>0)continue;
      bool tag_EleId = passEleIdTight->at(first);
      bool tag_EleKin = ele_pt->at(first)>ptTag && fabs(ele_etaSC->at(first))<2.5;
      bool tag_TriggerMatch = passFilterEle35->at(first);

      if(!(tag_EleId && tag_EleKin && tag_TriggerMatch))continue;

      bool probe_EleId = HWW_Electron_NewDef(second, ele_etaSC->at(second));
      bool probe_EleKin = fabs(ele_etaSC->at(second))<2.5;

      if(!(probe_EleId && probe_EleKin)) continue;

      TLorentzVector tag_eleLV, probe_eleLV, Z_candLV;
      tag_eleLV.SetPtEtaPhiM(ele_pt->at(first), ele_etaSC->at(first), ele_phi->at(first),0.);
      probe_eleLV.SetPtEtaPhiM(ele_pt->at(second), ele_etaSC->at(second), ele_phi->at(second),0.);
      Z_candLV = tag_eleLV + probe_eleLV;

      if (Z_candLV.M()<zMassL || Z_candLV.M() > zMassR) continue;


      h_Ele35_pt_total->Fill(ele_pt->at(second));
      h_Ele35_eta_total->Fill(ele_etaSC->at(second));
      h_Ele35_pt_eta_total->Fill(ele_etaSC->at(second),ele_pt->at(second));

      h_Ele23_Ele12_leg1_pt_total->Fill(ele_pt->at(second)); 
      h_Ele23_Ele12_leg1_eta_total->Fill(ele_etaSC->at(second)); 
      h_Ele23_Ele12_leg1_pt_eta_total->Fill(ele_etaSC->at(second),ele_pt->at(second)); 

      h_Ele23_Ele12_leg2_pt_total->Fill(ele_pt->at(second)); 
      h_Ele23_Ele12_leg2_eta_total->Fill(ele_etaSC->at(second)); 
      h_Ele23_Ele12_leg2_pt_eta_total->Fill(ele_etaSC->at(second),ele_pt->at(second)); 


      if (passFilterEle35->at(second)){
	h_Ele35_pt_pass->Fill(ele_pt->at(second));
	h_Ele35_eta_pass->Fill(ele_etaSC->at(second));
	h_Ele35_pt_eta_pass->Fill(ele_etaSC->at(second),ele_pt->at(second));
      }

      if (passFilterEle23_12_leg1->at(second)){
	h_Ele23_Ele12_leg1_pt_pass->Fill(ele_pt->at(second)); 
	h_Ele23_Ele12_leg1_eta_pass->Fill(ele_etaSC->at(second)); 
	h_Ele23_Ele12_leg1_pt_eta_pass->Fill(ele_etaSC->at(second),ele_pt->at(second)); 
      } 
      if (passFilterEle23_12_leg2->at(second)){
	h_Ele23_Ele12_leg2_pt_pass->Fill(ele_pt->at(second)); 
	h_Ele23_Ele12_leg2_eta_pass->Fill(ele_etaSC->at(second)); 
	h_Ele23_Ele12_leg2_pt_eta_pass->Fill(ele_etaSC->at(second),ele_pt->at(second)); 
      } 

      // if (Cut(ientry) < 0) continue;
    }
   file->Write(); 
  }
 
}

bool TagAndProbe::HWW_Electron_NewDef(int i, double eta)
{
bool mvaid = false;
bool tightid = false;
bool mediumid= false;
bool convVeto = ele_passConversionVeto->at(i);
double relIso = ele_relCombIsoWithEA->at(i);
mvaid = passEleIdMVA90Iso22V1->at(i);
 
if(fabs(eta) < 1.479){    // Barrel
//if (!convVeto) return false;
if (relIso >= 0.06) return false;
if (!mvaid) return false;
//if (!tightid) return false;
//if (!mediumid) return false;
if (fabs(ele_d0->at(i))>=0.05) return false;
if (fabs(ele_dz->at(i))>=0.1) return false;
}

else{
//if (sieie >= 0.03) return false;
//if (fabs(eInvMinusPInv) >= 0.014) return false;
//if (!convVeto) return false;
if (relIso >= 0.06) return false;
if (!mvaid) return false;
//if (!tightid) return false;
//if (!mediumid) return false;
if (fabs(ele_d0->at(i))>=0.1) return false;
if (fabs(ele_dz->at(i))>=0.2) return false;
}
return true;
}
