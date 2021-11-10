import base64, codecs
magic = 'SWxsbElJbGxJSWxsbGxsbGxJbElJSWxJSWxsSWxsbElJSUlsSWxsbElJbElJbGxJbGxsSUlJSUlsbGxJSUlsbElJbGxsbGxJbElsSUlsSWxsbGxsSWxsSUlJbElJSUlsbElsSWxJbGwgPSAxNTYNCnV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dSA9IDIyOQ0KYWFBQWFBQUFBQUFBYUFBYWFhYWFBQWFhYUFBQUFBQUFBYUFBQUFBQUFBQWFhQUFhQWFhQUFBQWFhQWFBYWFBYUFhYWFhYUFhYWFBYUFBYUFhQWFBQWFhQWFBQWFhYUFBQUFhYSA9IDI4OQ0KYUFBYWFhQWFBYWFhQUFBYUFhYWFhQUFhYWFBYWFhQWFhYUFBYUFhQUFBQUFBYUFhYUFhYUFBYUFhQUFhQUFBQWFhYUFhQWFBQWFhYUFhYWFBYUFBQWFhYUFBYWFhYWFBQUEgPSA1ODUNCmxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbCA9IDIwMA0KcjE2MzY0ODEzOTExMDI3NTgyOTQgPSAiaWZzYVNnYVFPSEtGcnREeXRjaUJGUWlqY3JyUFhCSmplS0tRY2R5Q2dCVnRobW1wZGxxWGJKdXVpVkt6R0htQWVJVElQbkxSVW9pYVZCWiINCmFhYUFBYWFhYWFBYUFhYWFhQUFBYWFhYUFhQWFBQUFBYUFBYWFhYUFhQUFhQUFhQUFhYWFBQUFhQUFhQUFBQUFBYWFhQUFhQWFhQUFhYUFBQWFBQWFhYWFBYUFBID0gMTQ3DQpBYWFhYUFBYUFBQUFhQWFhYUFhYWFBQWFBQUFhQUFhYWFhYUFhQUFBYWFBYWFhYWFhYUFBYWFBQUFhYUFBQUFhQUFBQWFhYWFBYUFBQUFBQWFhYWFhQUFBQUEgPSAiR1dQa1RRRXhnbXFnZUpvU0VUQU55ckxsTW5EWm5oclZ4QmZHVG15QVdieFJSQ0FLc2tDTkZ3a0pLQXJjZ0JZd0Vsb1poTWdBVHRkcnVlcCINCmI4OCA9IDQ2OA0KQUFBQWFBYUFhYWFBQUFBQUFhYWFBQWFBYUFBYWFhQWFhQUFBQUFhYWFhYWFBQWFBYUFhYUFhYUFhYWFBYUFBYWFhQUFBQWFBQWFBYWFhYUFhQWFhYUEgPSAzODENCksxNjM2NDgxMzkxMTAyMDk5Mjg0ID0gMTU4DQpsbGxsSWxsSWxsbGxJbGxsSUlJSWxsbElJbElJSUlsbGxJSWxJSUlJbElJbElJbGxJbElsbElsbElJSUlsbGxsSWxsbElsSUlJbElsbGxJbGxsID0gIkJsZVFLZ3FQYWJRbXJvV01CQ2pZb3NZclhadFpuRG5LcE1Cd0tvcmdnQktRY05HaXNCdWRWbVFocGx4Rm1sZ1hOb01sQWt0SVJCcnhXRHIiDQpsSWxsbElJbGxsbElsSWxJbGxsSUlJSUlJbGxsSUlsbGxJbGxJSUlsbElJbGxsSWxJSUlsSWxsSUlJbElsSUlJbGxJSWxsbGxsbElsSWxJbCA9IDIxMg0Kczc4ID0gImNDRktCYVl5Y2NsUHRDb0xtR0tQY1hHTFRraHJDYmpScnJ1eUppV0dldE96enZkRmJ0bElFZlpBWkROeEJGVEpRRFB2RklzYmxWS2NGY2UiDQpkR3hxcENienpZYU1nZVZPaVdBVkJxcWtyRlhCUlVRVWFXbXh0eHBzaElOWFlCVmpQSkh6cmVhbWpWcmtnY0dra0ZBWHhDS0hhSUVCUGdZNzYgPSAyODANCmROSnNIWklhVVhXSmdMamd3SHRMYWNuYmxtd3VVZWdhS2JHSUxVaHlxc0hwRUJiY0JISUNDS052UVR1alZGUG1RaFVyU2V0WUZraElZbGQ3NCA9IDI5NQ0KYUFBYWFBYWFhQWFBYUFhQUFhQWFhYUFBYWFhQWFhQWFBYUFBQWFhQWFBQWFBYWFhQUFBQWFhQWFBYWFBYUFBYUFhYUFhQWFhID0gMzAyDQpHSU1RRkNhRVBIeURqUmNUT0ZZQkhuQ3dsSVpNT2VQV1NIWVdrY2x6c0hqb2drRnJqb0FmYmV3d3J1UG5Kb3pEcFhzcWJPeFBqdEdEVlhQNzAgPSAzODENClk2OCA9IDQ5NA0KWHlXUXBhY0xTTEJoQVNlRWNhWHR0QlptYXhzYXNqdlR6RVdBQlFhS21ETkZtQWJzeWN3Y2ptRUtzVXBwc3dYVE9zQnJuYURCYUNRUU9aWTY2ID0gMTQ5DQpZNjQgPSAiSHpGem9iQklEVG92U0lnalBkZEh3QlF5enRqTEZlbGJtcXRxWlB3cXZIY0dFZGRDcU5kV09JTXFYV3FySGhHU0R6UWRvUG50UUZhd2JZZyINCllhYnlkUU9zR1BJSFFFSW5Pd0lEQmZJSHNYV0psRURRcnRVWUZJbWFhVGFNcGZMb2ROTkdXQ2dnVGFWVUNSUmRNUEljdXJobURyc3dMZHM2MiA9ICJwVFZ0b1dIQ2NBeWRuakJFR0J6alR3UHFFbnpwZmR5dFJWU091R2hHSWh3Qk5vS2pUSGJPVWlkUERxeGlnSHFSYkFGSlpZeXBtbmZkVkxEIg0KclFMYmF1b3R1d0tSR1NZVGdpT1NzYUNOS3FOaEVzbHNZVWh6aXNReUhTZFZaalJkUlBOQlpUSGhWTGd6ZEZjU0lrYU9RTUlyakFMcEpYbDYwID0gIlVSbXNQTnFZdklQVnRVREdBRG1xcUl4Z2p1a25mcFVxZVhGZWNSaEZOR25EVGZWbFV4c2Z3YmRwb1pFWm5nY1dhS2FlUkphcXBoaG5XV04iDQppNTggPSAiWk9XWERTRGFsR2ROeHpXTHVXd0ltVE1BRGtZQW9xckVYeW13ZUdwWGhvQWd4RXB3Skdob3dBdXNCZElkd29xd1lVWWtic0dac3JnZ01mRyINCmRQWkx2bVRDWVBUQnpBT0VMbWJJb1Rja2lSeEtTak11RmpqU1dYRmhLWGJLd2dKQkJLdUhLZ2pjelhIUmxXTERRS0R0Q1NsTnZqUWZJVGg1NiA9IDQ2NQ0KUjU0ID0gInhMUEJmVkhEckl3WWdXcll6VFRHbFBvWHJHR2ZZSVJCRU1QVEZMZkNaeUhWcXZwRklKQVFBT1JvRFFYZ0R3cHhlR1hDQnVhUFR0V2FRZVgiDQpBQWFhQWFhYUFBYUFBYUFBQWFBQWFhYUFhYUFBYWFhQUFhQWFhYUFBQUFhQUFhYUFhYUFhID0gIlFLVXBkZkhJd0FueUdvSENHTVVkUVNSd0JoQlNxTldlQVJYcXNtY2hiYlp2TlhicGpOdEpXb2ZIQnp0dG5VQ1R2cFlhSEVuVnJLWFplam8iDQpBQUFBYWFhYUFhQWFhQWFhQUFhQUFBYUFhYUFBYWFhQWFhQUFhQUFBQWFBQWFBQWFhYSA9IDMxNQ0KVXRKVGxRU2paVkREVWFMQlppbUxTQ0VReXlObWlObWpYTW5vZkp3R3RXRXRKWVNlZEhoaFRpbVRadWRKaWhxUVdidXVPVEdKTVh1R0J6RDQ4ID0gIkFsSHlIckN3aXRVZGZibWpLV29VcmFQQ3ZqZHRudmhHemR6Ukp0WVZ6bGhycHRZelNZTFZqZVh5d0FKUUZTVkpySEVMR2JPY0lid1VNdEsiDQphQUFhYUFBQUFhYWFhYWFhYWFBQUFBQUFhQUFhQWFBYUFBQUFBQWFhQUFBQUFhID0gInFRcGxZZXlsemtkdGRBeUhTQkVUdXFRWVlnRUd4bUtRdmNEclJhY0poUWRNREJycXdsS2lNdWtKV0ZJVWlWT2JQb2NIUVdYQXpNZ2xUb2MiDQpoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaCA9ICJwUEp5ZW5GRUR6S0lTUXVBdGVMc3JPc2VqdU5CRGxpQ0ZocWpza0JHZEhZaVBuWEZHb1JkaFlrUWRVR3JRTGlKbU1Yd2diTGFHVVV3cXJrIg0KQUFhYUFhYUFBYWFhQWFhYWFhYUFBYUFhYUFBQWFBQUFhYUFBYWFBYUFBID0gImFPeHRzcnJiUFBFcVlvVlVlUExMcGZ4RW9Jc255eUhhSkhpek5IYXBOWnZ4ZUtzU3hXbk9ZemZsUnREWkhqY1lUUnl5QVJrR0RsZGZsSlkiDQpPNDAgPSAzMzQNCm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubm5uID0gIlZZYllYSFloZlRvdnBYTE9TV1BEUFRwV3JvcFlXSWRNQ2JWek9IcXBid0hhUkF4dm5MZVhVS2hZbVpYUEpQeWVtWWxEdEh3ckZSekFuTWciDQpBYWFBQUFBQWFhQUFBQUFhQWFhYUFhYWFBQUFBQUFBYUFBQUEgPSA2NjYNCkFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUEgPSAzNTENCklJbElsbGxsbElJbElJbElJbGxsSUlJbElsSWxJbGxsID0gNDIyDQptMzAgPSA2NzQNCnV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXV1dXUgPSAyMzMNCklJSUlJbElsbGxsSUlJbElsSUlJSWxsSWxsID0gMjk4DQpTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1MgPSAidHNZc2NVS0lFdUNyYURkWmNoVVVJVHZtQ3VWak54ZlJCWmRhbVdsV2hpbGdzWEhRQ3ZQU0Z1eEJneFRrZ1FGRGlsWUtwS0pwY2dtZWlhQyINCloyMiA9IDQ3MQ0KYWFhYUFBQUFBQWFBYWFBYWFBQUEgPSAyMjMNCmxJbElsSWxJbElsSUlsbGxJSSA9IDM2NQ0KaGhoaGhoaGhoaGhoaGhoaCA9IDM1NQ0KSWxsbGxJSUlJbElsSWwgPSA0NTkNCkRyb2J0bmNrU0FpWU1PTVh1cnVSUGliZHVnY1R3Q2tabHVKWnpiV2NjQWxJeWZMclVQZGhQZlVEd3pRZG9aa1BoSVF2QUJDR3p0ZXB0eUwxMiA9IDI2Mw0KbGxsbElJSWxJSSA9IDMzNg0KUzE2MzY0ODEzOTEwOTgwMzg3OCA9IDMyMw0KSUlsSWxsID0gMTk5DQpsSUlsID0gNDU1DQpKR3ZJRXZ3bmt2WVBtZGxxZWl3alhMRU1lbFhUYVhKbnp0Q014THNBRENEQVZ4S05KbUdod0JEV0tIYkd3R3l5eFZ6UnJQUnJzVWpDb1hrMiA9ICJXRENIYnFzRmRGc0tIZXRPblRDQnFSc2N0SUJ6bkdLZk1KSmNwQlJ4WFNmYk54WEpjcmVETVdQWWhxVEdLY2dEdk9YZXptbEpiekZSU1F0Ig0KDQoNCg0KZnJvbSB0ZWxlZ3JhbSAuZXh0IGltcG9ydCBVcGRhdGVyICxDb21tYW5kSGFuZGxlciAsTWVzc2FnZUhhbmRsZXIgLEZpbHRlcnMgI2xpbmU6Mjpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgVXBkYXRlciwgQ29tbWFuZEhhbmRsZXIsIE1lc3NhZ2VIYW5kbGVyLCBGaWx0ZXJzDQppbXBvcnQgbG9nZ2luZyAjbGluZTozOmltcG9ydCBsb2dnaW5nDQpmcm9tIHNlbGVuaXVtIC53ZWJkcml2ZXIgLnN1cHBvcnQgLnVpIGltcG9ydCBTZWxlY3QgI2xpbmU6NDpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5zdXBwb3J0LnVpIGltcG9ydCBTZWxlY3QNCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlciAjbGluZTo1OmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlcg0KZnJvbSB0ZWxlZ3JhbSBpbXBvcnQgSW5saW5lS2V5Ym9hcmRCdXR0b24gLElubGluZUtleWJvYXJkTWFya3VwICxVcGRhdGUgI2xpbmU6Njpmcm9tIHRlbGVncmFtIGltcG9ydCBJbmxpbmVLZXlib2FyZEJ1dHRvbiwgSW5saW5lS2V5Ym9hcmRNYXJrdXAsIFVwZGF0ZQ0KZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmtleXMgaW1wb3J0IEtleXMgI2xpbmU6Nzpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jb21tb24ua2V5cyBpbXBvcnQgS2V5cw0KZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jaHJvbWUgLm9wdGlvbnMgaW1wb3J0IE9wdGlvbnMgI2xpbmU6ODpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jaHJvbWUub3B0aW9ucyBpbXBvcnQgT3B0aW9ucw0KZnJvbSBzZWxlbml1b'
love = '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'
god = 'Rfa2V5cyAoS2V5cyAuQ09OVFJPTCAsJ2EnKSNsaW5lOjcyOmxpbmtiYXI0LnNlbmRfa2V5cyhLZXlzLkNPTlRST0wsICdhJykNCiAgICBPTzBPT09PT09PTzAwMDAwMCAuc2VuZF9rZXlzIChLZXlzIC5CQUNLU1BBQ0UgKSNsaW5lOjczOmxpbmtiYXI0LnNlbmRfa2V5cyhLZXlzLkJBQ0tTUEFDRSkNCiAgICBPTzBPT09PT09PTzAwMDAwMCAuc2VuZF9rZXlzIChPTzBPME9PT09PTzAwT08wTyAuYXJncyApI2xpbmU6NzQ6bGlua2JhcjQuc2VuZF9rZXlzKGNvbnRleHQuYXJncykNCiAgICBPT09PT08wT08wT08wTzAwMCA9T09PTzBPT08wT08wTzBPT08gLmZpbmRfZWxlbWVudF9ieV94cGF0aCAoIi8vaW5wdXRbQGNsYXNzPSdhbnQtY2FsZW5kYXItcGlja2VyLWlucHV0IGFudC1pbnB1dCddIikjbGluZTo3ODpkYXRhZXIgPSBicm93c2VyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgiLy9pbnB1dFtAY2xhc3M9J2FudC1jYWxlbmRhci1waWNrZXItaW5wdXQgYW50LWlucHV0J10iKQ0KICAgIE9PT09PTzBPTzBPTzBPMDAwIC5jbGljayAoKSNsaW5lOjc5OmRhdGFlci5jbGljaygpDQogICAgdGltZSAuc2xlZXAgKDEgKSNsaW5lOjgwOnRpbWUuc2xlZXAoMSkNCiAgICBmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZSAjbGluZTo4Mjpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQ0KICAgIGZyb20gZGF0ZXRpbWUgaW1wb3J0IHRpbWVkZWx0YSAjbGluZTo4Mzpmcm9tIGRhdGV0aW1lIGltcG9ydCB0aW1lZGVsdGENCiAgICBmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRlICNsaW5lOjg0OmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGUNCiAgICBPTzBPME9PTzAwTzBPT08wMCA9ZGF0ZSAudG9kYXkgKCkjbGluZTo4NTpCZWdpbmRhdGVzdHJpbmcgPSBkYXRlLnRvZGF5KCkNCiAgICBPT09PME8wT08wME9PTzBPMCA9MzAgI2xpbmU6ODY6ZGF0ID0gMzANCiAgICBPME8wMDAwTzBPMDBPME8wTyA9T08wTzBPT08wME8wT09PMDAgK3RpbWVkZWx0YSAoZGF5cyA9T09PTzBPME9PMDBPT08wTzAgKSNsaW5lOjg5OkVuZGRhdGUgPSBCZWdpbmRhdGVzdHJpbmcgKyB0aW1lZGVsdGEoZGF5cz1kYXQpDQogICAgZGF0ZSA9Zid7TzBPMDAwME8wTzAwTzBPME99IDE1OjI2JyNsaW5lOjkxOmRhdGUgPSBmJ3tFbmRkYXRlfSAxNToyNicNCiAgICBPT09PME9PTzBPTzBPME9PTyAuZmluZF9lbGVtZW50X2J5X3hwYXRoICgiLy9pbnB1dFtAY2xhc3M9J2FudC1jYWxlbmRhci1pbnB1dCAnXSIpLnNlbmRfa2V5cyAoZGF0ZSApI2xpbmU6OTI6YnJvd3Nlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoIi8vaW5wdXRbQGNsYXNzPSdhbnQtY2FsZW5kYXItaW5wdXQgJ10iKS5zZW5kX2tleXMoZGF0ZSkNCiAgICBPT09PME8wTzBPTzBPMDAwTyA9T09PTzBPT08wT08wTzBPT08gLmZpbmRfZWxlbWVudF9ieV94cGF0aCAoIi8vQVtAY2xhc3M9J2FudC1jYWxlbmRhci1vay1idG4nXSIpI2xpbmU6OTQ6b2sgPSBicm93c2VyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgiLy9BW0BjbGFzcz0nYW50LWNhbGVuZGFyLW9rLWJ0biddIikNCiAgICBPT09PME8wTzBPTzBPMDAwTyAuY2xpY2sgKCkjbGluZTo5NTpvay5jbGljaygpDQogICAgdGltZSAuc2xlZXAgKDEgKSNsaW5lOjk3OnRpbWUuc2xlZXAoMSkNCiAgICBPMDBPTzBPMDBPTzAwMDAwTyA9T09PTzBPT08wT08wTzBPT08gLmZpbmRfZWxlbWVudF9ieV94cGF0aCAoJygvL0JVVFRPTltAY2xhc3M9ImFudC1zd2l0Y2giXSlbMl0nKSNsaW5lOjk5OmxpbmtiYXI1ID0gYnJvd3Nlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJygvL0JVVFRPTltAY2xhc3M9ImFudC1zd2l0Y2giXSlbMl0nKQ0KICAgIE8wME9PME8wME9PMDAwMDBPIC5jbGljayAoKSNsaW5lOjEwMDpsaW5rYmFyNS5jbGljaygpDQogICAgTzBPME9PT09PT09PMDBPTzAgPU9PT08wT09PME9PME8wT09PIC5maW5kX2VsZW1lbnRfYnlfeHBhdGggKCcoLy9JTlBVVFtAdHlwZT0ibnVtYmVyIl0pWzFdJykuZ2V0X2F0dHJpYnV0ZSAoInZhbHVlIikjbGluZToxMDM6cG9ydCA9IGJyb3dzZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcoLy9JTlBVVFtAdHlwZT0ibnVtYmVyIl0pWzFdJykuZ2V0X2F0dHJpYnV0ZSgidmFsdWUiKQ0KICAgIE9PT09PME9PTzAwMDAwTzBPID1PT09PME9PTzBPTzBPME9PTyAuZmluZF9lbGVtZW50X2J5X3hwYXRoICgnKC8vSU5QVVRbQHR5cGU9InRleHQiXSlbM10nKS5nZXRfYXR0cmlidXRlICgidmFsdWUiKSNsaW5lOjEwNDp1aWQgPSBicm93c2VyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnKC8vSU5QVVRbQHR5cGU9InRleHQiXSlbM10nKS5nZXRfYXR0cmlidXRlKCJ2YWx1ZSIpDQogICAgT09PME8wME9PME8wT08wT08gPU9PT08wT09PME9PME8wT09PIC5maW5kX2VsZW1lbnRfYnlfeHBhdGggKCcvL0lOUFVUW0Byb2xlPSJzcGluYnV0dG9uIl0nKS5nZXRfYXR0cmlidXRlICgidmFsdWUiKSNsaW5lOjEwNTpnYiA9ICBicm93c2VyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9JTlBVVFtAcm9sZT0ic3BpbmJ1dHRvbiJdJykuZ2V0X2F0dHJpYnV0ZSgidmFsdWUiKQ0KICAgIE9PME8wT09PT09PMDBPTzBPIC5ib3QgLnNlbmRfbWVzc2FnZSAoY2hhdF9pZCA9T08wME8wTzAwTzBPTzBPT08gLm1lc3NhZ2UgLmNoYXRfaWQgLHRleHQgPWYi4pyFIFNVQ0NFU1NGVUxMWSBDUkVBVEVEIOKchVxuXG7wn5SwUGFpZCBQcml2ZXQgVjJSQVkg8J+UsFxuXG7hl5ogIEhvc3QgSVAg4oCiIOC5m2B7SVB9YFxu4ZeaICBQb3J0IOKAoiDguZtge08wTzBPT09PT09PTzAwT08wfWBcbuGXmiAgRGF0YSBMaW1pdCDigKIgYHtPT08wTzAwT08wTzBPTzBPT31HQmBcbuGXmiAgRXhwaXJlIGRhdGUg4oCiIGB7TzBPMDAwME8wTzAwTzBPME99YFxu4ZeaICBVVWlkIOKAoiDguZtge09PT09PME9PTzAwMDAwTzBPfWBcblxu4L+CICBQcm90b2NvbCDigKIgdm1lc3MvSFRUUFxuXG5bLV0g4pWQ4pSA4pSA4pSA4pSA4pSA4pSA4pSA4peH4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pWQXG4gYHZtZXNzOi8vZXcwS0lDQWlkaUk2SUNJeUlpd05DaUFnSW5Ceklqb2dJaUlzRFFvZ0lDSmhaR1FpT2lBaVNWQWlMQTBLSUNBaWNHOXlkQ0k2SUNJd0lpd05DaUFnSW1sa0lqb2dJbFZWU1VRaUxBMEtJQ0FpWVdsa0lqb2dJakFpTEEwS0lDQWljMk41SWpvZ0ltRjFkRzhpTEEwS0lDQWlibVYwSWpvZ0luUmpjQ0lzRFFvZ0lDSjBlWEJsSWpvZ0ltaDBkSEFpTEEwS0lDQWlhRzl6ZENJNklDSlpUMVV1Y0dGNWJHOWtaUzVJVDFOVUlpd05DaUFnSW5CaGRHZ2lPaUFpSWl3TkNpQWdJblJzY3lJNklDSWlMQTBLSUNBaWMyNXBJam9nSWlJTkNuMD1gXG5bLV0g4pWQ4pSA4pSA4pSA4pSA4pSA4pSA4pSA4peH4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pWQXG7igLrimKxb4oCiXSBTQ1JJUFRTIOKVkOKXhyBEQVJLVjJSQVkg4peH4pWQIFvigKJd4pisIOKAolxuXG5b8J+nv1lPVSBUZWNo8J+nv10oaHR0cHM6Ly90Lm1lL1lvdVRlY2hfVlBOX0hVQikiLHBhcnNlX21vZGUgPXRlbGVncmFtIC5QYXJzZU1vZGUgLk1BUktET1dOICkjbGluZToxMDg6Y29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLm1lc3NhZ2UuY2hhdF9pZCwgdGV4dD1mIuKchSBTVUNDRVNTRlVMTFkgQ1JFQVRFRCDinIVcblxu8J+UsFBhaWQgUHJpdmV0IFYyUkFZIPCflLBcblxu4ZeaICBIb3N0IElQIOKAoiDguZtge0lQfWBcbuGXmiAgUG9ydCDigKIg4LmbYHtwb3J0fWBcbuGXmiAgRGF0YSBMaW1pdCDigKIgYHtnYn1HQmBcbuGXmiAgRXhwaXJlIGRhdGUg4oCiIGB7RW5kZGF0ZX1gXG7hl5ogIFVVaWQg4oCiIOC5m2B7dWlkfWBcblxu4L+CICBQcm90b2NvbCDigKIgdm1lc3MvSFRUUFxuXG5bLV0g4pWQ4pSA4pSA4pSA4pSA4pSA4pSA4pSA4peH4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pWQXG4gYHZtZXNzOi8vZXcwS0lDQWlkaUk2SUNJeUlpd05DaUFnSW5Ceklqb2dJaUlzRFFvZ0lDSmhaR1FpT2lBaVNWQWlMQTBLSUNBaWNHOXlkQ0k2SUNJd0lpd05DaUFnSW1sa0lqb2dJbFZWU1VRaUxBMEtJQ0FpWVdsa0lqb2dJakFpTEEwS0lDQWljMk41SWpvZ0ltRjFkRzhpTEEwS0lDQWlibVYwSWpvZ0luUmpjQ0lzRFFvZ0lDSjBlWEJsSWpvZ0ltaDBkSEFpTEEwS0lDQWlhRzl6ZENJNklDSlpUMVV1Y0dGNWJHOWtaUzVJVDFOVUlpd05DaUFnSW5CaGRHZ2lPaUFpSWl3TkNpQWdJblJzY3lJNklDSWlMQTBLSUNBaWMyNXBJam9nSWlJTkNuMD1gXG5bLV0g4pWQ4pSA4pSA4pSA4pSA4pSA4pSA4pSA4peH4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pWQXG7igLrimKxb4oCiXSBTQ1JJUFRTIOKVkOKXhyBEQVJLVjJSQVkg4peH4pWQIFvigKJd4pisIOKAolxuXG5b8J+nv1lPVSBUZWNo8J+nv10oaHR0cHM6Ly90Lm1lL1lvdVRlY2hfVlBOX0hVQikiLCBwYXJzZV9tb2RlPXRlbGVncmFtLlBhcnNlTW9kZS5NQVJLRE9XTikNCiAgICBPTzBPMDBPMDAwT09PMDAwMCA9T09PTzBPT08wT08wTzBPT08gLmZpbmRfZWxlbWVudF9ieV94cGF0aCAoJygvL0JVVFRPTltAY2xhc3M9ImFudC1idG4gYW50LWJ0bi1wcmltYXJ5Il0pWzFdJykjbGluZToxMTA6bGlua2JhcjcgPSBicm93c2VyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnKC8vQlVUVE9OW0BjbGFzcz0iYW50LWJ0biBhbnQtYnRuLXByaW1hcnkiXSlbMV0nKQ0KICAgIE9PME8wME8wMDBPT08wMDAwIC5jbGljayAoKSNsaW5lOjExMTpsaW5rYmFyNy5jbGljaygpDQogICAgT09PTzBPT08wT08wTzBPT08gLmNsb3NlICgpI2xpbmU6MTEzOmJyb3dzZXIuY2xvc2UoKQ0KDQoNCmwgPSAiRHFCbXdzZ2R3YUh6TlFRcGRSVGdLUFhETHVnaktQQWlNUlh2ZVNJZ1ZPQ3B4S2lqQ3dnY2psWW5yRnVKbHhRZVlURXVGS25rVG1QRlliUSINCkFhQSA9IDUyOQ0KbGxsSWwgPSAiaUJDd0RSeU9UdGd3ZGxvamJjS05Gb1NaS25iTkdoR2FnRmdJT0ZuaW1Db1F3ZURnR1hBUUJhQVFZeEhHdElQREtxSHVTa2luZHJydndHTyINCmI3ID0gIkFXVGVqQm1tQU5qZGxxSWxvTkVuc1VNY1VGa1J'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
