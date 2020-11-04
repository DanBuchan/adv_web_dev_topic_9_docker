from django.db import models


class EC(models.Model):
    ec_name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.ec_name


class Sequencing(models.Model):
    sequencing_factory = models.CharField(max_length=256,
                                          null=False, blank=False)
    factory_location = models.CharField(max_length=256,
                                        null=False, blank=False)

    def __str__(self):
        return self.factory_location


class Gene(models.Model):
    gene_id = models.CharField(max_length=256, null=False,
                               blank=False, db_index=True)
    entity = models.CharField(max_length=256, null=False,
                              blank=False)
    start = models.IntegerField(null=False, blank=True)
    stop = models.IntegerField(null=False, blank=True)
    sense = models.CharField(max_length=1)
    start_codon = models.CharField(max_length=1, default="M")
    sequencing = models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)
    ec = models.ForeignKey(EC, on_delete=models.DO_NOTHING)
    access = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.gene_id


class Product(models.Model):
    type = models.CharField(max_length=256, null=False,
                            blank=False)
    product = models.CharField(max_length=256, null=False, blank=False)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)


class Attribute(models.Model):
    key = models.CharField(max_length=256, null=False, blank=False)
    value = models.CharField(max_length=256, null=False, blank=False)
    gene = models.ManyToManyField(Gene, through='GeneAttributeLink')

    def __str__(self):
        return self.key+":"+self.value


class GeneAttributeLink(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.DO_NOTHING)
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
