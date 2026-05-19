# Decision Report

- generated_at: 2026-05-19T22:48:47.630556+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4510**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4510, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.73% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.93** / 初期 $100.00 (+23.93%)
- 確定: 475件 (Win 126 / Loss 164 / Flat 185) / skip 596件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROMPT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $123.93

## 4. Latest Market Context

- 更新: 2026-05-19T22:48:45.015337+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=76704.4
- Funnel: target 759 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +55.31% | $8,885,206.61 |
| EDEN/USDT:USDT | +28.89% | $15,693,788.89 |
| BSB/USDT:USDT | +14.38% | $35,005,768.01 |
| BANANAS31/USDT:USDT | +14.19% | $1,359,542.89 |
| LIT/USDT:USDT | +13.97% | $3,373,100.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +1.68% | +1.99% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.97% | +1.28% |
| XMR/USDT:USDT | below_1h_threshold | +0.55% | +0.85% |
| LAB/USDT:USDT | below_1h_threshold | +0.44% | +0.75% |
| PENGU/USDT:USDT | below_1h_threshold | +0.37% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
