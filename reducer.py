#!/usr/bin/env python3
import sys

current_word = None
doc_list = set()

# Lê linha por linha do Hadoop Streaming
for line in sys.stdin:
    word, doc_id = line.strip().split("\t", 1)

    # Se a palavra mudou, imprime o índice do termo anterior
    if current_word and current_word != word:
        print(f"{current_word}\t{sorted(doc_list)}")
        doc_list = set()

    current_word = word
    doc_list.add(doc_id)

# Imprime a última palavra processada
if current_word:
    print(f"{current_word}\t{sorted(doc_list)}")
