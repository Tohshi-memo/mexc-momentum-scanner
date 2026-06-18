# Decision Report

- generated_at: 2026-06-18T15:33:27.471319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7055**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=7055, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/20 | 30.0% | +2.45% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.75% | **+0.61%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.95% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$100.46** / 初期 $100.00 (+0.46%)
- 確定トレード: 14件 (TP 5 / SL 9 / EXP 0)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.71** / 初期 $100.00 (+115.71%)
- 確定: 1882件 (Win 530 / Loss 601 / Flat 751) / skip 1734件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 158件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0668 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T15:33:20.797936+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.95% price=63178.9
- Funnel: target 795 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +109.96% | $15,441,120.15 |
| O/USDT:USDT | +76.05% | $7,973,323.01 |
| RE/USDT:USDT | +45.93% | $8,729,890.65 |
| H/USDT:USDT | +31.46% | $34,487,874.74 |
| HEI/USDT:USDT | +30.98% | $1,144,372.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +2.27% | +3.22% |
| HEI/USDT:USDT | below_1h_threshold | +1.75% | +2.70% |
| MITO/USDT:USDT | below_1h_threshold | +1.11% | +2.06% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +1.89% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +1.63% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
