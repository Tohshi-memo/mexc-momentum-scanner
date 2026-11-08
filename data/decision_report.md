# Decision Report

- generated_at: 2026-11-08T05:41:20.172267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18405**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=18405, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +1.79% | **+0.90%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.33% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.31% | **+0.59%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.93% | **+2.35%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.83% | **+1.84%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.79% | **+1.61%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.71% | **+1.46%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.00% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,538.84** / 初期 $100.00 (+1438.84%)
- 確定: 7101件 (Win 2042 / Loss 2269 / Flat 2790) / skip 7865件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $1,538.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7061件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0873 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6565件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000380 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T05:41:07.698151+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=75811.0
- Funnel: target 1089 → liquid 106 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +155.82% | $7,908,604.08 |
| MET/USDT:USDT | +5.05% | $1,606,344.80 |
| BTW/USDT:USDT | +4.65% | $6,383,712.53 |
| LIT/USDT:USDT | +3.25% | $11,042,176.47 |
| USELESS/USDT:USDT | +2.96% | $2,097,188.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MET/USDT:USDT | below_1h_threshold | +1.22% | +1.24% |
| NEAR/USDT:USDT | below_1h_threshold | +0.79% | +0.82% |
| LIT/USDT:USDT | below_1h_threshold | +0.55% | +0.58% |
| PEPE/USDT:USDT | below_1h_threshold | +0.52% | +0.54% |
| LDO/USDT:USDT | below_1h_threshold | +0.46% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
