from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer


@api_view(['GET', 'POST'])
def candidate_list(request):

    if request.method == 'GET':
        candidates = Candidate.objects.all()

        # Filtering
        experience = request.query_params.get('years_experience')
        if experience:
            candidates = candidates.filter(years_experience=experience)

        # Ordering
        ordering = request.query_params.get('ordering', '-score')
        allowed_orderings = ['score', '-score', 'applied_at', '-applied_at', 'years_experience']
        if ordering not in allowed_orderings:
            ordering = '-score'
        candidates = candidates.order_by(ordering)

        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def candidate_detail(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def stats(request):
    candidates = Candidate.objects.all()
    total = candidates.count()

    if total == 0:
        return Response({'total': 0, 'avg_score': 0, 'strong': 0})

    scores = [c.score for c in candidates]
    avg_score = round(sum(scores) / total, 1)
    strong = candidates.filter(score__gte=80).count()

    return Response({
        'total': total,
        'avg_score': avg_score,
        'strong': strong,
    })