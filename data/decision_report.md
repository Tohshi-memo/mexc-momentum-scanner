# Decision Report

- generated_at: 2026-05-14T06:58:37.735924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4275**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=4275, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.36% | **+1.36%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.47% | **+1.32%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.41% | **+1.12%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.55% | **+1.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.07% | **+4.07%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.39% | **+1.07%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.15% | **+0.97%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 492件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T06:58:31.599602+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79760.2
- Funnel: target 766 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +25.24% | $2,005,737.68 |
| GIGA/USDT:USDT | +21.89% | $1,141,041.05 |
| UP/USDT:USDT | +20.28% | $5,290,586.08 |
| CSCOSTOCK/USDT:USDT | +19.96% | $5,125,278.52 |
| IRYS/USDT:USDT | +16.05% | $5,464,758.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.07% | +4.08% |
| AIN/USDT:USDT | below_1h_threshold | +3.51% | +3.52% |
| USELESS/USDT:USDT | below_1h_threshold | +1.68% | +1.69% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.16% | +1.17% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.15% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
