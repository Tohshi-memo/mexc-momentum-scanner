# Decision Report

- generated_at: 2026-08-04T20:16:26.861799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10318**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10318, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.38% | **+0.21%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.26% | **+0.19%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.32% | **+0.18%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.20% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.81%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.68% | **+0.67%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.66% | **+0.66%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3153件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2444件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0219 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.80** / 初期 $100.00 (+16.80%)
- 確定: 1075件 (Win 345 / Loss 416 / Flat 314) / pending 5件 / skip 711件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000340 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AAOISTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $116.80

## 6. Latest Market Context

- 更新: 2026-08-04T20:16:19.133234+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64085.7
- Funnel: target 937 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +29.17% | $2,083,440.38 |
| BICO/USDT:USDT | +14.80% | $13,952,228.64 |
| HFT/USDT:USDT | +11.68% | $1,239,606.59 |
| PUMPFUN/USDT:USDT | +9.34% | $40,641,842.63 |
| ALABSTOCK/USDT:USDT | +8.29% | $2,215,032.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +3.07% | +3.24% |
| HFT/USDT:USDT | below_1h_threshold | +2.85% | +3.03% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.83% | +3.00% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.33% | +1.50% |
| LAB/USDT:USDT | below_1h_threshold | +0.95% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
