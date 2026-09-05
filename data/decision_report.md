# Decision Report

- generated_at: 2026-09-05T16:27:09.649895+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13751**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13751, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.38% | **-1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.80% | **+1.26%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.14% | **+0.96%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.58% | **+0.87%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$848.84** / 初期 $100.00 (+748.84%)
- 確定: 5057件 (Win 1519 / Loss 1651 / Flat 1887) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $848.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.03** / 初期 $100.00 (+89.03%)
- 確定: 2496件 (Win 697 / Loss 588 / Flat 1211) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0435 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ICX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $189.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.12** / 初期 $100.00 (+19.12%)
- 確定: 2375件 (Win 704 / Loss 902 / Flat 769) / pending 6件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000211 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ICX/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.12

## 6. Latest Market Context

- 更新: 2026-09-05T16:26:55.740476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79823.9
- Funnel: target 1050 → liquid 131 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 76.6 >= 65=1, 4h RSI 69.7 >= 65=1, 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +11.54% | $20,461,762.33 |
| 4/USDT:USDT | +10.41% | $23,150,186.33 |
| MARSCOIN/USDT:USDT | +7.56% | $8,760,456.57 |
| BASECAT/USDT:USDT | +6.46% | $1,954,931.90 |
| BULLA/USDT:USDT | +5.87% | $20,089,754.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.50% | +4.42% |
| UNI/USDT:USDT | below_1h_threshold | +4.08% | +4.01% |
| CHIP/USDT:USDT | below_1h_threshold | +3.29% | +3.21% |
| EDGE/USDT:USDT | below_1h_threshold | +3.12% | +3.04% |
| CATI/USDT:USDT | below_1h_threshold | +2.59% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
