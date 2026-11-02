# Decision Report

- generated_at: 2026-11-02T05:31:34.599412+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18010**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=18010, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.78% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_BB3S | 3/20 | 15.0% | +3.54% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.41** / 初期 $100.00 (+1426.41%)
- 確定: 6862件 (Win 1990 / Loss 2203 / Flat 2669) / skip 7709件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,526.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$382.62** / 初期 $100.00 (+282.62%)
- 確定: 4450件 (Win 1193 / Loss 987 / Flat 2270) / skip 6971件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0866 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $382.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6172件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T05:31:16.891597+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78339.4
- Funnel: target 1088 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +32.31% | $1,888,353.42 |
| IDOL/USDT:USDT | +22.27% | $14,502,391.63 |
| RT/USDT:USDT | +19.10% | $1,608,123.70 |
| EVAA/USDT:USDT | +12.33% | $6,661,348.16 |
| KORU/USDT:USDT | +11.10% | $27,588,143.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.61% | +3.66% |
| IDOL/USDT:USDT | below_1h_threshold | +1.99% | +2.04% |
| RT/USDT:USDT | below_1h_threshold | +1.76% | +1.81% |
| KORU/USDT:USDT | below_1h_threshold | +1.02% | +1.07% |
| GRASS/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
