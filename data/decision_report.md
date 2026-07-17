# Decision Report

- generated_at: 2026-07-17T14:26:35.499289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8854**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8854, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.87% | **+1.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.31% | **+2.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.02% | **+1.72%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.08% | **+1.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$350.61** / 初期 $100.00 (+250.61%)
- 確定: 2969件 (Win 926 / Loss 947 / Flat 1096) / skip 2446件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.17% 残高後 $350.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.99** / 初期 $100.00 (+8.99%)
- 確定: 816件 (Win 193 / Loss 171 / Flat 452) / skip 1449件
- 成長率目線: 平均log +0.000105 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0522 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $108.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定: 120件 (Win 39 / Loss 71 / Flat 10) / pending 3件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $98.82

## 6. Latest Market Context

- 更新: 2026-07-17T14:26:27.795123+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=63291.8
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +45.17% | $4,561,539.56 |
| XEC/USDT:USDT | +28.70% | $2,165,645.21 |
| AKE/USDT:USDT | +25.03% | $37,706,415.11 |
| KAITO/USDT:USDT | +21.14% | $5,365,086.49 |
| LUMIA/USDT:USDT | +20.69% | $3,057,129.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.66% | +4.40% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.78% | +2.52% |
| US/USDT:USDT | below_1h_threshold | +2.55% | +2.29% |
| UB/USDT:USDT | below_1h_threshold | +2.40% | +2.14% |
| TAC/USDT:USDT | below_1h_threshold | +2.31% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
