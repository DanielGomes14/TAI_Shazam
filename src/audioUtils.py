from consts import SAMPLE_MAX_FREQS
import subprocess

def add_noise(sample, sample_name, noise):
    cmd = f"sox {sample} -p synth whitenoise vol {noise} | sox -m {sample} - {SAMPLE_MAX_FREQS}{sample_name}"
    subprocess.run([cmd], shell=True)
