# Decision Report

- generated_at: 2026-05-07T03:17:36.444162+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3544**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3544, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.32% | **+2.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.61% | **+1.44%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.25** / 初期 $100.00 (+2.25%)
- 確定: 39件 (Win 12 / Loss 15 / Flat 12) / skip 66件
- 成長率目線: 平均log +0.000571 / 幾何平均 +0.057% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $102.25

## 4. Latest Market Context

- 更新: 2026-05-07T03:17:31.077323+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81030.4
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +219.44% | $1,274,084.23 |
| DOGS/USDT:USDT | +74.86% | $8,693,324.11 |
| FHE/USDT:USDT | +33.65% | $16,077,914.49 |
| PENGUIN/USDT:USDT | +27.66% | $1,165,434.26 |
| TONCOIN/USDT:USDT | +17.88% | $260,674,910.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +3.11% | +3.17% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.20% | +2.26% |
| UB/USDT:USDT | below_1h_threshold | +1.94% | +1.99% |
| ICP/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |
| NOT/USDT:USDT | below_1h_threshold | +1.30% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
