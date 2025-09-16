#!/bin/bash
#
#
#
#
#
source ../pyRFXtrx/bin/activate
TEMP_SOUHAITEE=19
while true
do
	sleep 1
	TEMP_RELEVEE=$(./acquire.py c7:00)
	if (( $(echo "$TEMP_RELEVEE < $TEMP_SOUHAITEE" | bc -l) ))
	then
		echo "off - $(date) - $TEMP_RELEVEE"
		./sendFoffFrigo_ventilateur_pm.py
	else
		echo "on  - $(date) - $TEMP_RELEVEE"
		./sendFonFrigo_ventilateur_pm.py
	fi
done
