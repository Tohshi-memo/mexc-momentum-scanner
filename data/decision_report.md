# Decision Report

- generated_at: 2026-06-08T00:24:56.804854+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6011**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6011, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.34% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 2/17 | 11.8% | +0.90% | **+0.11%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.40% | **+1.26%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.81** / 初期 $100.00 (+55.81%)
- 確定: 1128件 (Win 277 / Loss 341 / Flat 510) / skip 1444件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $155.81

## 4. Latest Market Context

- 更新: 2026-06-08T00:24:53.967703+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63253.3
- Funnel: target 772 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +27.93% | $4,279,371.61 |
| PIPPIN/USDT:USDT | +23.29% | $5,736,792.07 |
| BEAT/USDT:USDT | +21.99% | $84,551,798.17 |
| BLESS/USDT:USDT | +18.93% | $9,047,116.99 |
| EPIC/USDT:USDT | +14.22% | $1,444,705.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.37% | +3.44% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +2.94% |
| ALLO/USDT:USDT | below_1h_threshold | +2.73% | +2.80% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +2.64% | +2.71% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
