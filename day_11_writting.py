from pathlib import Path
# creating a log file to store the pipeline data
log_path = Path("pipeline_log.txt")
print("Opening a secure file stream to write data.")
print("----------------------------------------")
# writing data to the log file
# the 'a' mode is used to open the file in append mode,
#  which means that new data will be added to the end of the
#  file without overwriting the existing data.
with open(log_path, mode= "a") as log_file:
    # .write() method is used to write the data to the file.
    #  It takes a string as an argument and writes it to the file.
    log_file.write("=== Unreal engine pipeline log ===\n")
    log_file.write("Asset name: SM_Castle_Gate\n")
    log_file.write("Status: Successfully Exported to FBX\n")
print("Stream securely closed. Data saved permanently.")
print("----------------------")
print("Reading the file content:")
print("---------------------")
# reading the data from the log file
''' encoding parameter is used to specify the character encoding of the file being read.
 In this case, it is set to "utf-8", which is a widely used character encoding that can 
 represent a wide range of characters from different languages and scripts.'''

with open(log_path, mode= "r" , encoding= "utf-8") as f:
    # reading the data line by line
    for line in f:
        print(line.strip()) # strip() is used to remove spaces and newline characters. 
print("-----------------")
print("file is closed scurely.")
