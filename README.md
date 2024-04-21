# Wafer Scheduling using Johnson's Rule

This Python script applies Johnson's Rule to determine the optimal order of wafer processing across two machines to minimize the total processing time. It can handle both predefined sample data and user-provided input.

This is submission for the CSE 551: Foundation of Algorithms - Programming Assignment by Gautham Vijayaraj (ASU ID: 1229599464)

## Prerequisites

To run this script, you will need:
- Python 3.x installed on your computer.

## Running the Script

1. **Open Terminal or Command Prompt**: Navigate to the folder where the script is saved.

2. **Run the Script**:
   - Execute the command below in your terminal or command prompt:
     ```
     python wafer_scheduling.py
     ```
   - If you are using mac, then enter this:
     ``` 
     python3 wafer_scheduling.py
     ```

3. **Input Options**:
   - When prompted, type `sample` to run the script with predefined sample wafers.
   - Type `own` to enter your own data for each wafer. You will need to input the number of wafers and then specify the processing times on both machines for each wafer.

## Script Features

- **Sample Case**: The script includes a sample case with predefined wafers if you select the `sample` option. This allows you to quickly test the functionality of the algorithm.
- **Custom Input**: For more specific scenarios, you can input your own set of wafers by selecting the `own` option. You will be prompted to input the number of wafers and the processing times for each machine.
- **Output**: After processing, the script outputs the optimal sequence of wafers, the total elapsed time of the process, and the idle time on Machine 1.


## Troubleshooting

If you encounter any issues with running the script:
- Ensure Python is properly installed by running `python --version` in your command line. `python3 --version` if mac.
- Check that you are in the correct directory where the script is located.
- Verify the syntax and inputs are correctly entered as prompted by the script.

