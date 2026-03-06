import { useState } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { DataGrid } from '@mui/x-data-grid';
import StatCard from '../components/StatCard';
import ScoreChip from '../components/ScoreChip';
import { useCandidates, useStats } from '../hooks/useCandidates';

const orderingOptions = [
  { value: '-score',       label: 'Highest Score' },
  { value: 'score',        label: 'Lowest Score' },
  { value: '-applied_at',  label: 'Newest First' },
  { value: 'applied_at',   label: 'Oldest First' },
];

export default function Dashboard() {
  const [ordering, setOrdering] = useState('-score');
  const { candidates, loading } = useCandidates({ ordering });
  const { stats, loading: statsLoading } = useStats();

  const columns = [
    { field: 'name',             headerName: 'Name',       flex: 1 },
    { field: 'email',            headerName: 'Email',      flex: 1 },
    { field: 'years_experience', headerName: 'Experience', width: 120,
      renderCell: (p) => `${p.value} yrs` },
    { field: 'score',            headerName: 'Score',      width: 100 },
    { field: 'score_label',      headerName: 'Rating',     width: 120,
      renderCell: (p) => (
        <ScoreChip label={p.value} score={p.row.score} />
      )
    },
  ];

  return (
    <Box sx={{ p: 3, maxWidth: 1200, mx: 'auto' }}>

      {/* Header */}
      <Typography variant="h4" fontWeight={800} mb={1}>
        Candidate Dashboard
      </Typography>
      <Typography variant="body2" color="text.secondary" mb={3}>
        AI-powered scoring — ranked by best match
      </Typography>

      {/* Stat cards */}
      <Grid container spacing={2} mb={3}>
        <Grid item xs={12} md={4}>
          <StatCard
            title="Total Candidates"
            value={stats?.total ?? '—'}
            subtitle="all time"
            loading={statsLoading}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <StatCard
            title="Average Score"
            value={stats?.avg_score ?? '—'}
            subtitle="out of 100"
            loading={statsLoading}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <StatCard
            title="Strong Matches"
            value={stats?.strong ?? '—'}
            subtitle="score ≥ 80"
            loading={statsLoading}
          />
        </Grid>
      </Grid>

      {/* Filter */}
      <Box sx={{ mb: 2 }}>
        <TextField
          select
          label="Sort by"
          value={ordering}
          onChange={(e) => setOrdering(e.target.value)}
          size="small"
          sx={{ minWidth: 180 }}
        >
          {orderingOptions.map(o => (
            <MenuItem key={o.value} value={o.value}>{o.label}</MenuItem>
          ))}
        </TextField>
      </Box>

      {/* Table */}
      <Box sx={{ height: 500 }}>
        <DataGrid
          rows={candidates}
          columns={columns}
          loading={loading}
          pageSizeOptions={[10, 25, 50]}
          initialState={{ pagination: { paginationModel: { pageSize: 10 } } }}
          disableRowSelectionOnClick
          sx={{
            border: '1px solid #e2e8f0',
            borderRadius: 2,
            '& .MuiDataGrid-columnHeaders': { backgroundColor: '#f8fafc' },
          }}
        />
      </Box>

    </Box>
  );
}