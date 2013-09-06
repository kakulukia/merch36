# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price'
        db.add_column(u'products_product', 'price',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['products.Price']),
                      keep_default=False)

        # Adding field 'Product.employee_price'
        db.add_column(u'products_product', 'employee_price',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='employee_products', to=orm['products.Price']),
                      keep_default=False)


        # Changing field 'Sale.size'
        db.alter_column(u'products_sale', 'size_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Size']))

        # Changing field 'Sale.color'
        db.alter_column(u'products_sale', 'color_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Color']))

        # Changing field 'Sale.price'
        db.alter_column(u'products_sale', 'price_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Price']))

        # Changing field 'Sale.sex'
        db.alter_column(u'products_sale', 'sex_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Sex']))

        # Changing field 'Delivery.color'
        db.alter_column(u'products_delivery', 'color_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Color']))

        # Changing field 'Delivery.sex'
        db.alter_column(u'products_delivery', 'sex_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Sex']))

        # Changing field 'Delivery.size'
        db.alter_column(u'products_delivery', 'size_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['products.Size']))

    def backwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column(u'products_product', 'price_id')

        # Deleting field 'Product.employee_price'
        db.delete_column(u'products_product', 'employee_price_id')


        # Changing field 'Sale.size'
        db.alter_column(u'products_sale', 'size_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Size']))

        # Changing field 'Sale.color'
        db.alter_column(u'products_sale', 'color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Color']))

        # Changing field 'Sale.price'
        db.alter_column(u'products_sale', 'price_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Price']))

        # Changing field 'Sale.sex'
        db.alter_column(u'products_sale', 'sex_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Sex']))

        # Changing field 'Delivery.color'
        db.alter_column(u'products_delivery', 'color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Color']))

        # Changing field 'Delivery.sex'
        db.alter_column(u'products_delivery', 'sex_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Sex']))

        # Changing field 'Delivery.size'
        db.alter_column(u'products_delivery', 'size_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Size']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.color': {
            'Meta': {'object_name': 'Color'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'products.delivery': {
            'Meta': {'ordering': "['-delivery_date']", 'object_name': 'Delivery'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Color']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Imprint']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'sex': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Sex']"}),
            'size': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Size']"})
        },
        u'products.imprint': {
            'Meta': {'object_name': 'Imprint'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'products.price': {
            'Meta': {'ordering': "['price']", 'object_name': 'Price'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Color']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'employee_price': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employee_products'", 'to': u"orm['products.Price']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Price']"}),
            'sexes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Sex']", 'symmetrical': 'False'}),
            'sizes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Size']", 'symmetrical': 'False'})
        },
        u'products.sale': {
            'Meta': {'ordering': "['-purchase_date']", 'object_name': 'Sale'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Color']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employee_discount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Imprint']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Price']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'sex': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Sex']"}),
            'size': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['products.Size']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'products.sex': {
            'Meta': {'object_name': 'Sex'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'products.size': {
            'Meta': {'ordering': "['value']", 'object_name': 'Size'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['products']