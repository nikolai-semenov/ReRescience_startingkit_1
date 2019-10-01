#!/usr/bin/python
import os
import sys
import pandas as pd
import numpy as np


def main():
    # print command line arguments
    input_dir, output_dir = sys.argv[1:]
    predicted_result = []
    df = np.loadtxt(os.path.join(input_dir, 'data.data'))
    df = pd.DataFrame(df, columns=['column 1', 'column 2', 'column 3'])

    df['result'] = df.sum(axis=1)

    np.savetxt(os.path.join(output_dir, 'data.predict'), np.array(df['result']), fmt='%.3f')
    return 0

if __name__ == "__main__":
    main()
