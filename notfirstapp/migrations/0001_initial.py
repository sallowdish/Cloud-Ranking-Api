# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'notfirstapp_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=1, blank=1)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50, null=1, blank=1)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'notfirstapp', ['Account'])

        # Adding model 'Game'
        db.create_table(u'notfirstapp_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gamename', self.gf('django.db.models.fields.CharField')(default='Game', max_length=100)),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=1, blank=True)),
            ('fk_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Image'], null=True)),
        ))
        db.send_create_signal(u'notfirstapp', ['Game'])

        # Adding model 'Figure'
        db.create_table(u'notfirstapp_figure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Player', max_length=50)),
            ('tag', self.gf('django.db.models.fields.CharField')(default='Player#0000', max_length=50)),
            ('User_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'notfirstapp', ['Figure'])

        # Adding model 'Play'
        db.create_table(u'notfirstapp_play', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Game'])),
            ('Figure_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Figure'])),
        ))
        db.send_create_signal(u'notfirstapp', ['Play'])

        # Adding model 'Own'
        db.create_table(u'notfirstapp_own', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Game'])),
            ('User_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'notfirstapp', ['Own'])

        # Adding model 'ScoreRank'
        db.create_table(u'notfirstapp_scorerank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Figure_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Figure'])),
            ('Game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Game'])),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('achieveTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=1, blank=True)),
        ))
        db.send_create_signal(u'notfirstapp', ['ScoreRank'])

        # Adding model 'TimeRank'
        db.create_table(u'notfirstapp_timerank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Figure_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Figure'])),
            ('Game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notfirstapp.Game'])),
            ('finishTime', self.gf('django.db.models.fields.TimeField')()),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('achieveTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=1, blank=True)),
        ))
        db.send_create_signal(u'notfirstapp', ['TimeRank'])

        # Adding model 'Image'
        db.create_table(u'notfirstapp_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagefile', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'notfirstapp', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'notfirstapp_account')

        # Deleting model 'Game'
        db.delete_table(u'notfirstapp_game')

        # Deleting model 'Figure'
        db.delete_table(u'notfirstapp_figure')

        # Deleting model 'Play'
        db.delete_table(u'notfirstapp_play')

        # Deleting model 'Own'
        db.delete_table(u'notfirstapp_own')

        # Deleting model 'ScoreRank'
        db.delete_table(u'notfirstapp_scorerank')

        # Deleting model 'TimeRank'
        db.delete_table(u'notfirstapp_timerank')

        # Deleting model 'Image'
        db.delete_table(u'notfirstapp_image')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'notfirstapp.account': {
            'Meta': {'object_name': 'Account'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': '1', 'blank': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': '1', 'blank': '1'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'notfirstapp.figure': {
            'Meta': {'object_name': 'Figure'},
            'User_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Player'", 'max_length': '50'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "'Player#0000'", 'max_length': '50'})
        },
        u'notfirstapp.game': {
            'Meta': {'object_name': 'Game'},
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': '1', 'blank': 'True'}),
            'fk_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Image']", 'null': 'True'}),
            'gamename': ('django.db.models.fields.CharField', [], {'default': "'Game'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'notfirstapp.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagefile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'notfirstapp.own': {
            'Game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Game']"}),
            'Meta': {'object_name': 'Own'},
            'User_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'notfirstapp.play': {
            'Figure_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Figure']"}),
            'Game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Game']"}),
            'Meta': {'object_name': 'Play'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'notfirstapp.scorerank': {
            'Figure_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Figure']"}),
            'Game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Game']"}),
            'Meta': {'object_name': 'ScoreRank'},
            'achieveTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'notfirstapp.timerank': {
            'Figure_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Figure']"}),
            'Game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notfirstapp.Game']"}),
            'Meta': {'object_name': 'TimeRank'},
            'achieveTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': '1', 'blank': 'True'}),
            'finishTime': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['notfirstapp']