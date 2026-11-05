# Decision Report

- generated_at: 2026-11-05T07:21:29.494086+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18167**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=18167, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,506.99** / 初期 $100.00 (+1406.99%)
- 確定: 6986件 (Win 2019 / Loss 2242 / Flat 2725) / skip 7742件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,506.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.01** / 初期 $100.00 (+272.01%)
- 確定: 4560件 (Win 1223 / Loss 1030 / Flat 2307) / skip 7018件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0796 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $372.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6326件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000205 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T07:21:18.455145+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80593.5
- Funnel: target 1077 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +34.28% | $6,129,659.36 |
| ELSA/USDT:USDT | +26.14% | $4,050,225.38 |
| APPSTOCK/USDT:USDT | +20.60% | $1,517,142.89 |
| AIN/USDT:USDT | +17.80% | $3,244,955.68 |
| FLUID/USDT:USDT | +16.00% | $5,382,922.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +2.70% | +2.74% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.76% |
| ICNT/USDT:USDT | below_1h_threshold | +1.48% | +1.52% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.29% |
| BEAMX/USDT:USDT | below_1h_threshold | +1.16% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
