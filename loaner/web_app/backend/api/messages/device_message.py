# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Device messages for Device API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from protorpc import message_types
from protorpc import messages

from loaner.web_app.backend.api.messages import shared_messages
from loaner.web_app.backend.api.messages import shelf_messages


class Reminder(messages.Message):
  """Reminder ProtoRPC message.

  Attributes:
    level: int, Indicates if a reminder is due, overdue, or massively overdue.
    time:  DateTime at which the Device's borrower was reminded.
    count: int, Indicates the number of reminders seen.
  """
  level = messages.IntegerField(1)
  time = message_types.DateTimeField(2)
  count = messages.IntegerField(3)


class DeviceRequest(messages.Message):
  """General Device request ProtoRPC message with several identifiers.

  Attributes:
    asset_tag: str, The asset tag of the Chrome device.
    chrome_device_id: str, The Chrome device id of the Chrome device.
    serial_number: str, The serial number of the Chrome device.
    urlkey: str, The URL-safe key of a device.
    unknown_identifier: str, Either an asset tag or serial number of the device.
  """
  asset_tag = messages.StringField(1)
  chrome_device_id = messages.StringField(2)
  serial_number = messages.StringField(3)
  urlkey = messages.StringField(4)
  unknown_identifier = messages.StringField(5)


class Device(messages.Message):
  """Device ProtoRPC message.

  Attributes:
    serial_number: str, The serial number of the Chrome device.
    asset_tag: str, The asset tag of the Chrome device.
    enrolled: bool, Indicates the enrollment status of the device.
    device_model: int, Identifies the model name of the device.
    due_date: datetime, The date that device is due for return.
    last_know_healthy: datetime, The date to indicate the last known healthy
        status.
    shelf: shelf_messages.Shelf, The message for a shelf.
    assigned_user: str, The email of the user who is assigned to the device.
    assignment_date: datetime, The date the device was assigned to a user.
    current_ou: str, The current organizational unit the device belongs to.
    ou_change_date: datetime, The date the organizational unit was changed.
    locked: bool, Indicates whether or not the device is locked.
    lost: bool, Indicates whether or not the device is lost.
    mark_pending_return_date: datetime, The date a user marked device returned.
    chrome_device_id: str, A unique device ID.
    last_heartbeat: datetime, The date of the last time the device checked in.
    damaged: bool, Indicates the if the device is damaged.
    damaged_reason: str, A string denoting the reason for being reported as
        damaged.
    last_reminder: Reminder, Level, time, and count of the last reminder
        the device had.
    next_reminder: Reminder, Level, time, and count of the next reminder.
    page_size: int, The number of results to query for and display.
    page_number: int, the page index to offset the results.
    max_extend_date: datetime, Indicates maximum extend date a device can have.
    guest_enabled: bool, Indicates if guest mode has been already enabled.
    guest_permitted: bool, Indicates if guest mode has been allowed.
    given_name: str, The given name for the user.
    query: shared_message.SearchRequest, a message containing query options to
        conduct a search on an index.
  """
  serial_number = messages.StringField(1)
  asset_tag = messages.StringField(2)
  urlkey = messages.StringField(3)
  enrolled = messages.BooleanField(4, default=True)
  device_model = messages.StringField(5)
  due_date = message_types.DateTimeField(6)
  last_known_healthy = message_types.DateTimeField(7)
  shelf = messages.MessageField(shelf_messages.Shelf, 8)
  assigned_user = messages.StringField(9)
  assignment_date = message_types.DateTimeField(10)
  current_ou = messages.StringField(11)
  ou_changed_date = message_types.DateTimeField(12)
  locked = messages.BooleanField(13)
  lost = messages.BooleanField(14)
  mark_pending_return_date = message_types.DateTimeField(15)
  chrome_device_id = messages.StringField(16)
  last_heartbeat = message_types.DateTimeField(17)
  damaged = messages.BooleanField(18)
  damaged_reason = messages.StringField(19)
  last_reminder = messages.MessageField(Reminder, 20)
  next_reminder = messages.MessageField(Reminder, 21)
  page_size = messages.IntegerField(22, default=10)
  page_number = messages.IntegerField(23, default=1)
  max_extend_date = message_types.DateTimeField(24)
  guest_enabled = messages.BooleanField(25)
  guest_permitted = messages.BooleanField(26)
  given_name = messages.StringField(27)
  query = messages.MessageField(shared_messages.SearchRequest, 28)


class ListDevicesResponse(messages.Message):
  """List device response ProtoRPC message.

  Attributes:
    devices: Device, A device to display.
    total_results: int, the total number of results for a query.
  """
  devices = messages.MessageField(Device, 1, repeated=True)
  total_results = messages.IntegerField(2)
  total_pages = messages.IntegerField(3)


class DamagedRequest(messages.Message):
  """Damaged device ProtoRPC message.

  Attributes:
    device: DeviceRequest, A device to be fetched.
    damaged_reason: str, The reason the device is being reported as damaged.
  """
  device = messages.MessageField(DeviceRequest, 1)
  damaged_reason = messages.StringField(2)


class ExtendLoanRequest(messages.Message):
  """Loan extension request ProtoRPC message.

  Atrributes:
    device: DeviceRequest, A device to be fetched.
    extend_date: datetime, The date to extend the loan for.
  """
  device = messages.MessageField(DeviceRequest, 1)
  extend_date = message_types.DateTimeField(2)


class ListUserDeviceResponse(messages.Message):
  """UserDeviceResponse ProtoRPC message.

  Atrributes:
    devices: list, The list of devices assigned to the user.
  """
  devices = messages.MessageField(Device, 1, repeated=True)
