# Decision Report

- generated_at: 2026-06-19T06:03:27.794296+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7105**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=7105, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.81% | **+0.60%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.49% | **+0.25%** |
| LIMIT_ATR | 7/20 | 35.0% | +0.38% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.97% | **+0.60%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.43** / 初期 $100.00 (+119.43%)
- 確定: 1925件 (Win 549 / Loss 621 / Flat 755) / skip 1741件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $219.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 207件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0457 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T06:03:23.458292+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62740.2
- Funnel: target 795 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +88.28% | $7,181,653.63 |
| ZEREBRO/USDT:USDT | +20.30% | $3,698,829.44 |
| HEI/USDT:USDT | +19.35% | $1,605,731.49 |
| BTW/USDT:USDT | +16.92% | $3,184,255.22 |
| BASED/USDT:USDT | +16.59% | $6,003,767.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.05% | +3.00% |
| BEAT/USDT:USDT | below_1h_threshold | +2.13% | +2.07% |
| BASED/USDT:USDT | below_1h_threshold | +1.21% | +1.16% |
| PLAY/USDT:USDT | below_1h_threshold | +0.87% | +0.81% |
| ALLO/USDT:USDT | below_1h_threshold | +0.71% | +0.66% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
