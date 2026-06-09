# Decision Report

- generated_at: 2026-06-09T15:27:01.792978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6144**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6144, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.65% | **+1.32%** |
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.43% | **+0.21%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.88** / 初期 $100.00 (+48.88%)
- 確定: 1184件 (Win 296 / Loss 371 / Flat 517) / skip 1521件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $148.88

## 4. Latest Market Context

- 更新: 2026-06-09T15:26:58.981027+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=61412.7
- Funnel: target 774 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +36.29% | $24,568,866.78 |
| SLX/USDT:USDT | +34.58% | $6,184,134.08 |
| JCT/USDT:USDT | +30.03% | $1,945,143.19 |
| POWER/USDT:USDT | +27.87% | $4,877,559.81 |
| VELVET/USDT:USDT | +22.98% | $21,433,844.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.00% | +4.16% |
| CHIP/USDT:USDT | below_1h_threshold | +3.84% | +4.00% |
| ALLO/USDT:USDT | below_1h_threshold | +2.36% | +2.52% |
| BEAT/USDT:USDT | below_1h_threshold | +2.28% | +2.44% |
| ATOM/USDT:USDT | below_1h_threshold | +1.83% | +1.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
