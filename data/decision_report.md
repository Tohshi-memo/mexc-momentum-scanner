# Decision Report

- generated_at: 2026-06-16T14:29:39.123443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6868**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=6868, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.52% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.87% | **+3.89%** |
| ASK_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.04% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.98** / 初期 $100.00 (+84.98%)
- 確定: 1741件 (Win 457 / Loss 545 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUFFER/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $184.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 123件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score +0.0167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T14:29:34.593197+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=65609.3
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +48.81% | $4,374,225.63 |
| BSB/USDT:USDT | +45.01% | $35,437,283.23 |
| PORTAL/USDT:USDT | +35.97% | $3,722,020.58 |
| LAB/USDT:USDT | +27.33% | $17,442,374.67 |
| ASTEROID/USDT:USDT | +24.74% | $3,929,860.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +2.00% | +2.62% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.34% | +1.95% |
| STG/USDT:USDT | below_1h_threshold | +1.09% | +1.70% |
| VELVET/USDT:USDT | below_1h_threshold | +0.85% | +1.47% |
| RUNE/USDT:USDT | below_1h_threshold | +0.84% | +1.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
