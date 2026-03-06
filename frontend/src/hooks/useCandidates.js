import { useState, useEffect } from 'react';
import { candidateApi } from '../api/candidates';

export function useCandidates(filters = {}) {
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading]       = useState(true);
  const [error, setError]           = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    candidateApi.list(filters)
      .then(res => setCandidates(res.data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));

  }, [JSON.stringify(filters)]);

  return { candidates, loading, error };
}

export function useStats() {
  const [stats, setStats]   = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    candidateApi.stats()
      .then(res => setStats(res.data))
      .finally(() => setLoading(false));
  }, []);

  return { stats, loading };
}