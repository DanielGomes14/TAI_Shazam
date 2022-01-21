from consts import SAMPLE_MAX_FREQS
import subprocess

def add_noise(sample, sample_name, noise):
    cmd = f"sox {sample} -p synth whitenoise vol {noise} | sox -m {sample} - {SAMPLE_MAX_FREQS}noise_{noise}_{sample_name}"
    subprocess.run([cmd], shell=True)

def trim_audio_file(sample,trim, sample_name):
    start_time = 0
    end_time = trim
    
    cmd = f"sox {sample} {SAMPLE_MAX_FREQS}trim_{sample_name} trim {start_time} {end_time}"
    subprocess.run([cmd], shell=True)
    # print(sample)
    # tf.build_file(sample, f'{SAMPLE_MAX_FREQS}trim_{sample_name}')