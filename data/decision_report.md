# Decision Report

- generated_at: 2026-10-08T18:46:56.964016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16357, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.54% | **+0.35%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.31% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.16% | **+1.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +6.02% | **+0.90%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.91% | **+0.86%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.21% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6280件 (Win 1845 / Loss 2012 / Flat 2423) / skip 6638件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OGN/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3633件 (Win 1010 / Loss 853 / Flat 1770) / skip 6135件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0060 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PYTH/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4527件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T18:46:34.641854+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.92% price=81449.9
- Funnel: target 1083 → liquid 186 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=42, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +30.20% | $15,290,948.48 |
| OGN/USDT:USDT | +28.93% | $9,019,139.19 |
| BATON/USDT:USDT | +20.69% | $1,551,284.81 |
| SI/USDT:USDT | +17.09% | $1,392,922.56 |
| LONGXIA/USDT:USDT | +15.14% | $3,926,218.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BOME/USDT:USDT | below_relative_strength | +5.69% | +4.78% |
| PYTH/USDT:USDT | below_relative_strength | +5.67% | +4.75% |
| MOVR/USDT:USDT | below_relative_strength | +5.55% | +4.64% |
| APT/USDT:USDT | below_1h_threshold | +4.62% | +3.70% |
| SYN/USDT:USDT | below_1h_threshold | +4.45% | +3.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
