# Decision Report

- generated_at: 2026-09-11T17:36:25.630225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14240**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=14240, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_BB3S | 2/15 | 13.3% | +3.28% | **+0.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.37% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.97% | **+2.38%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.37% | **+1.03%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.84% | **+0.42%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 210件 (TP 78 / SL 127 / EXP 5)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,090.73** / 初期 $100.00 (+990.73%)
- 確定: 5398件 (Win 1627 / Loss 1747 / Flat 2024) / skip 5403件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MINA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.71% 残高後 $1,090.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.22** / 初期 $100.00 (+109.22%)
- 確定: 2816件 (Win 774 / Loss 655 / Flat 1387) / skip 4835件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $209.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.70** / 初期 $100.00 (+23.70%)
- 確定: 2733件 (Win 809 / Loss 1047 / Flat 877) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.70

## 6. Latest Market Context

- 更新: 2026-09-11T17:36:15.070810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=77734.1
- Funnel: target 1067 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +11.27% | $6,287,375.03 |
| LAB/USDT:USDT | +7.12% | $4,373,897.72 |
| STONK/USDT:USDT | +3.54% | $1,381,787.71 |
| HNT/USDT:USDT | +3.12% | $1,865,935.10 |
| AERO/USDT:USDT | +2.58% | $1,420,764.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.39% | +2.58% |
| WLFI/USDT:USDT | below_1h_threshold | +2.03% | +2.22% |
| USELESS/USDT:USDT | below_1h_threshold | +2.01% | +2.20% |
| HNT/USDT:USDT | below_1h_threshold | +1.82% | +2.00% |
| STONK/USDT:USDT | below_1h_threshold | +1.46% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
