# Copyright 2019.7    Nan LEE

import argparse
import os
import csv
import numpy as np
import cPickle
#import matplotlib.pyplot as plt


def calculate_pesq(args):
    """Calculate PESQ of all enhaced speech. 
    
    Args:
      workspace: str, path of workspace. 
      speech_dir: str, path of clean speech. 
      te_snr: float, testing SNR. 
    """
    workspace = args.workspace
    speech_dir = args.speech_dir
    #te_snr = args.te_snr
    type = args.type
    # Remove already existed file. 
    os.system('rm _pesq_itu_results.txt')
    os.system('rm _pesq_results.txt')
    
    # Calculate PESQ of all enhaced speech. 
    enh_speech_dir = os.path.join(workspace, "enh_wavs", type)
    names = os.listdir(enh_speech_dir)
    for (cnt, na) in enumerate(names):
        print(cnt, na)
        enh_path = os.path.join(enh_speech_dir, na)
        
        speech_na = na.split('.')[0]
        speech_path = os.path.join(speech_dir, "%s.wav" % speech_na)
        print(speech_path)
        print(enh_path) 
        # Call executable PESQ tool. 
        cmd = ' '.join(["./pesq", speech_path, enh_path, "+16000"])
        os.system(cmd)        
        
        
def get_stats(args):
    """Calculate stats of PESQ. 
    """
    pesq_path = "_pesq_results.txt"
    with open(pesq_path, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        lis = list(reader)
        
    pesq_dict = {}
    for i1 in xrange(1, len(lis) - 1):
        li = lis[i1]
        na = li[0]
        pesq = float(li[1])
        noise_type = na.split('.')[1]
        if noise_type not in pesq_dict.keys():
            pesq_dict[noise_type] = [pesq]
        else:
            pesq_dict[noise_type].append(pesq)
        
    avg_list, std_list = [], []
    f = "{0:<16} {1:<16}"
    print(f.format("Noise", "PESQ"))
    print("---------------------------------")
    for noise_type in pesq_dict.keys():
        pesqs = pesq_dict[noise_type]
        avg_pesq = np.mean(pesqs)
        std_pesq = np.std(pesqs)
        avg_list.append(avg_pesq)
        std_list.append(std_pesq)
        print(f.format(noise_type, "%.2f +- %.2f" % (avg_pesq, std_pesq)))
    print("---------------------------------")
    print(f.format("Avg.", "%.2f +- %.2f" % (np.mean(avg_list), np.mean(std_list))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode')

    parser_plot_training_stat = subparsers.add_parser('plot_training_stat')
    parser_plot_training_stat.add_argument('--workspace', type=str, required=True)
    #parser_plot_training_stat.add_argument('--tr_snr', type=float, required=True)
    parser_plot_training_stat.add_argument('--bgn_iter', type=int, required=True)
    parser_plot_training_stat.add_argument('--fin_iter', type=int, required=True)
    parser_plot_training_stat.add_argument('--interval_iter', type=int, required=True)

    parser_calculate_pesq = subparsers.add_parser('calculate_pesq')
    parser_calculate_pesq.add_argument('--type', type=str, required=True)
    parser_calculate_pesq.add_argument('--workspace', type=str, required=True)
    parser_calculate_pesq.add_argument('--speech_dir', type=str, required=True)
    #parser_calculate_pesq.add_argument('--te_snr', type=float, required=True)
    
    parser_get_stats = subparsers.add_parser('get_stats')
    
    args = parser.parse_args()
    
    if args.mode == 'plot_training_stat':
        plot_training_stat(args)
    elif args.mode == 'calculate_pesq':
        calculate_pesq(args)
    elif args.mode == 'get_stats':
        get_stats(args)
    else:
        raise Exception("Error!")
