# Decision Report

- generated_at: 2026-10-17T02:56:27.424755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16846**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16846, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +2.24% | **+0.79%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |
| LIMIT_BB3S | 9/15 | 60.0% | +0.81% | **+0.49%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.67% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.91% | **+1.43%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.57% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.28** / 初期 $100.00 (+1165.28%)
- 確定: 6322件 (Win 1851 / Loss 2028 / Flat 2443) / skip 7085件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,265.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3689件 (Win 1027 / Loss 878 / Flat 1784) / skip 6568件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0992 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5006件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000266 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T02:56:12.854877+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81452.4
- Funnel: target 1084 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +93.33% | $15,977,759.89 |
| ICNT/USDT:USDT | +24.13% | $3,615,401.02 |
| SIREN/USDT:USDT | +18.47% | $1,161,373.17 |
| FOLKS/USDT:USDT | +10.15% | $1,291,029.14 |
| UVXY/USDT:USDT | +9.98% | $2,827,032.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +4.26% | +4.33% |
| ICNT/USDT:USDT | below_1h_threshold | +2.86% | +2.94% |
| WLD/USDT:USDT | below_1h_threshold | +2.11% | +2.19% |
| TIA/USDT:USDT | below_1h_threshold | +1.97% | +2.04% |
| TMX/USDT:USDT | below_1h_threshold | +1.64% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
