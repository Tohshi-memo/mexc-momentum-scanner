# Decision Report

- generated_at: 2026-06-09T14:05:39.150713+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6140**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=6140, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.15% | **+1.72%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.92% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.43% | **+0.21%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.07% | **-0.04%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.63** / 初期 $100.00 (+49.63%)
- 確定: 1180件 (Win 296 / Loss 370 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWER/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.63

## 4. Latest Market Context

- 更新: 2026-06-09T14:05:36.581252+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62180.3
- Funnel: target 774 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +44.50% | $23,677,568.48 |
| JCT/USDT:USDT | +31.10% | $1,226,426.83 |
| SLX/USDT:USDT | +28.03% | $5,687,469.74 |
| VELVET/USDT:USDT | +17.97% | $21,246,650.75 |
| IO/USDT:USDT | +17.90% | $1,036,043.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.02% | +2.12% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.63% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.01% | +1.11% |
| ZEST/USDT:USDT | below_1h_threshold | +0.86% | +0.97% |
| BEAT/USDT:USDT | below_1h_threshold | +0.67% | +0.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
