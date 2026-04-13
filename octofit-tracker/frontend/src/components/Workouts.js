import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Workouts API endpoint:', API_URL);
        console.log('Fetched workouts:', results);
        setWorkouts(results);
      });
  }, []);

  return (
    <div>
      <h2 className="mb-4">Workouts</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered align-middle">
          <thead className="table-light">
            <tr>
              <th>User</th>
              <th>Workout</th>
              <th>Reps</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, i) => (
              <tr key={i}>
                <td>{workout.user}</td>
                <td>{workout.workout}</td>
                <td>{workout.reps}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
