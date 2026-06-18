# Decision Report

- generated_at: 2026-06-18T06:11:39.295598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7013**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=7013, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$212.96** / 初期 $100.00 (+112.96%)
- 確定: 1859件 (Win 519 / Loss 589 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $212.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.35** / 初期 $100.00 (+5.35%)
- 確定: 286件 (Win 80 / Loss 76 / Flat 130) / skip 138件
- 成長率目線: 平均log +0.000182 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0562 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.35

## 5. Latest Market Context

- 更新: 2026-06-18T06:11:34.172543+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63898.7
- Funnel: target 793 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +94.85% | $37,210,757.28 |
| SYN/USDT:USDT | +64.56% | $4,943,686.41 |
| O/USDT:USDT | +44.96% | $2,433,871.07 |
| H/USDT:USDT | +31.98% | $31,557,025.41 |
| HOME/USDT:USDT | +28.58% | $1,960,413.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.64% | +3.75% |
| AGT/USDT:USDT | below_1h_threshold | +3.43% | +3.53% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.87% | +2.97% |
| PLAY/USDT:USDT | below_1h_threshold | +2.56% | +2.66% |
| H/USDT:USDT | below_1h_threshold | +2.19% | +2.29% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
