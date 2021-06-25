class Track:

    def __init__(self, name, artiste, timesplayed):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def __str__(self):
        return "Track Name: {}, Artiste Name: {}, Times Played: {}".format(self._name,self._artiste,self._timesplayed)

    def get_name(self):
        return self._name
    name = property(get_name)

    def get_artiste(self):
        return self._artiste
    artiste = property(get_artiste)

    def play(self):
        self._timesplayed += 1
        return "Playing: " + self.__str__()

class DLLNode:
    def __init__(self, item, next_node, previous_node):
        self._item = item
        self._next_node = next_node
        self._previous_node = previous_node
    
    def set_item(self, item):
        if not isinstance(item, Track) or item is not None:
            print("Item is not a track or None object")
        else:
            self._item = item
    
    def get_item(self):
        return self._item
    item = property(get_item, set_item)
    
    
    def set_next_node(self, next_node):
        if not isinstance(next_node, DLLNode):
            print("ERROR --> the pointer to next node is not of type DLLNode" )
        
        else:
            self._next_node = next_node
    
    def get_next_node(self):
        return self._next_node
    next_node = property(get_next_node, set_next_node)
    
    def set_previous_node(self, previous_node):
        if not isinstance(previous_node, DLLNode):
            print("ERROR --> the pointer to previous node is not of type DLLNode" )
        else:
            self._previous_node = previous_node

    def get_previous_node(self):
        return self._previous_node
    previous_node = property(get_previous_node, set_previous_node)

class PyToonz:

    def __init__(self):
       self.head_node = DLLNode(None,None,None)
       self.tail_node = DLLNode(None, None, self.head_node)
       self.head_node = DLLNode(None,self.tail_node,None) 
       self.num_of_tracks = 0
       self.selected_track = None
        
    def __str__(self):
        return_string = "Playlist:" + "\n"
        i = 0
        iterated_track = self.head_node.get_next_node()
        if self.num_of_tracks == 0:
            return_string = "Playlist Empty, try adding a new track"
            return return_string     
        
        while i < self.num_of_tracks:
            if iterated_track is not None:
                iterated_track_is_selected_str = ""
                if iterated_track == self.selected_track:
                    iterated_track_is_selected_str = "-->"
                return_string += iterated_track_is_selected_str + iterated_track.get_item().__str__() + "\n"
                iterated_track = iterated_track.get_next_node()
                i += 1
            else:
                return_string = "No tracks in pytoonz"
        return return_string

    def length(self):
        return self.num_of_tracks

    def get_current(self):
        if self.selected_track is not None:
            return self.selected_track.get_item()
        else:
            return None
        
    def add_after(self, track):
         
        if not isinstance(track, Track):
            print("ERROR IN ADD_AFTER() ->> The track your trying to add is not of the correct type")
        else:
            track_to_be_added = DLLNode(track, None, None)
            
            if self.selected_track == None:
                track_to_be_added.set_next_node(self.tail_node)
                self.tail_node.set_previous_node(track_to_be_added)
                self.head_node.set_next_node(track_to_be_added)
                track_to_be_added.set_previous_node(self.head_node)
                self.selected_track = track_to_be_added
                self.num_of_tracks += 1
            
            else:
                track_to_be_added.set_next_node(self.selected_track.get_next_node())
                self.selected_track.get_next_node().set_previous_node(track_to_be_added)
                self.selected_track.set_next_node(track_to_be_added)
                track_to_be_added.set_previous_node(self.selected_track)
                self.num_of_tracks += 1
            
    def add_track(self, track):
        
        if self.selected_track is not None:
            selected_track_holder = self.selected_track
            self.selected_track = self.tail_node.get_previous_node()
            self.add_after(track)
            self.selected_track = selected_track_holder

        else:
            self.add_after(track)

    def next_track(self):
        if self.selected_track is not None:
            if self.selected_track.get_next_node() == self.tail_node:
                self.selected_track = self.head_node.get_next_node()
            else:
                self.selected_track = self.selected_track.get_next_node()
            
        else:
            print("ERROR IN NEXT_TRACK() -> no next reference to selected track")
    
    def prev_track(self):
        if self.selected_track is not None:
            if self.selected_track.get_previous_node() == self.head_node:
                self.selected_track = self.tail_node.get_previous_node()
            else:
                self.selected_track = self.selected_track.get_previous_node()
        else:
            print("ERROR IN PREV_TRACK() -> no previous reference to selected track")

    def reset(self):
        if self.num_of_tracks != 0:
            self.selected_track = self.head_node.get_next_node()
        else:
            print("ERROR IN REST() -> No track next referece to head track")
    
    def play(self):
        if self.selected_track is not None:
            print(self.selected_track.get_item().play())
        else:
            print("ERROR IN PLAY() -> No Track is currently selected")

    def remove_current(self):
        if self.num_of_tracks != 0:
            if self.selected_track != None:
                if self.selected_track.get_next_node() != None and self.selected_track.get_previous_node() != None:
                    self.selected_track.get_previous_node().set_next_node(self.selected_track.get_next_node())
                    self.selected_track.get_next_node().set_previous_node(self.selected_track.get_previous_node())
                    self.next_track()
                    self.num_of_tracks -= 1
                    if self.num_of_tracks == 0:
                        self.selected_track = None
                
            else:
                return None
        else:
            print('ERROR IN REMOVE_CURRENT() -> No tracks in playlist')
        