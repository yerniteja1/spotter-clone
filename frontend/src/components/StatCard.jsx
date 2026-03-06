import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Skeleton from '@mui/material/Skeleton';

export default function StatCard({ title, value, subtitle, loading }) {
  return (
    <Card elevation={0} sx={{ border: '1px solid #e2e8f0', borderRadius: 2 }}>
      <CardContent>
        <Typography variant="overline" color="text.secondary">
          {title}
        </Typography>
        {loading ? (
          <Skeleton width={80} height={48} />
        ) : (
          <Typography variant="h3" fontWeight={800} color="text.primary">
            {value}
          </Typography>
        )}
        <Typography variant="body2" color="text.secondary">
          {subtitle}
        </Typography>
      </CardContent>
    </Card>
  );
}