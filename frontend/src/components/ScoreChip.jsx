import Chip from '@mui/material/Chip';

export default function ScoreChip({ label, score }) {
  const color =
    score >= 80 ? 'success' :
    score >= 60 ? 'warning' :
    score >= 40 ? 'default' : 'error';

  return (
    <Chip
      label={label}
      color={color}
      size="small"
      sx={{ fontWeight: 700, minWidth: 70 }}
    />
  );
}