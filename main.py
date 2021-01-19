# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os


def find_in_file(file_dir, file_extension, value_find_by):
    os.chdir(file_dir)
    for log_file in glob.glob("*.{0}".format(file_extension)):
        with open(log_file) as log:
            if value_find_by in log.read():
                print(log_file)
        print("\n-------------------------------\n")


print "Informe o diretório dos arquivos:",
file_dir = raw_input()

print "Informe a extensão dos arquivos:",
file_extension = raw_input()


program_end = '-1'

while program_end != '0':
    print "Informe o valor a pesquisar nos arquivos:",
    value_find_by = raw_input()
    program_end = value_find_by
    find_in_file(file_dir, file_extension, value_find_by)
    print "Para finalizar, basta digitar 0:",

