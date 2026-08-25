# Decision Report

- generated_at: 2026-08-25T02:46:38.420389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12568**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12568, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.30% | **+0.81%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.53% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.82% | **+1.69%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.05% | **+1.33%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.73% | **+1.23%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.82% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$691.84** / 初期 $100.00 (+591.84%)
- 確定: 4548件 (Win 1385 / Loss 1491 / Flat 1672) / skip 4581件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $691.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.05** / 初期 $100.00 (+56.05%)
- 確定: 1975件 (Win 536 / Loss 472 / Flat 967) / skip 4004件
- 成長率目線: 平均log +0.000225 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $156.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2128件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T02:46:22.786707+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.24% price=80788.9
- Funnel: target 1022 → liquid 179 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 74.8 >= 65=1, 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +78.50% | $4,123,446.78 |
| TAC/USDT:USDT | +43.51% | $2,127,470.41 |
| PONS/USDT:USDT | +19.24% | $1,605,089.77 |
| CASHCAT/USDT:USDT | +18.50% | $2,698,202.52 |
| STORJ/USDT:USDT | +17.17% | $5,130,871.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_relative_strength | +5.95% | +4.71% |
| BR/USDT:USDT | below_1h_threshold | +4.35% | +3.11% |
| 1000BONK/USDT:USDT | below_1h_threshold | +4.12% | +2.88% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.20% | +1.96% |
| ZEC/USDT:USDT | below_1h_threshold | +3.13% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
