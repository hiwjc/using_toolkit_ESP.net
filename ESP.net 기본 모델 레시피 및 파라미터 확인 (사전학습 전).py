import yaml, pprint

conf = yaml.safe_load(open("/home/jpong/espnet/egs2/librispeech/asr1/conf/train_asr_conformer.yaml"))
pp = pprint.PrettyPrinter(indent=2)

print("=== Top-level keys ===")
pp.pprint(list(conf.keys()))


import yaml, pprint

conf = yaml.safe_load(open("egs2/librispeech/asr1/conf/train_asr_conformer.yaml"))
pp = pprint.PrettyPrinter(indent=2)

enc_conf = conf["encoder"]
dec_conf = conf["decoder"]

print("=== Encoder ===")
pp.pprint(enc_conf)
print("\n=== Decoder ===")
pp.pprint(dec_conf)

print("=== Encoder 세부 설정 ===")
pp.pprint(conf["encoder_conf"])

print("\n=== Decoder 세부 설정 ===")
pp.pprint(conf["decoder_conf"])
