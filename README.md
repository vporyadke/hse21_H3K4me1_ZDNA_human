## Длины и положение пиков

## ![ENCFF540NGG.hg19.hist](images/ENCFF540NGG.hg19.hist.png)

![chip_seeker.ENCFF540NGG.hg19.filtered.plotAnnoPie](images/chip_seeker.ENCFF540NGG.hg19.filtered.plotAnnoPie.png)

![ENCFF759NWD.hg19.hist](images/ENCFF759NWD.hg19.hist.png)

![chip_seeker.H3K4me1_K562.intersect.plotAnnoPie](images/chip_seeker.H3K4me1_K562.intersect.plotAnnoPie.png)

## Известное расположение вторичной структуры ДНК (zhunt)



![chip_seeker.zhunt.plotAnnoPie](images/chip_seeker.zhunt.plotAnnoPie.png)

![zhunt.hist](images/zhunt.hist.png)

## Пересечения

`cat  *.hg19.filtered.bed  |   sort -k1,1 -k2,2n   |   bedtools merge   >  H3K4me1_K562.merge.hg19.bed`

`[filter with src/filter.py]`

`bedtools intersect -a zhunt.bed -b H3K4me1_K562.merge.hg19.filtered.bed > H3K4me1_K562.intersect.bed`

![chip_seeker.H3K4me1_K562.intersect.plotAnnoPie](images/chip_seeker.H3K4me1_K562.intersect.plotAnnoPie.png)

![H3K4me1_K562.intersect.hist](images/H3K4me1_K562.intersect.hist.png)

Пример пересечения: [chr1:162249261-162249269](http://genome-euro.ucsc.edu/cgi-bin/hgTracks?hgsid=265931980_nEsDGHzZ1C2JGNkAszdeuwK63Apa&db=hg19&position=chr1%3A162249261-162249269)

![intersect.genome_browser](images/intersect.genome_browser.png)

## Анализ

4983 пика ассоциированы с 3403 различными генами. Наиболее значимые категории - связанные с распознаванием запахов (detection of chemical stimulus involved in sensory perception of smell, sensory perception of smell, detection of chemical stimulus involved in sensory perception, sensory perception of chemical stimulus, detection of stimulus involved in sensory perception).