import os
import sys
from BF1942_Extraction_Readout_Scripts.refractor_flat_archive import RefractorFlatArchive

map_name = "GC_Bespin_Night"

client_file_path = f"client/{map_name}.rfa"
if not os.path.isfile(client_file_path):
    print(f"Error: Please add the client file \"{map_name}.rfa\" first to this folder: \:build\client\".")
    sys.exit()

rfa = RefractorFlatArchive(client_file_path)
rfa.delete_all_non_server_files()
rfa.add_directory(f"../src/bf1942/levels/{map_name}", "../src")

if not os.path.exists("server"):
    os.makedirs("server")
rfa.write(f"server{os.sep}{map_name.lower()}.rfa")
