import sublime, sublime_plugin

class SelectToBookmarkCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        """Get initial position"""
        initialPoint = self.view.sel()[0].begin()

        """Clear selected things (if any)"""
        self.view.sel().clear()

        """Move to next bookmark or previous bookmark"""
        forward = args.get('forward','true')
        if forward is True:
            self.view.run_command("next_bookmark")
        else:
            self.view.run_command("prev_bookmark")


        """Get current position (position of the bookmark)"""
        finalPoint = self.view.sel()[0].begin()

        """Clear selected things (if any)"""
        self.view.sel().clear()

        """Region to select"""
        regionToSelect = sublime.Region(initialPoint, finalPoint)

        """Add the region to the selection"""
        self.view.sel().add(regionToSelect)
