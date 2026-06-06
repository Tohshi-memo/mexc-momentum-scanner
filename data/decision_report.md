# Decision Report

- generated_at: 2026-06-06T16:57:46.664057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5868**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5868, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.77% | **+1.66%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.71% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1415件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T16:57:39.313264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=60689.1
- Funnel: target 771 → liquid 141 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +9.76% | $6,888,683.33 |
| HEI/USDT:USDT | +6.56% | $5,755,230.54 |
| MYX/USDT:USDT | +5.26% | $1,167,020.17 |
| PLAY/USDT:USDT | +4.22% | $1,282,564.42 |
| HOME/USDT:USDT | +3.81% | $10,501,518.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.25% | +4.36% |
| HOME/USDT:USDT | below_1h_threshold | +3.81% | +3.92% |
| SLX/USDT:USDT | below_1h_threshold | +3.01% | +3.11% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.57% | +2.68% |
| BTW/USDT:USDT | below_1h_threshold | +2.47% | +2.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
