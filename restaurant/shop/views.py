from django.shortcuts import render, redirect
from .models import Produs, Categorie, Livrare


def homepage(request):
    if 'cos' not in request.session:
        request.session['cos'] = []

    if 'categorie' in request.GET:
        id_categorie = int(request.GET.get('categorie'))
        categorie_obiect = Categorie.objects.get(id=id_categorie)
        produse = Produs.objects.filter(categorie=categorie_obiect ).all()
    else:
        produse = Produs.objects.all()
    categorii = Categorie.objects.all()

    produse_cos = {}
    for id_produs in request.session['cos']:
        produs = Produs.objects.get(id=id_produs)
        if id_produs not in produse_cos:
            produse_cos[id_produs] = {
                'nume': produs.nume,
                'pret': produs.pret,
                'count': 1
            }
        else:
            produse_cos[id_produs]['count'] += 1

    context = {
        'produse': produse,
        'categorii': categorii,
        'total': sum([obiect_produs['count'] * obiect_produs['pret'] for id_produs, obiect_produs in produse_cos.items()]),
    }
    return render(request, 'home.html', context)


def checkout(request):
    produse_cos = {}
    for id_produs in request.session['cos']:
        produs = Produs.objects.get(id=id_produs)
        if id_produs not in produse_cos:
            produse_cos[id_produs] = {
                'nume': produs.nume,
                'pret': produs.pret,
                'count': 1
            }
        else:
            produse_cos[id_produs]['count'] += 1

    context = {
        'produse': produse_cos,
        'total': sum([obiect_produs['count'] * obiect_produs['pret'] for id_produs, obiect_produs in produse_cos.items()]),
        'nr_produse': sum([obiect_produs['count'] for id_produs, obiect_produs in produse_cos.items()])
    }
    return render(request, 'checkout.html', context)


def adauga_in_cos(request, id_produs):
    produs = Produs.objects.get(id=id_produs)
    request.session['cos'].append(produs.id)

    return redirect('homepage')


def creste_cantitate_cos(request, id_produs):
    if 'cos' in request.session:
        request.session['cos'].append(id_produs)
        request.session.modified = True
    return redirect('checkout')


def scadere_cantitate_cos(request, id_produs):
    if 'cos' in request.session:
        try:
            request.session['cos'].remove(id_produs)
            request.session.modified = True
        except ValueError:
            pass
    return redirect('checkout')


def finalizare_comanda(request):
    if request.method == 'POST':
        adresa = request.POST.get('adresa')
        numar_telefon = request.POST.get('numar_telefon')
        metoda_plata = request.POST.get('metoda_plata')

        produse_cos = [Produs.objects.get(id=id_produs) for id_produs in request.session['cos']]
        livrare = Livrare.objects.create(adresa=adresa, numar_telefon=numar_telefon, metoda_plata=metoda_plata)

        for produs in produse_cos:
            livrare.produse.add(produs)
        request.session['cos'] = []
        request.session.modified = True

    return redirect('homepage')


def comenzile_mele(request):
    comenzi = Livrare.objects.all()
    context = {
        'comenzi': comenzi
    }

    Livrare.objects.all().delete()

    return render(request, 'comenzi.html', context)