# Decision Report

- generated_at: 2026-10-18T00:26:23.547133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16925**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=16925, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.66% | **+0.73%** |
| LIMIT_BB3S | 6/16 | 37.5% | +1.43% | **+0.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.59% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.21% | **+4.66%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.24% | **+0.99%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.09% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,301.78** / 初期 $100.00 (+1201.78%)
- 確定: 6391件 (Win 1863 / Loss 2044 / Flat 2484) / skip 7095件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BAT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account -0.01% 残高後 $1,301.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6646件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0333 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5083件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000267 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T00:26:09.051405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=81455.7
- Funnel: target 1084 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +24.11% | $1,674,319.26 |
| BR/USDT:USDT | +21.50% | $10,266,481.64 |
| Q/USDT:USDT | +18.93% | $6,898,969.10 |
| AVA/USDT:USDT | +18.17% | $2,101,725.22 |
| AGT/USDT:USDT | +16.71% | $16,778,816.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.75% | +2.75% |
| BR/USDT:USDT | below_1h_threshold | +1.27% | +1.27% |
| XMR/USDT:USDT | below_1h_threshold | +0.94% | +0.94% |
| STX/USDT:USDT | below_1h_threshold | +0.57% | +0.57% |
| AGT/USDT:USDT | below_1h_threshold | +0.53% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
