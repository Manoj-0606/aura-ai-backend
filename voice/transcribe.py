from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_file="test.wav"):

    segments, info = model.transcribe(
        audio_file,
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text


if __name__ == "__main__":

    result = transcribe_audio()

    print("\nTRANSCRIPTION:")
    print(result)