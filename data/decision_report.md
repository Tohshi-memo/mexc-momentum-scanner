# Decision Report

- generated_at: 2026-10-28T16:41:38.578692+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=17730, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.06% | **+1.01%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.82% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.34%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,543.68** / 初期 $100.00 (+1443.68%)
- 確定: 6774件 (Win 1970 / Loss 2170 / Flat 2634) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,543.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.53** / 初期 $100.00 (+258.53%)
- 確定: 4251件 (Win 1154 / Loss 969 / Flat 2128) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0634 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $358.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5891件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T16:41:24.085285+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80463.8
- Funnel: target 1083 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +11.90% | $2,166,458.55 |
| BLESS/USDT:USDT | +5.26% | $21,544,583.35 |
| Q/USDT:USDT | +3.74% | $18,785,905.56 |
| AKE/USDT:USDT | +3.56% | $5,610,050.80 |
| AGT/USDT:USDT | +2.55% | $2,339,208.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.57% | +3.65% |
| Q/USDT:USDT | below_1h_threshold | +2.86% | +2.94% |
| AGT/USDT:USDT | below_1h_threshold | +2.55% | +2.63% |
| SNXX/USDT:USDT | below_1h_threshold | +2.03% | +2.11% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.87% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
