# Decision Report

- generated_at: 2026-07-25T16:36:24.037942+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9532**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9532, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +1.30% | **+0.31%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.19% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.84% | **+2.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.30% | **+1.95%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.79% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$445.74** / 初期 $100.00 (+345.74%)
- 確定: 3360件 (Win 1064 / Loss 1089 / Flat 1207) / skip 2733件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $445.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$135.54** / 初期 $100.00 (+35.54%)
- 確定: 1185件 (Win 324 / Loss 259 / Flat 602) / skip 1758件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1437 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $135.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.58** / 初期 $100.00 (+7.58%)
- 確定: 578件 (Win 195 / Loss 222 / Flat 161) / pending 5件 / skip 422件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000518 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.58

## 6. Latest Market Context

- 更新: 2026-07-25T16:36:14.594671+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64155.7
- Funnel: target 898 → liquid 139 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +14.72% | $88,905,647.40 |
| DEXE/USDT:USDT | +11.11% | $134,729,877.05 |
| ESPORTS/USDT:USDT | +8.63% | $22,377,259.82 |
| SYN/USDT:USDT | +4.52% | $4,082,092.24 |
| ZAMA/USDT:USDT | +3.12% | $6,552,010.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.63% | +4.63% |
| ZAMA/USDT:USDT | below_1h_threshold | +3.26% | +3.26% |
| EUL/USDT:USDT | below_1h_threshold | +3.10% | +3.09% |
| BASED/USDT:USDT | below_1h_threshold | +2.73% | +2.72% |
| RIF/USDT:USDT | below_1h_threshold | +2.13% | +2.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
