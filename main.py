# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
import re


def find_in_file(file_dir, value_find_by):
    os.chdir(file_dir)
    for log_file in glob.glob("*.*"):
        occurrence_found = False

        with open(log_file, 'r') as log:
            log_content_lines = log.read()
            if value_find_by in log_content_lines:
                occurrence_found = True

        if occurrence_found:
            print(log_file)
            print("\n-------------------------------\n")


print "Informe o diretório dos arquivos:",
file_dir = raw_input()

program_end = '-1'

while program_end != '0':
    print "Informe o valor a pesquisar nos arquivos:",
    value_find_by = raw_input()
    program_end = value_find_by
    find_in_file(file_dir, value_find_by)
    print "Para finalizar, basta digitar 0 |",
