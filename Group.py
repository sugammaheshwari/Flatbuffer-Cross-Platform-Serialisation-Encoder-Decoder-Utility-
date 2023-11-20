# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Group(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Group()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGroup(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Group
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Group
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Group
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Group
    def AvgAge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Group
    def AvgWeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Group
    def NamesCnt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Group
    def Names(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Group
    def NamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Group
    def NamesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def GroupStart(builder):
    builder.StartObject(6)

def Start(builder):
    GroupStart(builder)

def GroupAddId(builder, id):
    builder.PrependInt16Slot(0, id, 0)

def AddId(builder, id):
    GroupAddId(builder, id)

def GroupAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    GroupAddName(builder, name)

def GroupAddAvgAge(builder, avgAge):
    builder.PrependFloat32Slot(2, avgAge, 0.0)

def AddAvgAge(builder, avgAge):
    GroupAddAvgAge(builder, avgAge)

def GroupAddAvgWeight(builder, avgWeight):
    builder.PrependFloat32Slot(3, avgWeight, 0.0)

def AddAvgWeight(builder, avgWeight):
    GroupAddAvgWeight(builder, avgWeight)

def GroupAddNamesCnt(builder, namesCnt):
    builder.PrependInt16Slot(4, namesCnt, 0)

def AddNamesCnt(builder, namesCnt):
    GroupAddNamesCnt(builder, namesCnt)

def GroupAddNames(builder, names):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(names), 0)

def AddNames(builder, names):
    GroupAddNames(builder, names)

def GroupStartNamesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartNamesVector(builder, numElems: int) -> int:
    return GroupStartNamesVector(builder, numElems)

def GroupEnd(builder):
    return builder.EndObject()

def End(builder):
    return GroupEnd(builder)