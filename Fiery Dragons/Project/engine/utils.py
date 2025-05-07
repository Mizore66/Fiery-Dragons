from math import pi, sin, cos
from pygame import mixer


def lengthdir_x(dist: float, angle: float) -> float:
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    Returns the x-component of a vector given a distance and angle.

    Parameters
    ----------
        dist : float
            the distance of the vector
        angle : float
            the angle of the vector
    
    Returns
    -------
        float
            the x-component of the vector
    """
    radian_angle = angle * pi / 180
    return dist * cos(radian_angle)


def lengthdir_y(dist: float, angle: float) -> float:
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    Returns the y-component of a vector given a distance and angle.

    Parameters
    ----------
        dist : float
            the distance of the vector
        angle : float
            the angle of the vector
    
    Returns
    -------
        float
            the y-component of the vector
    """
    radian_angle = angle * pi / 180
    return dist * -sin(radian_angle)


def play_sound(sound_file):
    """
    Author: Yash Mahmud (32945795)

    Plays a sound effect.

    Parameters
    ----------
        sound_file : str
            the filename of the sound effect
    """
    snd = mixer.Sound('assets/sounds/' + sound_file + '.ogg')
    mixer.Sound.play(snd)


def play_music(music_file):
    """
    Author: Yash Mahmud (32945795)

    Plays a music file.

    Parameters
    ----------
        music_file : str
            the filename of the music file
    """
    mixer.music.load('assets/sounds/' + music_file + '.ogg')
    mixer.music.play(-1)


def toggle_music():
    """
    Author: Yash Mahmud (32945795)

    Toggles the background music.
    """
    if mixer.music.get_busy():
        mixer.music.stop()
    else:
        play_music("musBackground")
