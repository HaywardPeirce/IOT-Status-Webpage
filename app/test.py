#import ships

import sys
# Add the ptdraft folder path to the sys.path list
#sys.path.append('/home/ubuntu/workspace/ship_traffic_data/')

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import your module
import ships

print ships.getShips()