# Decision Report

- generated_at: 2026-10-02T01:56:29.877484+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15959**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.27% / filled 20/20。**
- 全期間 MARKET基準: n=15959, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.27% | **+3.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.27% | **+3.27%** |
| LIMIT_1PCT | 18/20 | 90.0% | +3.41% | **+3.07%** |
| LIMIT_2PCT | 16/20 | 80.0% | +3.27% | **+2.62%** |
| LIMIT_ATR | 8/20 | 40.0% | +3.65% | **+1.46%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.20% | **-0.12%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -1.13% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.12** / 初期 $100.00 (+1210.12%)
- 確定: 6064件 (Win 1797 / Loss 1955 / Flat 2312) / skip 6456件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.15% 残高後 $1,310.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3604件 (Win 1005 / Loss 844 / Flat 1755) / skip 5766件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0557 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T01:56:18.558564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=84861.9
- Funnel: target 1097 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +65.45% | $3,349,140.43 |
| UAI/USDT:USDT | +11.05% | $2,500,308.30 |
| MAGMA/USDT:USDT | +8.41% | $1,568,917.81 |
| ZRO/USDT:USDT | +7.75% | $10,639,060.29 |
| MUU/USDT:USDT | +7.47% | $14,881,828.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAVE/USDT:USDT | below_1h_threshold | +1.88% | +1.75% |
| STRK/USDT:USDT | below_1h_threshold | +1.63% | +1.50% |
| JTO/USDT:USDT | below_1h_threshold | +1.40% | +1.27% |
| AKE/USDT:USDT | below_1h_threshold | +1.22% | +1.09% |
| FET/USDT:USDT | below_1h_threshold | +1.21% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
