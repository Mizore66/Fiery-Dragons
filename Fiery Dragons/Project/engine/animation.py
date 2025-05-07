class Animation:
    """
    A class to represent an animation.

    Author: Anas Tarek Qumhiyeh (32985754)

    Attributes
    ----------
    frames : list
        A list of frames to animate.
    delay : int
        The delay between each frame.
    loop : bool
        A flag indicating whether the animation should loop.
    play : bool
        A flag indicating whether the animation is playing.
    update_func : function
        The function to call when updating the animation.
    current_frame : int
        The current frame of the animation.
    current_delay : int
        The current delay of the animation.

    Methods
    -------
    update():
        Updates the animation.
    on_update():
        A function to call when updating the animation.
    play_animation():
        Plays the animation.
    play_animation_at(frame: int):
        Plays the animation at a specific frame.
    get_current_frame():
        Returns the current frame of the animation.
    is_playing() -> bool:
        Checks if the animation is playing.
    ended() -> bool:
        Checks if the animation has ended.
    set_on_update(func):
        Sets the function to call when updating the animation.
    """

    def __init__(self, frames, delay, loop=False):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Constructs all the necessary attributes for the Animation object.

        Parameters
        ----------
            frames : list
                A list of frames to animate.
            delay : int
                The delay between each frame.
            loop : bool, optional
                A flag indicating whether the animation should loop (default is False).
        """
        self.frames = frames
        self.delay = delay
        self.loop = loop
        self.play = False
        self.update_func = self.on_update
        self.current_frame = 0
        self.current_delay = 0

    def update(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Updates the animation.
        """
        self.current_delay += 1
        if self.current_delay >= self.delay and self.play:
            self.current_delay = 0
            self.current_frame += 1
            self.update_func()
            if self.current_frame >= len(self.frames) and self.loop:
                self.current_frame = 0
            elif self.current_frame >= len(self.frames) and not self.loop:
                self.play = False

    def on_update(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        A function to call when updating the animation.
        """
        pass

    def play_animation(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Plays the animation.
        """
        self.current_frame = 0
        self.play = True

    def play_animation_at(self, frame: int):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Plays the animation at a specific frame.

        Parameters
        ----------
            frame : int
                The frame to play the animation at.
        """
        self.current_frame = frame
        self.play = True

    def get_current_frame(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Returns the current frame of the animation.

        Returns
        -------
            int
                The current frame of the animation.
        """
        return self.frames[self.current_frame]

    def is_playing(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Checks if the animation is playing.

        Returns
        -------
            bool
                True if the animation is playing, False otherwise.
        """
        return self.play

    def ended(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Checks if the animation has ended.

        Returns
        -------
            bool
                True if the animation has ended, False otherwise.
        """
        return self.current_frame == len(self.frames) - 1

    def set_on_update(self, func):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Sets the function to call when updating the animation.

        Parameters
        ----------
            func : function
                The function to call when updating the animation.
        """
        self.update_func = func
