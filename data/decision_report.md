# Decision Report

- generated_at: 2026-06-01T01:40:29.784239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5258**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5258, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.34% | **+1.05%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.55% | **+1.01%** |
| LIMIT_BB3S_LONG | 7/10 | 70.0% | +1.31% | **+0.92%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.49% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.01** / 初期 $100.00 (+33.01%)
- 確定: 891件 (Win 207 / Loss 266 / Flat 418) / skip 928件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $133.01

## 4. Latest Market Context

- 更新: 2026-06-01T01:40:26.550560+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=73584.3
- Funnel: target 777 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +138.84% | $23,894,216.86 |
| H/USDT:USDT | +70.43% | $17,354,367.90 |
| STG/USDT:USDT | +20.16% | $22,047,187.81 |
| HOME/USDT:USDT | +18.45% | $3,638,390.12 |
| CTR/USDT:USDT | +17.99% | $1,425,131.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +2.85% | +3.22% |
| WLD/USDT:USDT | below_1h_threshold | +2.41% | +2.77% |
| MEGA/USDT:USDT | below_1h_threshold | +2.28% | +2.64% |
| BILL/USDT:USDT | below_1h_threshold | +2.18% | +2.55% |
| MEME/USDT:USDT | below_1h_threshold | +1.99% | +2.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
