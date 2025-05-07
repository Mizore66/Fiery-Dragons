from pygame.time import get_ticks

class Timer:
    """
    Author: Chua Xian Loong (32669747)

    A class used to represent a Timer.

    ...

    Attributes
    ----------
    duration : int
        The duration of the timer in milliseconds.
    break_duration : int
        The duration of the break timer in milliseconds.
    start_time : int
        The starting time of the timer.
    active : bool
        A flag indicating whether the timer is active.
    on_break : bool
        A flag indicating whether the break timer is active.
    break_start_time : int
        The starting time of the break timer.

    Methods
    -------
    activate():
        Activates the timer.
    deactivate():
        Deactivates the timer.
    start_break():
        Starts the break timer.
    end_break():
        Ends the break timer.
    update():
        Updates the state of the timer.
    is_time_up() -> bool:
        Checks if the timer has run out of duration.
    get_remaining_time() -> str:
        Returns the remaining time of the timer in the format MM:SS.
    get_break_time_left() -> str:
        Returns the remaining break time in the format MM:SS.
    """

    def __init__(self, duration: int, break_duration: int):
        """
        Author: Chua Xian Loong (32669747)

        Constructs all the necessary attributes for the Timer object.

        Parameters
        ----------
        duration : int
            The duration of the timer in seconds.
        break_duration : int
            The duration of the break timer in seconds.
        """
        self.duration = duration    * 1000 # convert to milliseconds
        self.break_duration = break_duration * 1000  # convert seconds to milliseconds        
        self.start_time = 0
        self.active = False
        self.on_break = False
        self.break_start_time = 0

    def activate(self):
        """
        Author: Chua Xian Loong (32669747)

        Activates the timer.
        """
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        """
        Author: Chua Xian Loong (32669747)

        Deactivates the timer.
        """
        self.active = False
        self.start_time = 0

    def start_break(self):
        """
        Author: Chua Xian Loong (32669747)

        Starts the break timer.
        """
        self.on_break = True
        self.break_start_time = get_ticks()

    def end_break(self):
        """
        Author: Chua Xian Loong (32669747)

        Ends the break timer.
        """
        self.on_break = False
        self.start_time = get_ticks()  # Restart game timer after break

    def update(self):
        """
        Author: Chua Xian Loong (32669747)

        Updates the state of the timer.
        """
        current_time = get_ticks()
        if self.on_break:
            if current_time - self.break_start_time >= self.break_duration:
                self.end_break()
        elif self.active:
            if current_time - self.start_time >= self.duration:
                self.start_break()

    def is_time_up(self):
        """
        Author: Chua Xian Loong (32669747)

        Checks if the timer has run out of duration.

        Returns
        -------
        bool
            True if the timer has run out, False otherwise.
        """
        if not self.active:
            return True
        current_time = get_ticks()
        return (current_time - self.start_time) >= self.duration
    
    def get_remaining_time(self):
        """
        Author: Chua Xian Loong (32669747)

        Returns the remaining time of the timer in the format MM:SS.

        Returns
        -------
        str
            The remaining time of the timer.
        """
        if not self.active:
            return "00:00"
        current_time = get_ticks()
        remaining_time = max(0, self.duration - (current_time - self.start_time))
        minutes = remaining_time // 60000
        seconds = (remaining_time % 60000) // 1000
        return f"{minutes:02}:{seconds:02}"
    
    def get_break_time_left(self):
        """
        Author: Chua Xian Loong (32669747)
        
        Returns the remaining break time in the format MM:SS.

        Returns
        -------
        str
            The remaining break time.
        """
        if not self.on_break:
            return "00:00"
        current_time = get_ticks()
        remaining_break_time = max(0, self.break_duration - (current_time - self.break_start_time))
        minutes = remaining_break_time // 60000
        seconds = (remaining_break_time % 60000) // 1000
        return f"{minutes:02}:{seconds:02}"