# Define a component that counts button clicks
class ButtonClicker(rio.Component):
    # Define the attributes of the component. Rio will watch these
    # for changes and automatically update the GUI.
    clicks: int = 0

    # Define a method that increments the click count. We'll later
    # make a button that calls this method whenever it is pressed.
    def _on_press(self) -> None:
        self.clicks += 1

    # Define the `build` method. This method essentially tells rio
    # what a ButtonClicker component looks like. Whenever the state
    # of the ButtonClicker component changes, rio will call its
    # `build` method and update the GUI according to the output.
    def build(self) -> rio.Component:
        return rio.Column(
            rio.Button('Click me', on_press=self._on_press),
            rio.Text(f'You clicked the button {self.clicks} time(s)'),
        )

# Create an App and tell it to display a ButtonClicker when it starts
app = rio.App(build=ButtonClicker)
app.run_in_browser()  # Or `app.run_in_window()` to run as local app!