from database.db import get_connection
from .entities.Bus import Bus
from datetime import datetime

class BusModel():

  @classmethod
  def get_bus(self):
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus")
        resultset=cursor.fetchall()

        for row in resultset:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          buslist.append(bus.to_JESON())
      
      connection.close()
      return buslist

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def get_bus_rtime(self):
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus WHERE datatime = clock_timestamp()")
        row=cursor.fetchone()

        bus = None
        if row != None:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          bus=bus.to_JESON()
      
      connection.close()
      return bus

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def get_bus_time(self):
    
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus WERE datetime =")
        resultset=cursor.fetchall()

        for row in resultset:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          buslist.append(bus.to_JESON())
      
      connection.close()
      return buslist

    except Exception as ex:
      raise Exception(ex)