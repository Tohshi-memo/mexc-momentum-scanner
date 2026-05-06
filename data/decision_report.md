# Decision Report

- generated_at: 2026-05-06T09:37:29.752311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3439**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3439, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.31% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.72% | **+1.55%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.20% | **+1.43%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.69% | **+1.21%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.61% | **+1.13%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.85% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定: 1件 (Win 0 / Loss 0 / Flat 1) / skip 0件
- 成長率目線: 平均log +0.000000 / 幾何平均 +0.000% per trade / maxDD +0.00%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $100.00

## 4. Latest Market Context

- 更新: 2026-05-06T09:37:26.622993+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81912.0
- Funnel: target 769 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1, 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +47.27% | $10,696,707.75 |
| B3/USDT:USDT | +34.51% | $1,469,210.65 |
| ZEC/USDT:USDT | +33.17% | $750,529,986.97 |
| FHE/USDT:USDT | +30.71% | $28,822,706.68 |
| STORJ/USDT:USDT | +26.73% | $2,607,478.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.02% | +3.01% |
| PYTH/USDT:USDT | below_1h_threshold | +2.01% | +2.00% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.94% | +1.93% |
| AKT/USDT:USDT | below_1h_threshold | +1.88% | +1.87% |
| AR/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
