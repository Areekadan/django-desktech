import random 
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class ProductPublishedManager(models.Manager):
    def get_queryset(self):
        return(
            super(ProductPublishedManager, self)
            .get_queryset()
            .filter(published_status=True)
        )
class Product(TimeStampedUUIDModel):
    class ProductType(models.TextChoices):
        DESKPAD = "Deskpad", _("Deskpad")
        HEADSET_HANGER = "Headset Holder", _("Headset Holder")
        LIGHTING = "Lighting", _("Lighting")
        DECORATIONS = "Decorations", _("Decorations")
        PLANTS = "Desk Plant", _("Desk Plant")
        OTHER = "Other", _("Other")
    user = models.ForeignKey(
        User, 
        verbose_name= _("Agent, Seller or Buyer"), 
        related_name="agent_buyer", 
        on_delete=models.DO_NOTHING)
    title = models.CharField(
        verbose_name=_("Product Title"),
        max_length = 250)
    slug = AutoSlugField(
        populate_from="title", 
        unique=True,
        always_update=True)
    ref_code = models.CharField(
        verbose_name=_("Product Reference Code"),
        max_length=255,
        unique=True,
        blank=True)
    description = models.TextField(
        verbose_name=_("Description"),
        default="No Description Entered.")
    price = models.DecimalField(
        verbose_name=_("Price"), 
        max_digits = 8,
        decimal_places=2,
        default=0.0)
    tax = models.DecimalField(verbose_name=_("Tax"), 
        max_digits=8,
        decimal_places=2,
        default=0.05,
        help_text="Defaults to Canada, Alberta GST charge")
    product_type = models.CharField(
        verbose_name=_("Product Type"),
        max_length=50,
        choices=ProductType.choices,
        default=ProductType.OTHER)
    cover_photo = models.ImageField(verbose_name=_("Primary Photo"),
        default="/mediafiles/defaultNoImage.jpg",
        null=True,
        blank=True)
    photo1 = models.ImageField(
        default="/mediafiles/defaultNoImage.jpg",
        null=True,
        blank=True)
    photo2 = models.ImageField(
        default="/mediafiles/defaultNoImage.jpg",
        null=True,
        blank=True)
    photo3 = models.ImageField(
        default="/mediafiles/defaultNoImage.jpg",
        null=True,
        blank=True)
    photo4 = models.ImageField(
        default="/mediafiles/defaultNoImage.jpg",
        null=True,
        blank=True)
    published_status = models.BooleanField(
        verbose_name=_("Published Status"),
        default=False)
    views = models.IntegerField(verbose_name=_("Total Views"), default = 0)
    objects = models.Manager()
    published = ProductPublishedManager()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name= "Product"
        verbose_name_plural = "Products"
    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.description(self.description)
        self.ref_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(Product, self).save(*args, **kwargs)

    @property
    def final_product_price(self):
        tax_percentage = self.tax
        product_price = self.price
        tax_amount = round(tax_percentage * product_price, 2)
        price_after_tax= float(round(product_price + tax_amount, 2))
        return price_after_tax
class ProductViews(TimeStampedUUIDModel):
    ip = models.CharField(
        verbose_name=_("IP Address"),
        max_length=250,)
    product = models.ForeignKey(
        Product, 
        related_name="product_views", 
        on_delete = models.CASCADE)
    def __str__(self):
        return (f"Total views on - {self.product.title} is - {self.product.views} view(s)")
    class Meta:
        verbose_name = "Total Views on Product"
        verbose_name_plural = "Total Product Views"
        