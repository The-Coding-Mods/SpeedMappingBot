import time

from discord import ui, Interaction, TextStyle


class SetupModal(ui.Modal, title="Setup SpeedMapping"):
    start_time = ui.TextInput(label="Start Time of the event (in unix timestamp)", style=TextStyle.short, min_length=10,
                              max_length=10, default=f"{int(time.time())}")
    length = ui.TextInput(label="Length speed mapping time (in minutes)", max_length=3, default="60")

    async def on_submit(self, interaction: Interaction) -> None:
        await interaction.response.send_message(f"Start time: {self.start_time} \n Length: {self.length}")
