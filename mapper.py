#!/usr/bin/env python3
import sys
import re

# Função para processar cada linha (documento)
for line in sys.stdin:
    doc_id, text = line.strip().split("\t", 1)  # Documento no formato: ID<TAB>Texto
    words = re.findall(r'\w+', text.lower())  # Tokeniza as palavras

    for word in words:
        print(f"{word}\t{doc_id}")  # Emite (termo, documento)
