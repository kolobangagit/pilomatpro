from store.models import YandexMetrica

def yandex_counter_id(request):
    metrica = YandexMetrica.objects.all()
    if metrica:
        # return {'counter_id': metrica[0]}
        return {'counter_id': metrica[0].counter_id,
                'clickmap': metrica[0].clickmap,
                'accurateTrackBounce': metrica[0].accurateTrackBounce,
                'trackLinks': metrica[0].trackLinks
                }
    else:
        return {'counter_id': 2345678978,
                'clickmap': True,
                'accurateTrackBounce': True,
                'trackLinks': True
                }