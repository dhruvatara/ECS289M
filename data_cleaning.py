#script to clean the data to extract features as outlined in Touchlogger
"""
1. discard azimuth angle since typing mostly affects pitch and roll angles
2. normalize the angles by finding mean of angles and subtracting
3. combine the two CSVs
"""