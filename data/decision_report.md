# Decision Report

- generated_at: 2026-11-12T16:11:29.358070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18747**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=18747, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.90% | **+1.24%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,706.89** / 初期 $100.00 (+1606.89%)
- 確定: 7235件 (Win 2083 / Loss 2317 / Flat 2835) / skip 8073件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,706.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.99** / 初期 $100.00 (+289.99%)
- 確定: 4780件 (Win 1283 / Loss 1058 / Flat 2439) / skip 7378件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0019 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KGEN/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $389.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6907件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000399 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-12T16:11:16.021581+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=72095.4
- Funnel: target 1105 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +7.01% | $6,351,746.58 |
| CRWVSTOCK/USDT:USDT | +2.10% | $3,803,028.71 |
| DELTAELECSTOCK/USDT:USDT | +2.10% | $1,396,771.44 |
| Q/USDT:USDT | +1.95% | $5,026,558.88 |
| AXTISTOCK/USDT:USDT | +1.86% | $1,177,808.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVDL/USDT:USDT | below_1h_threshold | +3.81% | +3.24% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +3.81% | +3.23% |
| MVLL/USDT:USDT | below_1h_threshold | +3.46% | +2.88% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +3.33% | +2.75% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.97% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
