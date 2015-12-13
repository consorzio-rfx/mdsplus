from MDSplus import mdsExceptions, Device

class SPIDER(Device):
    """MARTe configuration"""
    parts=[{'path':':COMMENT', 'type':'text'},
      {'path':':CAMERA_FREQ', 'type':'numeric', 'value':10},
      {'path':':CAMERA_START', 'type':'numeric', 'value':0},
      {'path':':CAMERA_DURAT', 'type':'numeric', 'value':60},
      {'path':':CAEN_FREQ', 'type':'numeric', 'value':2},
      {'path':':CAEN_START', 'type':'numeric', 'value':0},
      {'path':':CAEN_DURAT', 'type':'numeric', 'value':30},
      {'path':':NI_FREQ', 'type':'numeric', 'value':10000},
      {'path':':NI_START', 'type':'numeric', 'value':0},
      {'path':':NI_DURAT', 'type':'numeric', 'value':60},
      {'path':':NI6368_FREQ', 'type':'numeric', 'value':10000},
      {'path':':NI6368_START', 'type':'numeric', 'value':0},
      {'path':':NI6368_DURAT', 'type':'numeric', 'value':60},
      {'path':':BREAK_DEAD', 'type':'numeric', 'value':10},
      {'path':':BREAK_REC', 'type':'numeric', 'value':0},
      {'path':'.WAVE_1', 'type':'structure'},
      {'path':'.WAVE_1:WAVE', 'type':'signal'},
      {'path':'.WAVE_1:MIN_X', 'type':'numeric'},
      {'path':'.WAVE_1:MAX_X', 'type':'numeric'},
      {'path':'.WAVE_1:MIN_Y', 'type':'numeric'},
      {'path':'.WAVE_1:MAX_Y', 'type':'numeric'},
      {'path':'.WAVE_2', 'type':'structure'},
      {'path':'.WAVE_2:WAVE', 'type':'signal'},
      {'path':'.WAVE_2:MIN_X', 'type':'numeric'},
      {'path':'.WAVE_2:MAX_X', 'type':'numeric'},
      {'path':'.WAVE_2:MIN_Y', 'type':'numeric'},
      {'path':'.WAVE_2:MAX_Y', 'type':'numeric'},
      {'path':'.WAVE_3', 'type':'structure'},
      {'path':'.WAVE_3:WAVE', 'type':'signal'},
      {'path':'.WAVE_3:MIN_X', 'type':'numeric'},
      {'path':'.WAVE_3:MAX_X', 'type':'numeric'},
      {'path':'.WAVE_3:MIN_Y', 'type':'numeric'},
      {'path':'.WAVE_3:MAX_Y', 'type':'numeric'},
      {'path':'.WAVE_4', 'type':'structure'},
      {'path':'.WAVE_4:WAVE', 'type':'signal'},
      {'path':'.WAVE_4:MIN_X', 'type':'numeric'},
      {'path':'.WAVE_4:MAX_X', 'type':'numeric'},
      {'path':'.WAVE_4:MIN_Y', 'type':'numeric'},
      {'path':'.WAVE_4:MAX_Y', 'type':'numeric'},
      {'path':'.WAVE_REC', 'type':'structure'},
      {'path':'.WAVE_REC:WAVE', 'type':'signal'},
      {'path':'.WAVE_REC:MIN_X', 'type':'numeric'},
      {'path':'.WAVE_REC:MAX_X', 'type':'numeric'},
      {'path':'.WAVE_REC:MIN_Y', 'type':'numeric'},
      {'path':'.WAVE_REC:MAX_Y', 'type':'numeric'}]
