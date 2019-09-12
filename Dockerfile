FROM stevenmburns/pysat_image:2019mar14 as tally_image

RUN \
    pip install matplotlib

COPY . /polish_floorplanner/

RUN \
    bash -c "source general/bin/activate && cd /polish_floorplanner/ && pip install ."














