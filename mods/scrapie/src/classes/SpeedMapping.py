class SpeedMapping:

    def __init__(self, start_time: int, length: int, guild_id: int = None, channel_id: int = None):
        self.start_time = start_time
        self.length = length
        self.guildId = guild_id
        self.channelId = channel_id

    def write_to_file(self):
        pass
