from consts import SAMPLE_MAX_FREQS
import subprocess, os

def add_noise(sample, sample_name, noise):
    n_sample_name = f"noise_{noise}_{sample_name}"

    sample_musics = { f.name for f in os.scandir(SAMPLE_MAX_FREQS) }

    if n_sample_name not in sample_musics:
        cmd = f"sox {sample} -p synth whitenoise vol {noise} | sox -m {sample} - {SAMPLE_MAX_FREQS}{n_sample_name}"
        subprocess.run([cmd], shell=True)
    
    if sample_name in sample_musics:
        os.remove(f"{SAMPLE_MAX_FREQS}{sample_name}")

    sample=f"{SAMPLE_MAX_FREQS}{n_sample_name}"
    return sample, n_sample_name


def trim_audio_file(sample, trim_start, duration, sample_name):
    start_time = trim_start
    end_time = trim_start + duration
    n_trim_name = f"trim_{start_time}-{end_time}_{sample_name}"

    sample_musics = { f.name for f in os.scandir(SAMPLE_MAX_FREQS) }

    if n_trim_name not in sample_musics:
        cmd = f"sox -t wav {sample} {SAMPLE_MAX_FREQS}{n_trim_name} trim {start_time} {end_time}"
        subprocess.run([cmd], shell=True)

    if sample_name in sample_musics:
        os.remove(f"{SAMPLE_MAX_FREQS}{sample_name}")

    sample = f"{SAMPLE_MAX_FREQS}{n_trim_name}"

    return sample, n_trim_name