# Decision Report

- generated_at: 2026-11-05T16:26:36.920490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18186**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.70% / filled 20/20。**
- 全期間 MARKET基準: n=18186, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.70% | **+2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.70% | **+2.70%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.67% | **+0.34%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.41% | **+0.12%** |
| MARKET_LONG | 20/20 | 100.0% | -0.73% | **-0.73%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,505.05** / 初期 $100.00 (+1405.05%)
- 確定: 7005件 (Win 2021 / Loss 2243 / Flat 2741) / skip 7742件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,505.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.58** / 初期 $100.00 (+273.58%)
- 確定: 4578件 (Win 1229 / Loss 1030 / Flat 2319) / skip 7019件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $373.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6351件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000444 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T16:26:21.056408+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.14% price=76880.4
- Funnel: target 1084 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNXX/USDT:USDT | +15.36% | $54,045,221.96 |
| MUU/USDT:USDT | +13.75% | $33,817,573.30 |
| SOXL/USDT:USDT | +12.61% | $1,159,113,055.99 |
| ARIA/USDT:USDT | +9.36% | $3,158,249.84 |
| INTW/USDT:USDT | +8.58% | $2,669,533.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_relative_strength | +5.08% | +3.94% |
| Q/USDT:USDT | below_1h_threshold | +4.38% | +3.24% |
| LYN/USDT:USDT | below_1h_threshold | +4.24% | +3.10% |
| AIO/USDT:USDT | below_1h_threshold | +4.09% | +2.95% |
| PONS/USDT:USDT | below_1h_threshold | +3.89% | +2.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
