# Decision Report

- generated_at: 2026-10-17T04:16:29.563871+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16849**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16849, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_5PCT | 14/20 | 70.0% | +1.05% | **+0.73%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.71% | **+2.03%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.46% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,269.72** / 初期 $100.00 (+1169.72%)
- 確定: 6325件 (Win 1852 / Loss 2028 / Flat 2445) / skip 7085件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.35% 残高後 $1,269.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3689件 (Win 1027 / Loss 878 / Flat 1784) / skip 6571件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1055 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5012件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T04:16:15.124537+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81507.1
- Funnel: target 1084 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +129.90% | $16,473,936.28 |
| ICNT/USDT:USDT | +29.19% | $3,832,057.72 |
| SIREN/USDT:USDT | +20.34% | $1,098,979.93 |
| FOLKS/USDT:USDT | +14.56% | $1,330,369.53 |
| UVXY/USDT:USDT | +10.28% | $2,951,701.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.24% | +4.27% |
| DNA/USDT:USDT | below_1h_threshold | +3.70% | +3.73% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.37% | +2.40% |
| TIA/USDT:USDT | below_1h_threshold | +0.67% | +0.70% |
| XMR/USDT:USDT | below_1h_threshold | +0.58% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
