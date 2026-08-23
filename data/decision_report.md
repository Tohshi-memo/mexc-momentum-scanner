# Decision Report

- generated_at: 2026-08-23T13:46:30.877218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12455**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12455, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.43% | **+0.23%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.32% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.17%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.82% | **+1.09%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$697.17** / 初期 $100.00 (+597.17%)
- 確定: 4482件 (Win 1369 / Loss 1469 / Flat 1644) / skip 4534件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPL/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $697.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3931件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0024 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.63** / 初期 $100.00 (+16.63%)
- 確定: 1864件 (Win 549 / Loss 707 / Flat 608) / pending 1件 / skip 2065件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000072 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.63

## 6. Latest Market Context

- 更新: 2026-08-23T13:46:20.228408+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=77434.0
- Funnel: target 1018 → liquid 166 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.8 >= 65=1, 4h RSI 79.5 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +48.83% | $68,467,475.54 |
| UAI/USDT:USDT | +28.63% | $5,939,097.14 |
| ZRO/USDT:USDT | +22.93% | $23,958,096.26 |
| STX/USDT:USDT | +22.29% | $13,483,677.20 |
| PENDLE/USDT:USDT | +16.39% | $2,686,579.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.84% | +4.54% |
| ZEN/USDT:USDT | below_1h_threshold | +4.74% | +4.44% |
| AAVE/USDT:USDT | below_1h_threshold | +3.93% | +3.63% |
| LDO/USDT:USDT | below_1h_threshold | +3.73% | +3.43% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.63% | +3.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
