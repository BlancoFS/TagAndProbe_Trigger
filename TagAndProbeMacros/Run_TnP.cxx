//#include "TagAndProbe.C"
#include <fstream>
#include "TString.h"
#include "TSystem.h"

//  g++ Run_TnP.cxx -o tnp  `root-config --libs --cflags`    to compile the code

void RunLoop(TString file, TString output, int idx=-1)
//void RunLoop(void)
{

  TChain* chain = new TChain("ntupler/EventTree","");
  // Open the input stream
  ifstream in;
  in.open(file.Data());
//  in.open("SingleEleRun2016Hv2.txt");

  // Read the input list of files and add them to the chain
  TString currentFile;
  int counter=-1;

  cout << idx << endl;
  cout << output << endl;

  while(in.good()) {
    in >> currentFile;
    counter++;
    if (!currentFile.Contains("root")) continue; // protection
    if (idx>=0 && idx!=counter) continue;
    cout << "" << endl;
    cout << currentFile.Data() << endl;
    chain->Add(currentFile.Data());
  }
  in.close();
//  gSystem->CompileMacro("TrigEff_mc.C","f");
  TagAndProbe t(chain);
  t.Loop(output);

}
#if !defined(__CINT__) && !defined(__ACLIC__)

int main(int argc, char ** argv)
{


    if (argc < 2) {
        // Tell the user how to run the program
        std::cerr << "Usage: " << argv[0] << " NAME of file" << std::endl;
        return 1;
    }
  TString file = argv[1];
  TString output = argv[2];
  int index = -1;
  if (argc > 3) {
    index = stoi(argv[3]);
  }

  RunLoop(file,output, index); // just call the "ROOT Script"
//  RunLoop(); // just call the "ROOT Script"
  return 0;
}
#endif /* !defined(__CINT__) && !defined(__ACLIC__) */
