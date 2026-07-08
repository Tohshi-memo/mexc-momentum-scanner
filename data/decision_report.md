# Decision Report

- generated_at: 2026-07-08T18:56:51.333629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8499**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8499, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.69% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.34% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.30% | **+0.12%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$104.62** / 初期 $100.00 (+4.62%)
- 確定トレード: 79件 (TP 29 / SL 49 / EXP 1)
- 最新: TAG/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.23** / 初期 $100.00 (+223.23%)
- 確定: 2689件 (Win 852 / Loss 900 / Flat 937) / skip 2371件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $323.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1268件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0513 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T18:56:42.381222+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=62150.0
- Funnel: target 851 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +49.14% | $1,630,400.62 |
| POWER/USDT:USDT | +17.91% | $3,782,766.05 |
| ALLO/USDT:USDT | +11.02% | $11,242,200.21 |
| VANRY/USDT:USDT | +10.49% | $6,440,023.32 |
| BTW/USDT:USDT | +9.58% | $1,228,209.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.31% | +3.21% |
| BASED/USDT:USDT | below_1h_threshold | +3.24% | +3.14% |
| BEAT/USDT:USDT | below_1h_threshold | +2.84% | +2.73% |
| POWER/USDT:USDT | below_1h_threshold | +2.61% | +2.51% |
| APE/USDT:USDT | below_1h_threshold | +2.37% | +2.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
